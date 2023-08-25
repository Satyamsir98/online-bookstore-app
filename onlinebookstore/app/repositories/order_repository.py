from app.extensions import db
from app.models.order_model import Order

class OrderRepository:
    @staticmethod
    def add_order(user_id, book_id):
        new_order = Order(
            user_id=user_id,
            book_id=book_id
        )
        db.session.add(new_order)
        db.session.commit()
        return new_order

    @staticmethod
    def update_order(order_id, status):
        order = Order.query.get(order_id)
        if not order:
            return None
        order.order_status = status
        db.session.commit()
        return order

    @staticmethod
    def get_all_orders():
        return Order.query.all()

    @staticmethod
    def get_order_by_id(order_id):
        return Order.query.get(order_id)

    @staticmethod
    def delete_order(order_id):
        order = Order.query.get(order_id)
        if order:
            db.session.delete(order)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_orders_by_user_id(user_id):
        return Order.query.filter_by(user_id=user_id).all()
