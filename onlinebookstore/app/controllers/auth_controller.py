from flask import Blueprint, request, jsonify
from app.services.auth_service import AuthService

auth_bp = Blueprint('auth_bp', __name__)
auth_service = AuthService()

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return auth_service.login(data)

# @auth_bp.route('/register', methods=['POST'])
# def register_user():
#     data = request.get_json()
    
#     # Using the role from the data to register as either "Customer" or "Bookstore Owner"
#     if data['role'] not in ['Customer', 'Bookstore Owner']:
#         return jsonify({"message": "Invalid role"}), 400

#     # Assuming you have validation and registration logic for phone number
#     if len(data['phone_number']) != 10 or not data['phone_number'].isdigit():
#         return jsonify({"message": "Invalid phone number"}), 400

#     return auth_service.register_user(data)

@auth_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    # Using the role from the data to register as either "Customer" or "Bookstore Owner"
    if data['role'] not in ['Customer', 'Bookstore Owner', 'Admin']:
        return jsonify({"message": "Invalid role"}), 400
    
    return auth_service.register_user(data)

@auth_bp.route('/users', methods=['GET'])
def get_all_users():
    return auth_service.get_all_users()
