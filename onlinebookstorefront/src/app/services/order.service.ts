import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Order } from '../models/order.model'; // Ensure this model is defined based on your backend Order model
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class OrderService {
  private apiUrl = environment.apiUrl + '/orderbp'; // Change this to your backend URL

  constructor(private http: HttpClient) { }

  // Place an order
  placeOrder(userId: number, bookId: number): Observable<Order> {
    const body = { user_id: userId, book_id: bookId };
    return this.http.post<Order>(`${this.apiUrl}/orders`, body);
  }

  // Update an order
  updateOrder(orderId: number, status: string): Observable<Order> {
    const body = { status };
    return this.http.put<Order>(`${this.apiUrl}/orders/${orderId}`, body);
  }

  // Get all orders
  getAllOrders(): Observable<Order[]> {
    return this.http.get<Order[]>(`${this.apiUrl}/orders`);
  }

  // Get an order by ID
  getOrderById(orderId: number): Observable<Order> {
    return this.http.get<Order>(`${this.apiUrl}/orders/${orderId}`);
  }

  // Delete an order
  deleteOrder(orderId: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/orders/${orderId}`);
  }

  // Get all orders by User ID
  getOrdersByUserId(userId: number): Observable<Order[]> {
    return this.http.get<Order[]>(`${this.apiUrl}/orders/user/${userId}`);
  }
}
