from flask import Flask
from app import create_app
from app.extensions import db
from app.controllers import auth_controller, book_controller, order_controller, review_controller, cart_controller
from flask_cors import CORS

# Create Flask app instance
app = create_app()

# Initialize the database (this will create all tables based on the models)
with app.app_context():
    db.create_all()  # This will create all the tables defined by the models

# Register Blueprints (your controllers)
app.register_blueprint(auth_controller.auth_bp, url_prefix='/authbp')
app.register_blueprint(book_controller.book_bp, url_prefix='/bookbp')
app.register_blueprint(order_controller.order_bp, url_prefix='/orderbp')
app.register_blueprint(review_controller.review_bp, url_prefix='/reviewbp')
app.register_blueprint(cart_controller.cart_bp, url_prefix='/cartbp')

# Error Handling: Catch 404 errors
@app.errorhandler(404)
def not_found(error):
    return {"error": "Resource not found", "status_code": 404}, 404

# Error Handling: Catch 500 errors (Internal Server Errors)
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()  # Ensure to rollback any pending transaction in case of error
    return {"error": "Internal server error", "status_code": 500}, 500

def init_extensions(app):
    CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})
  # This allows requests from the Angular frontend

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    # app.run(debug=True)
