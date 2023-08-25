from datetime import datetime
from flask import jsonify
from app.models.book_model import Book
from app.extensions import db

class BookService:
    def get_all_books(self):
        books = Book.query.all()
        return jsonify([{
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "genre": book.genre,
        "price": book.price,
        "publication_date": book.publication_date,
        "bookstore_id": book.bookstore_id
    } for book in books]), 200

    def get_book(self, book_id):
    # Retrieve the book by ID from the database
        book = Book.query.get(book_id)
        
        # If the book doesn't exist, return an error message
        if not book:
            return jsonify({"message": "Book not found"}), 404
        
        # Return the full details of the book
        return jsonify({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "genre": book.genre,  # Added genre
            "price": book.price,
            "publication_date": book.publication_date,  # Added publication date
            "bookstore_id": book.bookstore_id  # Added bookstore ID
        }), 200


    def add_book(self, data):
        publication_date = datetime.strptime(data['publication_date'], '%Y-%m-%d').date()
        new_book = Book(
            title=data['title'],
            author=data['author'],
            genre=data.get('genre'),
            price=data['price'],
            publication_date=publication_date,
            bookstore_id=data['bookstore_id']
        )
        db.session.add(new_book)
        db.session.commit()
        return jsonify({"message": "Book added successfully!"}), 201

    def update_book(self, book_id, data):
        book = Book.query.get(book_id)
        if not book:
            return jsonify({"message": "Book not found"}), 404

        book.title = data.get('title', book.title)
        book.author = data.get('author', book.author)
        book.genre = data.get('genre', book.genre)
        book.price = data.get('price', book.price)
        db.session.commit()
        return jsonify({"message": "Book updated successfully!"}), 200

    def delete_book(self, book_id):
        book = Book.query.get(book_id)
        if not book:
            return jsonify({"message": "Book not found"}), 404

        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": "Book deleted successfully!"}), 200
