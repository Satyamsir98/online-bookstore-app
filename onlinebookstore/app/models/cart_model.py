from app.extensions import db

class Cart(db.Model):
    __tablename__ = 'cart'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each cart item
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # User who owns the cart
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)  # Book being added to the cart
    quantity = db.Column(db.Integer, nullable=False, default=1)  # Quantity of the book in the cart

    user = db.relationship('User', backref=db.backref('cart_items', lazy=True))  # Relationship with the User table
    book = db.relationship('Book', backref=db.backref('cart_items', lazy=True))  # Relationship with the Book table

    def __repr__(self):
        return f'<CartItem {self.id} for User {self.user_id}>'
