import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-registeruser',
  templateUrl: './registeruser.component.html',
  styleUrls: ['./registeruser.component.css']
})
export class RegisterUserComponent {
  registerForm: FormGroup;
  isSubmitting = false;
  errorMessage: string | null = null;

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private router: Router
  ) {
    this.registerForm = this.fb.group({
      name: ['', [Validators.required, Validators.minLength(3)]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]],
      phoneNumber: ['', [
        Validators.required, 
        Validators.pattern('^[0-9]{10}$') // Validate 10 digits phone number
      ]],
      role: ['', [Validators.required]]
    });
  }

  onRegister(): void {
    if (this.registerForm.valid) {
      this.isSubmitting = true;
      this.errorMessage = null;

      const { name, email, password, phoneNumber, role } = this.registerForm.value;

      this.authService.register(name, email, password, phoneNumber, role).subscribe({
        next: (response) => {
          this.router.navigate(['']);  // Redirect to login after successful registration
        },
        error: (error) => {
          this.isSubmitting = false;
          this.errorMessage = 'Registration failed. Please try again.';
          console.error(error);
        }
      });
    } else {
      this.errorMessage = 'Please fill all required fields correctly.';
    }
  }
}
