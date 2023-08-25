import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { JwtHelperService } from '@auth0/angular-jwt';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = 'http://localhost:5000/authbp'; // Change this to your backend URL

  constructor(private http: HttpClient) { }

  // Login method
  login(email: string, password: string): Observable<any> {
    const body = { email, password };
    return this.http.post(`${this.apiUrl}/login`, body);
  }

  register(name: string, email: string, password: string, phoneNumber: string, role: string): Observable<any> {
    // Check if the role is valid
    if (role !== 'Customer' && role !== 'Bookstore Owner') {
      throw new Error("Invalid role. Only 'Customer' and 'Bookstore Owner' are allowed.");
    }
  
    const body = { name, email, password, phone_number: phoneNumber, role };
    return this.http.post(`${this.apiUrl}/register`, body);
  }
  

  // Logout method
  logout(): void {
    // Remove the user and token from localStorage to log out
    localStorage.removeItem('user');
    localStorage.removeItem('token');
  }

  // Method to check if the user is authenticated
  isAuthenticated(): boolean {
    // Check if there's a token in localStorage and if it's still valid
    const token = localStorage.getItem('token');
    if (token) {
      const jwtHelper = new JwtHelperService();
      return !jwtHelper.isTokenExpired(token);  // Check if token is expired
    }
    return false;
  }

  // Get current user's name
  getCurrentUserName(): string | null {
    const user = localStorage.getItem('user');
    if (user) {
      return JSON.parse(user).name; // Assuming 'user' contains user details with a 'name' property
    }
    return null;
  }

  // Decode the JWT token
  decodedToken(tokenval: any) {
    const jwthelper = new JwtHelperService();
    const token = jwthelper.decodeToken(tokenval);
    return token;
  }
}
