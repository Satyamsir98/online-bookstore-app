import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { BookService } from 'src/app/services/book.service';

@Component({
  selector: 'app-editbook',
  templateUrl: './editbook.component.html',
  styleUrls: ['./editbook.component.css']
})
export class EditbookComponent {
  bookId!: number;
  book: any = {
    title: '',
    author: '',
    genre: '',
    price: 0,
    publication_date: ''
  };
  errorMessage = '';

  constructor(
    private route: ActivatedRoute,
    private bookService: BookService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.bookId = +this.route.snapshot.params['id'];
    this.fetchBookDetails();
  }

  fetchBookDetails(): void {
    this.bookService.getBook(this.bookId).subscribe({
      next: (data) => {
        this.book = data;
      },
      error: () => {
        this.errorMessage = 'Error fetching book details.';
      }
    });
  }

  updateBook(): void {
    this.bookService.updateBook(this.bookId, this.book).subscribe({
      next: () => {
        alert('Book updated successfully!');
        this.router.navigate(['/bookstore']);
      },
      error: () => {
        this.errorMessage = 'Error updating book.';
      }
    });
  }

}
