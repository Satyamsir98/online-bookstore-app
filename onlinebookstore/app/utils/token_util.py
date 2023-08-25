from flask_jwt_extended import create_access_token
 
def generate_token(user):
    """Generate a JWT token with user role information."""
    token_data = {
        "id": user.id,
        "role": user.role,
        "name":user.name,
        "email":user.email
    }
    token = create_access_token(identity=user.id, additional_claims=token_data)
    return token