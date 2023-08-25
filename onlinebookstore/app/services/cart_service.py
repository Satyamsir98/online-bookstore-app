from app.models.cart_model import Cart
from app import db
from flask import jsonify

class CartService:
    
    def get_all_carts(self):
        carts = Cart.query.all()
        return jsonify([{
            "id": cart.id,
            "user_id": cart.user_id,
            "book_id": cart.book_id,
            "quantity": cart.quantity
        } for cart in carts]), 200

    def get_cart(self, cart_id):
        cart = Cart.query.get(cart_id)
        if not cart:
            return jsonify({"message": "Cart item not found"}), 404
        return jsonify({
            "id": cart.id,
            "user_id": cart.user_id,
            "book_id": cart.book_id,
            "quantity": cart.quantity
        }), 200

    def get_cart_by_user_id(self, user_id):
        carts = Cart.query.filter_by(user_id=user_id).all()
        if not carts:
            return jsonify({"message": "No cart items found for this user"}), 404
        return jsonify([{
            "id": cart.id,
            "user_id": cart.user_id,
            "book_id": cart.book_id,
            "quantity": cart.quantity
        } for cart in carts]), 200

    def add_to_cart(self, user_id, book_id, quantity):
        # Check if book already exists in cart for this user
        existing_cart_item = Cart.query.filter_by(user_id=user_id, book_id=book_id).first()
        if existing_cart_item:
            # Update quantity if book already exists in cart
            existing_cart_item.quantity += quantity
        else:
            # Add new cart item
            new_cart_item = Cart(user_id=user_id, book_id=book_id, quantity=quantity)
            db.session.add(new_cart_item)
        
        db.session.commit()
        return jsonify({"message": "Book added to cart successfully!"}), 201

    def update_cart(self, cart_id, new_quantity):
        cart_item = Cart.query.get(cart_id)
        if not cart_item:
            return jsonify({"message": "Cart item not found"}), 404
        
        cart_item.quantity = new_quantity
        db.session.commit()
        return jsonify({"message": "Cart item updated successfully!"}), 200

    def delete_cart(self, cart_id):
        cart_item = Cart.query.get(cart_id)
        if not cart_item:
            return jsonify({"message": "Cart item not found"}), 404
        
        db.session.delete(cart_item)
        db.session.commit()
        return jsonify({"message": "Cart item deleted successfully!"}), 200

    def delete_book_in_cart_by_user_id(self, user_id, book_id):
        cart_item = Cart.query.filter_by(user_id=user_id, book_id=book_id).first()
        if not cart_item:
            return jsonify({"message": "Book not found in cart"}), 404
        
        db.session.delete(cart_item)
        db.session.commit()
        return jsonify({"message": "Book removed from cart successfully!"}), 200
