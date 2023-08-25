export interface Cart {
    id?: number; // Optional, since it may not be present when creating a new cart
    user_id: number; // The ID of the user who owns the cart
    book_id: number; // The ID of the book in the cart
    quantity: number; // The quantity of the book in the cart
  }


  