from flask import Blueprint, request, jsonify
from app import db
from app.models import User
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token

bcrypt = Bcrypt()

# Create a Blueprint for routes
bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
    return "Welcome to CodeBuddy!"


@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Check if the necessary fields are provided
    if not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Missing data'}), 400

    # Hash the password
    password_hash = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    # Create a new user
    new_user = User(username=data['username'], email=data['email'], password_hash=password_hash)

    # Save the user to the database
    db.session.add(new_user)
    try:
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Database error', 'error': str(e)}), 500


@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Find user by email
    user = User.query.filter_by(email=data['email']).first()

    if user and bcrypt.check_password_hash(user.password_hash, data['password']):
        # Create JWT token
        access_token = create_access_token(identity=user.user_id)
        return jsonify({'access_token': access_token}), 200

    return jsonify({'message': 'Invalid credentials'}), 401
