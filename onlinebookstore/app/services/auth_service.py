from flask import jsonify
from app.extensions import db
from app.models.user_model import User
from app.repositories.user_repository import UserRepository
from app.utils.token_util import generate_token  # Assuming you have a generate_token function

class AuthService:
    def register_user(self, data):
        # Create a new user without password hashing
        user = User(
            name=data['name'],
            email=data['email'],
            phone_number=data.get('phone_number'),
            password=data['password'],  # Consider hashing later for security
            role=data['role']  # Role can be "Customer", "Bookstore Owner", "Admin"
        )
        UserRepository.create_user(user)  # Using the repository method
        return jsonify({"message": f"{user.role} registered successfully!"}), 201

    # def login(self, data):
    #     # Find the user by email (single table lookup)
    #     user = UserRepository.get_user_by_email(data['email'])

    #     # Check the password directly (consider hashing later)
    #     if user and user.password == data['password']:
    #         # Generate token containing user details
    #         access_token = generate_token({
    #             "id": user.id,
    #             "name": user.name,
    #             "email": user.email,
    #             "role": user.role
    #         })
    #         return jsonify({"message": "Login successful", "token": access_token}), 200

    #     return jsonify({"message": "Invalid email or password"}), 401
    def login(self, data):
    # Find the user by email (single table lookup)
        user = UserRepository.get_user_by_email(data['email'])

        # Check if the user exists and the password is correct
        if user and user.password == data['password']:
            # Generate token containing user details
            # Pass the 'user' object directly
            access_token = generate_token(user)
            return jsonify({"message": "Login successful", "token": access_token}), 200

        return jsonify({"message": "Invalid email or password"}), 401


    def get_all_users(self):
        users = User.query.all()  # Fetch all users from the User table
        return jsonify([{
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        } for user in users]), 200

