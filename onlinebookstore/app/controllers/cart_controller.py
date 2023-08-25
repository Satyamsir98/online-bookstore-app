from flask import Blueprint, request, jsonify
from app.services.cart_service import CartService

cart_bp = Blueprint('cartbp', __name__, url_prefix='/cartbp')

cart_service = CartService()

@cart_bp.route('/carts', methods=['GET'])
def get_all_carts():
    return cart_service.get_all_carts()

@cart_bp.route('/carts/<int:cart_id>', methods=['GET'])
def get_cart(cart_id):
    return cart_service.get_cart(cart_id)

@cart_bp.route('/carts/user/<int:user_id>', methods=['GET'])
def get_cart_by_user_id(user_id):
    return cart_service.get_cart_by_user_id(user_id)

@cart_bp.route('/carts', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    user_id = data.get('user_id')
    book_id = data.get('book_id')
    quantity = data.get('quantity')

    if not user_id or not book_id or not quantity:
        return jsonify({"message": "Missing required fields: user_id, book_id, and quantity"}), 400

    return cart_service.add_to_cart(user_id, book_id, quantity)

@cart_bp.route('/carts/<int:cart_id>', methods=['PUT'])
def update_cart(cart_id):
    data = request.get_json()
    new_quantity = data.get('quantity')

    if new_quantity is None:
        return jsonify({"message": "Missing required field: quantity"}), 400

    return cart_service.update_cart(cart_id, new_quantity)

@cart_bp.route('/carts/<int:cart_id>', methods=['DELETE'])
def delete_cart(cart_id):
    return cart_service.delete_cart(cart_id)

@cart_bp.route('/carts/user/<int:user_id>/book/<int:book_id>', methods=['DELETE'])
def delete_book_in_cart(user_id, book_id):
    return cart_service.delete_book_in_cart_by_user_id(user_id, book_id)
