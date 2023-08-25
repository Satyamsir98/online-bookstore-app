from flask import Blueprint, request, jsonify
from app.services.review_service import ReviewService

review_bp = Blueprint('review_controller', __name__)

@review_bp.route('/reviews/book/<int:book_id>', methods=['GET'])
def get_reviews_by_book(book_id):
    return ReviewService.get_reviews_by_book(book_id)

@review_bp.route('/reviews/user/<int:user_id>', methods=['GET'])
def get_reviews_by_user(user_id):
    return ReviewService.get_reviews_by_user(user_id)

@review_bp.route('/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    user_id = data.get('user_id')  # User ID should be passed in the request
    if not user_id or not data.get('book_id') or not data.get('rating'):
        return jsonify({"message": "Missing required fields"}), 400

    return ReviewService.add_review(user_id, data)

@review_bp.route('/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.get_json()
    return ReviewService.update_review(review_id, data)

@review_bp.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    return ReviewService.delete_review(review_id)
