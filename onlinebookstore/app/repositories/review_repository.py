from app.extensions import db
from app.models.review_model import Review

class ReviewRepository:
    @staticmethod
    def get_reviews_by_book(book_id):
        # Fetch reviews for a particular book using the book_id
        return Review.query.filter_by(book_id=book_id).all()

    @staticmethod
    def get_reviews_by_user(user_id):
        # Fetch reviews by a user, using user_id instead of customer_id
        return Review.query.filter_by(user_id=user_id).all()

    @staticmethod
    def create_review(review):
        db.session.add(review)
        db.session.commit()

    @staticmethod
    def update_review(review):
        db.session.commit()

    @staticmethod
    def delete_review(review):
        db.session.delete(review)
        db.session.commit()
