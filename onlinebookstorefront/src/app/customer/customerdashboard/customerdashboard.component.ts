import { Component, OnInit } from '@angular/core';
import { BookService } from '../../services/book.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-customer-dashboard',
  templateUrl: './customerdashboard.component.html',
  styleUrls: ['./customerdashboard.component.css']
})
export class CustomerDashboardComponent implements OnInit {
  books: any[] = [];
  customerName: string = '';
  currentPage = 1;
  pageSize = 6;
  totalBooks = 0;

  constructor(private bookService: BookService, private router: Router) {}

  ngOnInit(): void {
    this.loadBooks();
    this.customerName = localStorage.getItem('name') || 'Customer';
  }

  loadBooks(): void {
    this.bookService.getAllBooks().subscribe({
      next: (data) => {
        this.books = data;
        this.totalBooks = data.length;
      },
      error: (err) => {
        console.error('Error loading books:', err);
      }
    });
  }

  get paginatedBooks(): any[] {
    const startIndex = (this.currentPage - 1) * this.pageSize;
    return this.books.slice(startIndex, startIndex + this.pageSize);
  }

  getTotalPages(): number {
    return Math.ceil(this.totalBooks / this.pageSize); // Added helper method
  }

  nextPage(): void {
    if (this.currentPage < this.getTotalPages()) {
      this.currentPage++;
    }
  }

  prevPage(): void {
    if (this.currentPage > 1) {
      this.currentPage--;
    }
  }

  viewBookDetails(bookId: number): void {
    this.router.navigate([`/customer/book-details/${bookId}`]);
  }
}
