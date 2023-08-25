from flask import Blueprint, request, jsonify
from app.services.order_service import OrderService

order_bp = Blueprint('order_bp', __name__)

# Initialize OrderService
order_service = OrderService()

# Place an order
@order_bp.route('/orders', methods=['POST'])
def place_order():
    data = request.get_json()
    user_id = data.get('user_id')
    book_id = data.get('book_id')

    if not user_id or not book_id:
        return jsonify({"message": "User ID and Book ID are required"}), 400

    return order_service.place_order(user_id, book_id)

# Update an order
@order_bp.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.get_json()
    status = data.get('status')

    if not status:
        return jsonify({"message": "Order status is required"}), 400

    return order_service.update_order(order_id, status)

# Get all orders
@order_bp.route('/orders', methods=['GET'])
def get_all_orders():
    return order_service.get_all_orders()

# Get an order by ID
@order_bp.route('/orders/<int:order_id>', methods=['GET'])
def get_order_by_id(order_id):
    return order_service.get_order_by_id(order_id)

# Delete an order
@order_bp.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    return order_service.delete_order(order_id)

# Get all orders by User ID
@order_bp.route('/orders/user/<int:user_id>', methods=['GET'])
def get_orders_by_user_id(user_id):
    return order_service.get_orders_by_user_id(user_id)
