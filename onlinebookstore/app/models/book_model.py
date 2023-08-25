from app.extensions import db

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50))
    price = db.Column(db.Float, nullable=False)
    publication_date = db.Column(db.Date)
    bookstore_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    orders = db.relationship('Order', backref='book', lazy=True)
    reviews = db.relationship('Review', backref='book', lazy=True)
