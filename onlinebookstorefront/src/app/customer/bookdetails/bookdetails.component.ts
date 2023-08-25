import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { BookService } from 'src/app/services/book.service';
import { CartService } from 'src/app/services/cart.service';
import { OrderService } from 'src/app/services/order.service';

@Component({
  selector: 'app-bookdetails',
  templateUrl: './bookdetails.component.html',
  styleUrls: ['./bookdetails.component.css']
})
export class BookDetailsComponent implements OnInit {
  bookId!: number;
  book: any;
  isLoading: boolean = true;
  errorMessage: string = '';
  
  constructor(
    private route: ActivatedRoute,
    private bookService: BookService,
    private cartService: CartService,
    private orderService: OrderService,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.bookId = +params['id']; // Get the book ID from the route
      this.fetchBookDetails();
    });
  }

  fetchBookDetails(): void {
    this.bookService.getBook(this.bookId).subscribe({
      next: (data) => {
        this.book = data;
        console.log(this.book)
        this.isLoading = false;
      },
      error: (err) => {
        this.errorMessage = 'Error fetching book details.';
        this.isLoading = false;
      }
    });
  }

  addToCart(): void {
    const userId = localStorage.getItem('id'); // Get user ID from localStorage
    const quantity = 1; // Assuming quantity is 1 for now
    
    if (userId) {
      this.cartService.addToCart(+userId, this.bookId, quantity).subscribe({
        next: () => {
          alert('Book added to cart!');
          this.router.navigate(['/customer/cart/userId']);
        },
        error: () => {
          alert('Failed to add book to cart.');
        }
      });
    } else {
      alert('User not logged in.');
    }
  }

  placeOrder(): void {
    const userId = localStorage.getItem('id'); // Get user ID from localStorage
    
    if (userId) {
      this.orderService.placeOrder(+userId, this.bookId).subscribe({
        next: (response) => {
          alert('Order placed successfully!');
          this.router.navigate(['/customer/order-history/userId']);
        },
        error: (err) => {
          alert('Failed to place order.');
        }
      });
    } else {
      alert('User not logged in.');
    }
  }
}
