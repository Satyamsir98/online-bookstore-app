from flask import jsonify
from app.repositories.order_repository import OrderRepository

class OrderService:
    def place_order(self, user_id, book_id):
        # Add the new order
        new_order = OrderRepository.add_order(user_id, book_id)
        if new_order:
            return jsonify({
                "message": "Order placed successfully!",
                "order_id": new_order.id,
                "status": new_order.order_status
            }), 201
        return jsonify({"message": "Failed to place order"}), 400

    def update_order(self, order_id, status):
        # Update the order status
        order = OrderRepository.update_order(order_id, status)
        if order:
            return jsonify({
                "message": "Order updated successfully!",
                "order_id": order.id,
                "new_status": order.order_status
            }), 200
        return jsonify({"message": "Order not found"}), 404

    def get_all_orders(self):
        # Get all orders
        orders = OrderRepository.get_all_orders()
        if orders:
            return jsonify([{
                "order_id": order.id,
                "user_id": order.user_id,
                "book_id": order.book_id,
                "order_date": order.order_date,
                "order_status": order.order_status
            } for order in orders]), 200
        return jsonify({"message": "No orders found"}), 404

    def get_order_by_id(self, order_id):
        # Get order by ID
        order = OrderRepository.get_order_by_id(order_id)
        if order:
            return jsonify({
                "order_id": order.id,
                "user_id": order.user_id,
                "book_id": order.book_id,
                "order_date": order.order_date,
                "order_status": order.order_status
            }), 200
        return jsonify({"message": "Order not found"}), 404

    def delete_order(self, order_id):
        # Delete the order
        if OrderRepository.delete_order(order_id):
            return jsonify({"message": "Order deleted successfully!"}), 200
        return jsonify({"message": "Order not found"}), 404

    def get_orders_by_user_id(self, user_id):
        # Get all orders for a specific user
        orders = OrderRepository.get_orders_by_user_id(user_id)
        if orders:
            return jsonify([{
                "order_id": order.id,
                "book_id": order.book_id,
                "order_date": order.order_date,
                "order_status": order.order_status
            } for order in orders]), 200
        return jsonify({"message": "No orders found for this user"}), 404
