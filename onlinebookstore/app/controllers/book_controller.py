from flask import Blueprint, request, jsonify
from app.services.book_service import BookService
from flask_jwt_extended import jwt_required

book_bp = Blueprint('book_bp', __name__)
book_service = BookService()

@book_bp.route('/books', methods=['GET'])
def get_all_books():
    return book_service.get_all_books()

@book_bp.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    return book_service.get_book(book_id)

@book_bp.route('/books', methods=['POST'])
# @jwt_required()
def add_book():
    data = request.get_json()
    return book_service.add_book(data)

@book_bp.route('/books/<int:book_id>', methods=['PUT'])
# @jwt_required()
def update_book(book_id):
    data = request.get_json()
    return book_service.update_book(book_id, data)

@book_bp.route('/books/<int:book_id>', methods=['DELETE'])
# @jwt_required()
def delete_book(book_id):
    return book_service.delete_book(book_id)
