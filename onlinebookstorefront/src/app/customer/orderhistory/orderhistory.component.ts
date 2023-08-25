import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { Book } from 'src/app/models/book.model';
import { Order } from 'src/app/models/order.model';
import { BookService } from 'src/app/services/book.service';
import { OrderService } from 'src/app/services/order.service';

@Component({
  selector: 'app-orderhistory',
  templateUrl: './orderhistory.component.html',
  styleUrls: ['./orderhistory.component.css']
})
export class OrderhistoryComponent {
  ordersItems: {
      book_id: number; title: string; author: string; genre?: string; totalPrice: number; date : string
  }[] = [];
    totalPrice: number = 0;
    isLoading: boolean = false;
    errorMessage: string | null = null;
  
    constructor(
      private bookService: BookService,
      private orderService: OrderService,
      private router: Router
    ) {}
  
    ngOnInit(): void {
      this.isLoading = true;
      const userId = localStorage.getItem('id');
      console.log(userId)
      if (userId) {
        this.orderService.getOrdersByUserId(Number(userId)).subscribe(
          (ordersData: Order[]) => {
            console.log("ordersData", ordersData)
            this.ordersItems = [];
            this.totalPrice = 0;
  
            for (const item of ordersData) {
              this.bookService.getBook(item.book_id).subscribe(
                (bookDetails: Book) => {
                  const ordersItem = {
                    book_id: bookDetails.id,
                    title: bookDetails.title,
                    author: bookDetails.author,
                    genre: bookDetails.genre,
                    totalPrice: bookDetails.price,
                    date : item.order_date
                  };
                  this.ordersItems.push(ordersItem);
                  console.log(this.ordersItems)
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
            this.errorMessage = 'Failed to load orders items';
            this.isLoading = false;
          }
        );
      }
    }
  
    calculateTotalPrice(): void {
      this.totalPrice = this.ordersItems.reduce((sum, item) => sum + item.totalPrice, 0);
    }

}
