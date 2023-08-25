import { Book } from './book.model';

export interface Order {
    id: number;
    user_id: number;
    book_id: number;
    order_date: string;  // Using string to represent DateTime in ISO format
    order_status: string;
    books: Book[];
  }
  