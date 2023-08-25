from app.extensions import db
from app.models.cart_model import Cart
from app.models.user_model import User
from app.models.book_model import Book

class CartRepository:
    @staticmethod
    def get_all_carts():
        """Fetches all cart items."""
        return Cart.query.all()

    @staticmethod
    def get_cart_by_id(cart_id):
        """Fetches a cart item by its ID."""
        return Cart.query.get(cart_id)

    @staticmethod
    def get_cart_by_user_id(user_id):
        """Fetches all cart items for a specific user."""
        return Cart.query.filter_by(user_id=user_id).all()

    @staticmethod
    def delete_cart(cart_id):
        """Deletes a cart item by its ID."""
        cart_item = Cart.query.get(cart_id)
        if cart_item:
            db.session.delete(cart_item)
            db.session.commit()
            return True
        return False

    @staticmethod
    def delete_book_in_cart_by_user_id(user_id, book_id):
        """Deletes a specific book from a user's cart."""
        cart_item = Cart.query.filter_by(user_id=user_id, book_id=book_id).first()
        if cart_item:
            db.session.delete(cart_item)
            db.session.commit()
            return True
        return False

    @staticmethod
    def add_to_cart(user_id, book_id, quantity):
        """Adds a book to the user's cart."""
        existing_cart_item = Cart.query.filter_by(user_id=user_id, book_id=book_id).first()
        if existing_cart_item:
            # If the book already exists in the cart, update the quantity
            existing_cart_item.quantity += quantity
        else:
            # Add a new cart item
            new_cart_item = Cart(user_id=user_id, book_id=book_id, quantity=quantity)
            db.session.add(new_cart_item)
        db.session.commit()

    @staticmethod
    def update_cart(cart_id, new_quantity):
        """Updates the quantity of a cart item."""
        cart_item = Cart.query.get(cart_id)
        if cart_item:
            cart_item.quantity = new_quantity
            db.session.commit()
            return True
        return False
