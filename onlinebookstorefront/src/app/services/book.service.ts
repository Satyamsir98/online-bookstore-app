import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Book } from '../models/book.model'; // Ensure this model is defined based on your backend Book model

@Injectable({
  providedIn: 'root'
})
export class BookService {
  private apiUrl = 'http://localhost:5000/bookbp'; // Updated to match backend URL

  constructor(private http: HttpClient) { }

  // Get all books
  getAllBooks(): Observable<Book[]> {
    return this.http.get<Book[]>(`${this.apiUrl}/books`);
  }

  // Get a book by ID
  getBook(bookId: number): Observable<Book> {
    return this.http.get<Book>(`${this.apiUrl}/books/${bookId}`);
  }

  // Add a new book (requires JWT token)
  addBook(book: Book): Observable<Book> {
    const token = localStorage.getItem('token'); // Assuming you store JWT token in localStorage
    const headers = new HttpHeaders().set('Authorization', `Bearer ${token}`);
    return this.http.post<Book>(`${this.apiUrl}/books`, book, { headers });
  }

  // Update a book (requires JWT token)
  updateBook(bookId: number, book: Book): Observable<Book> {
    const token = localStorage.getItem('token'); // Assuming you store JWT token in localStorage
    const headers = new HttpHeaders().set('Authorization', `Bearer ${token}`);
    return this.http.put<Book>(`${this.apiUrl}/books/${bookId}`, book, { headers });
  }

  // Delete a book (requires JWT token)
  deleteBook(bookId: number): Observable<void> {
    const token = localStorage.getItem('token'); // Assuming you store JWT token in localStorage
    const headers = new HttpHeaders().set('Authorization', `Bearer ${token}`);
    return this.http.delete<void>(`${this.apiUrl}/books/${bookId}`, { headers });
  }
}
