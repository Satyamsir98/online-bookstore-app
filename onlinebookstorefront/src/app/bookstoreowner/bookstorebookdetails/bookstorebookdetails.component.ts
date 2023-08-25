import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { BookService } from 'src/app/services/book.service';

@Component({
  selector: 'app-bookstorebookdetails',
  templateUrl: './bookstorebookdetails.component.html',
  styleUrls: ['./bookstorebookdetails.component.css']
})
export class BookstorebookdetailsComponent {
  bookId!: number;
  book: any;
  isLoading: boolean = true;
  errorMessage: string = '';
  
  constructor(
    private route: ActivatedRoute,
    private bookService: BookService,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.bookId = +params['id']; // Get the book ID from the route
      this.fetchBookDetails();
    });
  }

  fetchBookDetails(): void {
    this.bookService.getBook(this.bookId).subscribe({
      next: (data) => {
        this.book = data;
        this.isLoading = false;
      },
      error: () => {
        this.errorMessage = 'Error fetching book details.';
        this.isLoading = false;
      }
    });
  }
  deleteBook(): void {
    if (confirm('Are you sure you want to delete this book?')) {
      this.bookService.deleteBook(this.bookId).subscribe({
        next: () => {
          alert('Book deleted successfully!');
          this.router.navigate(['/bookstore']);
        },
        error: () => {
          alert('Error deleting book.');
        }
      });
    }
  }

  editBook(): void {
    this.router.navigate([`/bookstoreowner/editbook/${this.bookId}`]);
  }

}
