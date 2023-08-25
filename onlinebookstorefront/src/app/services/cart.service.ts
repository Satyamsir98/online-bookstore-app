import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Cart } from '../models/cart.model';  // Ensure this model is defined based on your backend Cart model

@Injectable({
  providedIn: 'root'
})
export class CartService {
  private apiUrl = 'http://localhost:5000/cartbp'; // Updated to match backend URL

  constructor(private http: HttpClient) { }

  // Get all carts
  getAllCarts(): Observable<Cart[]> {
    return this.http.get<Cart[]>(`${this.apiUrl}/carts`);
  }

  // Get a specific cart by ID
  getCart(cartId: number): Observable<Cart> {
    return this.http.get<Cart>(`${this.apiUrl}/carts/${cartId}`);
  }

  // Get the cart for a specific user
  getCartByUserId(userId: number): Observable<Cart[]> {
    return this.http.get<Cart[]>(`${this.apiUrl}/carts/user/${userId}`);
  }

  // Add a book to the cart (requires user_id, book_id, and quantity)
  addToCart(userId: number, bookId: number, quantity: number): Observable<Cart> {
    const body = { user_id: userId, book_id: bookId, quantity: quantity };
    return this.http.post<Cart>(`${this.apiUrl}/carts`, body);
  }

  // Update the quantity of a book in the cart
  updateCart(cartId: number, newQuantity: number): Observable<Cart> {
    const body = { quantity: newQuantity };
    return this.http.put<Cart>(`${this.apiUrl}/carts/${cartId}`, body);
  }

  // Delete a cart
  deleteCart(cartId: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/carts/${cartId}`);
  }

  // Delete a specific book in the user's cart
  deleteBookInCart(userId: number, bookId: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/carts/user/${userId}/book/${bookId}`);
  }
}
