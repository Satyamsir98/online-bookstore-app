import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-customernav',
  templateUrl: './customernav.component.html',
  styleUrls: ['./customernav.component.css']
})
export class CustomernavComponent {
  customerName: string = localStorage.getItem('name') || 'Customer';
  userId: number;
  constructor(private router: Router) {
    this.userId = Number(localStorage.getItem('id'));
  }

  logout(): void {
    localStorage.clear();
    this.router.navigate(['']);
  }
}
