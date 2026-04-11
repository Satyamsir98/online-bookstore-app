from app.extensions import db
from app.models import User, Book, Order, Review, Cart
from datetime import date

def seed_database(app):
    with app.app_context():

        # 👇 IMPORTANT: check if already seeded
        if User.query.first():
            print("Data already exists, skipping seeding...")
            return

        # ---------------- USERS ----------------
        bookstore_owner1 = User(
            name="Owner One",
            email="owner1@bookstore.com",
            phone_number="1234567890",
            password="password123",
            role="Bookstore Owner"
        )

        bookstore_owner2 = User(
            name="Owner Two",
            email="owner2@bookstore.com",
            phone_number="0987654321",
            password="password123",
            role="Bookstore Owner"
        )

        customer1 = User(
            name="Customer One",
            email="customer1@customer.com",
            phone_number="1112233445",
            password="customer123",
            role="Customer"
        )

        customer2 = User(
            name="Customer Two",
            email="customer2@customer.com",
            phone_number="2233445566",
            password="customer123",
            role="Customer"
        )

        admin = User(
            name="Admin User",
            email="admin@admin.com",
            password="admin123",
            role="Admin"
        )

        db.session.add_all([bookstore_owner1, bookstore_owner2, customer1, customer2, admin])
        db.session.commit()

        # ---------------- BOOKS ----------------
        book1 = Book(title="Book One by Owner One", author="Author One", genre="Fiction",
                     price=19.99, publication_date=date(2025, 1, 1), bookstore_id=bookstore_owner1.id)

        book2 = Book(title="Book Two by Owner One", author="Author Two", genre="Non-Fiction",
                     price=29.99, publication_date=date(2025, 1, 1), bookstore_id=bookstore_owner1.id)

        book3 = Book(title="Book Three by Owner One", author="Author Three", genre="Fantasy",
                     price=39.99, publication_date=date(2025, 1, 1), bookstore_id=bookstore_owner1.id)

        book4 = Book(title="Book One by Owner Two", author="Author Four", genre="Sci-Fi",
                     price=25.99, publication_date=date(2025, 1, 1), bookstore_id=bookstore_owner2.id)

        book5 = Book(title="Book Two by Owner Two", author="Author Five", genre="Romance",
                     price=15.99, publication_date=date(2025, 1, 1), bookstore_id=bookstore_owner2.id)

        book6 = Book(title="Book Three by Owner Two", author="Author Six", genre="Thriller",
                     price=17.99, publication_date=date(2025, 1, 1), bookstore_id=bookstore_owner2.id)

        db.session.add_all([book1, book2, book3, book4, book5, book6])
        db.session.commit()

        # ---------------- ORDERS ----------------
        order1 = Order(user_id=customer1.id, book_id=book1.id, order_status="Placed")
        order2 = Order(user_id=customer1.id, book_id=book4.id, order_status="Shipped")
        order3 = Order(user_id=customer2.id, book_id=book2.id, order_status="Delivered")
        order4 = Order(user_id=customer2.id, book_id=book5.id, order_status="Preparing")

        db.session.add_all([order1, order2, order3, order4])
        db.session.commit()

        # ---------------- REVIEWS ----------------
        review1 = Review(user_id=customer1.id, book_id=book1.id, rating=5,
                         review_text="Great book, highly recommend!")
        review2 = Review(user_id=customer1.id, book_id=book4.id, rating=4,
                         review_text="Very interesting, would buy again.")
        review3 = Review(user_id=customer2.id, book_id=book2.id, rating=3,
                         review_text="It was okay.")
        review4 = Review(user_id=customer2.id, book_id=book5.id, rating=4,
                         review_text="Good book.")

        db.session.add_all([review1, review2, review3, review4])
        db.session.commit()

        # ---------------- CART ----------------
        cart_item1 = Cart(user_id=customer1.id, book_id=book1.id, quantity=1)
        cart_item2 = Cart(user_id=customer1.id, book_id=book2.id, quantity=2)

        cart_item3 = Cart(user_id=customer2.id, book_id=book4.id, quantity=1)
        cart_item4 = Cart(user_id=customer2.id, book_id=book5.id, quantity=1)

        db.session.add_all([cart_item1, cart_item2, cart_item3, cart_item4])
        db.session.commit()

        print("✅ Database seeded successfully!")








# from app.extensions import app, db
# from app.models import User, Book, Order, Review, Cart
# from datetime import date

# # # Initialize Flask app and database
# # app = create_app()

# def seed_database(app):
#     with app.app_context():
#         if User.query.first():
#             print("Data already exists, skipping seeding...")
#             return
#         # # Delete existing data from all tables before seeding
#         # db.session.query(Cart).delete()
#         # db.session.query(Review).delete()
#         # db.session.query(Order).delete()
#         # db.session.query(Book).delete()
#         # db.session.query(User).delete()  # Updated to delete from the single 'users' table

#         # Commit to apply deletions
#         db.session.commit()

