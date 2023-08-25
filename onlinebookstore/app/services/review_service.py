from flask import jsonify
from app.models.review_model import Review
from app.extensions import db

class ReviewService:
    @staticmethod
    def get_reviews_by_book(book_id):
        reviews = Review.query.filter_by(book_id=book_id).all()
        return jsonify([{
            "review_id": review.id,
            "rating": review.rating,
            "review_text": review.review_text,
            "user_id": review.user_id  # Added user_id to include user info in the review
        } for review in reviews]), 200

    @staticmethod
    def get_reviews_by_user(user_id):
        reviews = Review.query.filter_by(user_id=user_id).all()
        return jsonify([{
            "review_id": review.id,
            "book_id": review.book_id,
            "rating": review.rating,
            "review_text": review.review_text,
            "book_title": review.book.title  # Assuming 'Book' model has a 'title' field
        } for review in reviews]), 200

    @staticmethod
    def add_review(user_id, data):
        new_review = Review(
            user_id=user_id,  # Refers to the user table (could be Customer, Admin, etc.)
            book_id=data['book_id'],
            rating=data['rating'],
            review_text=data['review_text']
        )
        db.session.add(new_review)
        db.session.commit()
        return jsonify({"message": "Review added successfully!"}), 201

    @staticmethod
    def update_review(review_id, data):
        review = Review.query.get(review_id)
        if not review:
            return jsonify({"message": "Review not found"}), 404

        review.rating = data.get('rating', review.rating)
        review.review_text = data.get('review_text', review.review_text)
        db.session.commit()
        return jsonify({"message": "Review updated successfully!"}), 200

    @staticmethod
    def delete_review(review_id):
        review = Review.query.get(review_id)
        if not review:
            return jsonify({"message": "Review not found"}), 404

        db.session.delete(review)
        db.session.commit()
        return jsonify({"message": "Review deleted successfully!"}), 200
