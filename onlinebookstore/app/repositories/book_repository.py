from app.extensions import db
from app.models.book_model import Book

class BookRepository:
    @staticmethod
    def get_all_books():
        return Book.query.all()

    @staticmethod
    def get_book_by_id(book_id):
        return Book.query.get(book_id)

    @staticmethod
    def get_books_by_bookstore(bookstore_id):
        return Book.query.filter_by(bookstore_id=bookstore_id).all()

    @staticmethod
    def create_book(book):
        db.session.add(book)
        db.session.commit()

    @staticmethod
    def update_book(book):
        db.session.commit()

    @staticmethod
    def delete_book(book):
        db.session.delete(book)
        db.session.commit()
