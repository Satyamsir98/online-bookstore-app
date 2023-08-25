import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { BookService } from 'src/app/services/book.service';

@Component({
  selector: 'app-addbook',
  templateUrl: './addbook.component.html',
  styleUrls: ['./addbook.component.css']
})
export class AddbookComponent {
  book: any = {
    title: '',
    author: '',
    genre: '',
    price: null,
    publication_date: ''
  };
  errorMessage = '';

  constructor(
    private bookService: BookService,
    private router: Router
  ) {}

  addBook(): void {
    const role = localStorage.getItem('role');
    const bookstoreId = localStorage.getItem('id');

    if (role !== 'Bookstore Owner') {
      alert('Unauthorized: Only Bookstore Owners can add books.');
      return;
    }

    if (!bookstoreId) {
      this.errorMessage = 'Error: No bookstore ID found in localStorage.';
      return;
    }

    this.book.bookstore_id = +bookstoreId; // Safely assign bookstore ID after checking null

    this.bookService.addBook(this.book).subscribe({
      next: () => {
        alert('Book added successfully!');
        this.router.navigate(['/bookstore']);
      },
      error: (err) => {
        this.errorMessage = 'Error adding book. Please try again.';
      }
    });
  }

}
