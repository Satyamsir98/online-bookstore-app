import { Component } from '@angular/core';
import { AuthService } from '../services/auth.service';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  loginForm: FormGroup;  // Declare the loginForm
  isSubmitting = false;
  errorMessage: string | null = null;

  constructor(
    private authService: AuthService,
    private router: Router,
    private fb: FormBuilder  // Inject FormBuilder
  ) {
    // Initialize the form group with controls
    this.loginForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]],
    });
  }

  // Handle form submission
  onLogin(): void {
    if (this.loginForm.valid) {
      this.isSubmitting = true;
      this.errorMessage = null;

      const { email, password } = this.loginForm.value;

      this.authService.login(email, password).subscribe({
        next: (response) => {
          const decodedToken = this.authService.decodedToken(response.token); // Call the decodedToken method

          // Store token, role, and user data in localStorage
          localStorage.setItem('token', response.token);
          localStorage.setItem('role', decodedToken.role); // Assuming the token has a 'role' field
          localStorage.setItem('id', decodedToken.id); // Assuming the token has an 'id' field
          localStorage.setItem('name', decodedToken.name); // Assuming the token has a 'name' field
          localStorage.setItem('email', decodedToken.email); // Assuming the token has an 'email' field

          this.redirectBasedOnRole(decodedToken.role); // Use decoded role to redirect
        },
        error: (error) => {
          this.isSubmitting = false;
          this.errorMessage = 'Invalid credentials. Please try again.';
          console.error(error);
        }
      });
    } else {
      this.errorMessage = 'Please enter both email and password correctly.';
    }
  }

  // Redirect user based on role
  private redirectBasedOnRole(role: string): void {
    if (role === 'Customer') {
      this.router.navigate(['/customer']);
    } else if (role === 'Bookstore Owner') {
      this.router.navigate(['/bookstore']);
    } else if (role === 'Admin') {
      this.router.navigate(['/admin']);
    }
  }
}
