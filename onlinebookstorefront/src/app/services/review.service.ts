import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Review } from '../models/review.model'; // Ensure this model is defined based on your backend Review model
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ReviewService {
  private apiUrl = environment.apiUrl + '/reviewbp'; // Change this to your backend URL

  constructor(private http: HttpClient) { }

  // Get reviews by Book ID
  getReviewsByBook(bookId: number): Observable<Review[]> {
    return this.http.get<Review[]>(`${this.apiUrl}/reviews/book/${bookId}`);
  }

  // Get reviews by User ID
  getReviewsByUser(userId: number): Observable<Review[]> {
    return this.http.get<Review[]>(`${this.apiUrl}/reviews/user/${userId}`);
  }

  // Add a review (requires user_id, book_id, and rating)
  addReview(userId: number, bookId: number, rating: number, comment: string): Observable<Review> {
    const body = { user_id: userId, book_id: bookId, rating, comment };
    return this.http.post<Review>(`${this.apiUrl}/reviews`, body);
  }

  // Update a review
  updateReview(reviewId: number, rating: number, comment: string): Observable<Review> {
    const body = { rating, comment };
    return this.http.put<Review>(`${this.apiUrl}/reviews/${reviewId}`, body);
  }

  // Delete a review
  deleteReview(reviewId: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/reviews/${reviewId}`);
  }
}