#         # Seed Users 
#         bookstore_owner1 = User(
#             name="Owner One",
#             email="owner1@bookstore.com",
#             phone_number="1234567890",
#             password="password123",  # No password hashing for now
#             role="Bookstore Owner"
#         )

#         bookstore_owner2 = User(
#             name="Owner Two",
#             email="owner2@bookstore.com",
#             phone_number="0987654321",
#             password="password123",  
#             role="Bookstore Owner"
#         )

#         # Seed Customers (No password hashing)
#         customer1 = User(
#             name="Customer One",
#             email="customer1@customer.com",
#             phone_number="1112233445",
#             password="customer123", 
#             role="Customer"
#         )

#         customer2 = User(
#             name="Customer Two",
#             email="customer2@customer.com",
#             phone_number="2233445566",
#             password="customer123", 
#             role="Customer"
#         )

#         # Seed Admin (No password hashing)
#         admin = User(
#             name="Admin User",
#             email="admin@admin.com",
#             password="admin123",  
#             role="Admin"
#         )

#         # Add all users to the database
#         db.session.add_all([bookstore_owner1, bookstore_owner2, customer1, customer2, admin])
#         db.session.commit()

#         # Seed Books for each Bookstore Owner
#         book1 = Book(
#             title="Book One by Owner One",
#             author="Author One",
#             genre="Fiction",
#             price=19.99,
#             publication_date=date(2025, 1, 1),
#             bookstore_id=bookstore_owner1.id
#         )

#         book2 = Book(
#             title="Book Two by Owner One",
#             author="Author Two",
#             genre="Non-Fiction",
#             price=29.99,
#             publication_date=date(2025, 1, 1),
#             bookstore_id=bookstore_owner1.id
#         )

#         book3 = Book(
#             title="Book Three by Owner One",
#             author="Author Three",
#             genre="Fantasy",
#             price=39.99,
#             publication_date=date(2025, 1, 1),
#             bookstore_id=bookstore_owner1.id
#         )

#         book4 = Book(
#             title="Book One by Owner Two",
#             author="Author Four",
#             genre="Sci-Fi",
#             price=25.99,
#             publication_date=date(2025, 1, 1),
#             bookstore_id=bookstore_owner2.id
#         )

#         book5 = Book(
#             title="Book Two by Owner Two",
#             author="Author Five",
#             genre="Romance",
#             price=15.99,
#             publication_date=date(2025, 1, 1),
#             bookstore_id=bookstore_owner2.id
#         )

#         book6 = Book(
#             title="Book Three by Owner Two",
#             author="Author Six",
#             genre="Thriller",
#             price=17.99,
#             publication_date=date(2025, 1, 1),
#             bookstore_id=bookstore_owner2.id
#         )

#         # Add books to the database
#         db.session.add_all([book1, book2, book3, book4, book5, book6])
#         db.session.commit()

#         # Seed Orders for each Customer
#         order1 = Order(user_id=customer1.id, book_id=book1.id, order_status="Placed")
#         order2 = Order(user_id=customer1.id, book_id=book4.id, order_status="Shipped")
#         order3 = Order(user_id=customer2.id, book_id=book2.id, order_status="Delivered")
#         order4 = Order(user_id=customer2.id, book_id=book5.id, order_status="Preparing")

#         # Add orders to the database
#         db.session.add_all([order1, order2, order3, order4])
#         db.session.commit()

#         # Seed Reviews for each Customer
#         review1 = Review(user_id=customer1.id, book_id=book1.id, rating=5, review_text="Great book, highly recommend!")
#         review2 = Review(user_id=customer1.id, book_id=book4.id, rating=4, review_text="Very interesting, would buy again.")
#         review3 = Review(user_id=customer2.id, book_id=book2.id, rating=3, review_text="It was okay, not bad but not amazing.")
#         review4 = Review(user_id=customer2.id, book_id=book5.id, rating=4, review_text="Good book for fans of the genre.")

#         # Add reviews to the database
#         db.session.add_all([review1, review2, review3, review4])
#         db.session.commit()

#         # Add Books to the Cart for Customer1
#         cart_item1 = Cart(user_id=customer1.id, book_id=book1.id, quantity=1)
#         cart_item2 = Cart(user_id=customer1.id, book_id=book2.id, quantity=2)  # Customer adds 2 copies of book2

#         # Add books to customer1's cart
#         db.session.add_all([cart_item1, cart_item2])
#         db.session.commit()

#         # Add Books to the Cart for Customer2
#         cart_item3 = Cart(user_id=customer2.id, book_id=book4.id, quantity=1)
#         cart_item4 = Cart(user_id=customer2.id, book_id=book5.id, quantity=1)

#         # Add books to customer2's cart
#         db.session.add_all([cart_item3, cart_item4])
#         db.session.commit()

#         print("Database seeded successfully!")

# # Run the seeder script
# if __name__ == "__main__":
#     seed_database()
