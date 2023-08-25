export interface Book {
    id: number;
    title: string;
    author: string;
    genre?: string;  // Optional as it might not always be provided
    price: number;
    publication_date?: string;  // Using string to match a date format (you can parse it later)
    bookstore_id: number;
    orders?: any[];  // Optional, could represent the orders related to this book
    reviews?: any[];  // Optional, could represent the reviews related to this book
  }
  