import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Book } from 'src/app/models/book.model';
import { Cart } from 'src/app/models/cart.model';
import { BookService } from 'src/app/services/book.service';
import { CartService } from 'src/app/services/cart.service';
import { OrderService } from 'src/app/services/order.service';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css']
})
export class CartComponent implements OnInit {
  cartItems: {
    book_id: number; title: string; author: string; genre?: string; totalPrice: number
}[] = [];
  totalPrice: number = 0;
  isLoading: boolean = false;
  errorMessage: string | null = null;

  constructor(
    private cartService: CartService,
    private bookService: BookService,
    private orderService: OrderService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.isLoading = true;
    const userId = localStorage.getItem('id');
    console.log(userId)
    if (userId) {
      this.cartService.getCartByUserId(Number(userId)).subscribe(
        (cartData: Cart[]) => {
          console.log("cartData", cartData)
          this.cartItems = [];
          this.totalPrice = 0;

          for (const item of cartData) {
            this.bookService.getBook(item.book_id).subscribe(
              (bookDetails: Book) => {
                const cartItem = {
                  book_id: bookDetails.id,
                  title: bookDetails.title,
                  author: bookDetails.author,
                  genre: bookDetails.genre,
                  totalPrice: item.quantity * bookDetails.price
                };
                this.cartItems.push(cartItem);
                console.log(this.cartItems)
                this.calculateTotalPrice();
              },
              (error) => {
                this.errorMessage = 'Failed to fetch book details';
                this.isLoading = false;
              }
            );
          }
          this.isLoading = false;
        },
        () => {
          this.errorMessage = 'Failed to load cart items';
          this.isLoading = false;
        }
      );
    }
  }

  calculateTotalPrice(): void {
    this.totalPrice = this.cartItems.reduce((sum, item) => sum + item.totalPrice, 0);
  }

  removeItemFromCart(bookId: number): void {
    const userId = localStorage.getItem('id');
    if (userId) {
      this.cartService.deleteBookInCart(Number(userId), bookId).subscribe(
        () => {
          // Corrected the comparison by comparing item.book_id with bookId
          this.cartItems = this.cartItems.filter(item => item.book_id !== bookId);
          this.calculateTotalPrice();
        },
        () => {
          this.errorMessage = 'Failed to remove item from cart';
        }
      );
    }
  }
  
  placeOrder(cartItems: any[]): void {
    const userId = localStorage.getItem('id');
    if (userId) {
      for (const item of cartItems){
        const bookId = item.book_id

        this.orderService.placeOrder(Number(userId), bookId).subscribe(
          () => this.router.navigate(['/customer/order-history/userId']),
          () => this.errorMessage = 'Failed to place order'
        );
        this.removeItemFromCart(bookId)
      }
      
    }
  }
}