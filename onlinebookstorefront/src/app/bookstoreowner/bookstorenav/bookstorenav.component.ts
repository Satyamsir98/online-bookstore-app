import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-bookstorenav',
  templateUrl: './bookstorenav.component.html',
  styleUrls: ['./bookstorenav.component.css']
})
export class BookstorenavComponent {
  bookstoreOwnerName: string = localStorage.getItem('name') || 'BookStore Owner';
    userId: number;
    constructor(private router: Router) {
      this.userId = Number(localStorage.getItem('id'));
    }
  
    logout(): void {
      localStorage.clear();
      this.router.navigate(['']);
    }

}
