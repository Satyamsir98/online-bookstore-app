import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { BookService } from 'src/app/services/book.service';

@Component({
  selector: 'app-bookstoreownerdashboard',
  templateUrl: './bookstoreownerdashboard.component.html',
  styleUrls: ['./bookstoreownerdashboard.component.css']
})
export class BookstoreownerdashboardComponent implements OnInit {
  books: any[] = [];
  bookstoreName: string = '';
  currentPage = 1;
  pageSize = 6;
  totalBooks = 0;

  constructor(private bookService: BookService, private router: Router) {}

  ngOnInit(): void {
    this.bookstoreName = localStorage.getItem('name') || 'Bookstore Owner';
    const role = localStorage.getItem('role');
    const bookstoreId = Number(localStorage.getItem('id'));

    if (role === 'Bookstore Owner') {
      this.loadBooksByBookstore(bookstoreId);
    } else {
      this.router.navigate(['']); // Redirect if not a bookstore owner
    }
  }

  loadBooksByBookstore(bookstoreId: number): void {
    this.bookService.getAllBooks().subscribe({
      next: (data) => {
        this.books = data.filter(book => book.bookstore_id === bookstoreId);
        this.totalBooks = this.books.length;
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
    return Math.ceil(this.totalBooks / this.pageSize);
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
    this.router.navigate([`/bookstoreowner/book-details/${bookId}`]);
  }

}
