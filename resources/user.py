from flask import request
from flask_restful import Resource
from http import HTTPStatus
from utils import hash_password
from models.user import User
from extensions import db 
# Define the "UserListResource" class as a resource
class UserListResource(Resource):
    def get(self, user_id=None):
        if user_id is None:
            return self.get_all_users()  # Récupération de tous les utilisateurs
        else:
            return self.get_user_by_id(user_id)  # Récupération d'un utilisateur par ID

    def get_all_users(self):
        # Récupération de tous les utilisateurs
        users = User.query.all()
        data = [
            {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'password':user.password
            }
            for user in users
        ]
        return data, HTTPStatus.OK

    def get_user_by_id(self, user_id):
        # Récupération de l'utilisateur par ID
        user = User.query.get(user_id)
        if user is None:
            return {'message': 'User not found'}, HTTPStatus.NOT_FOUND
        else:
          data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'password':user.password
                 }
        return data, HTTPStatus.OK
    # Define the "post" method to handle POST requests
    def post(self):
        # Retrieve JSON data from the request
        json_data = request.get_json()

        # Extract 'username' from JSON data
        username = json_data.get('username')
        
        # Extract 'email' from JSON data
        email = json_data.get('email')
        
        # Extract 'password' from JSON data
        non_hash_password = json_data.get('password')

        # Check if a user with the same username already exists
        if User.get_by_username(username):
            return {'message': 'Username already used'}, HTTPStatus.BAD_REQUEST

        # Check if a user with the same email address already exists
        if User.get_by_email(email):
            return {'message': 'Email already used'}, HTTPStatus.BAD_REQUEST

        # Hash the un-hashed password
        password = hash_password(non_hash_password)

        # Create an instance of the "User" class
        user = User(
            username=username,
            email=email,
            password=password
        )

        # Save the user to the database
        user.save()

        # Create a data dictionary
        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }

        # Return data with a "201 Created" status code
        return {
        'message': 'User added successfully',
        'data': data
    }, HTTPStatus.CREATED
    
    def put(self, user_id):
        # Retrieve the user by ID
        user = User.query.get(user_id)
        if user is None:
            return {'message': 'User not found'}, HTTPStatus.NOT_FOUND

        # Get JSON data from the request
        json_data = request.get_json()

        # Update user fields if provided
        username = json_data.get('username')
        email = json_data.get('email')
        non_hash_password = json_data.get('password')
        # Vérifier si 'username' n'est pas nul, donc la valeur sera modifiée par la nouvelle valeur de 'username'
        if username:
            user.username = username
        
        if email:
            # Check if the email is already used by another user
            if User.get_by_email(email) and User.get_by_email(email).id != user.id:
                return {'message': 'email already used'}, HTTPStatus.BAD_REQUEST
            user.email = email

        if non_hash_password:
            user.password = hash_password(non_hash_password)

        # Commit the changes if using SQLAlchemy
        db.session.commit()

        # Create a data dictionary for the updated user
        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }

        # Return the updated user data with status code "200 OK"
        return {
        'message': 'User modified successfully',
        'data': data
    }, HTTPStatus.OK
    """
    def patch(self, user_id):
        # Retrieve the user by ID
        user = User.query.get(user_id)
        if user is None:
            return {'message': 'User not found'}, HTTPStatus.NOT_FOUND

        # Get the JSON data from the request
        json_data = request.get_json()

        # Update fields if they exist in the request data
        if 'username' in json_data:
            user.username = json_data['username']
        
        if 'email' in json_data:
            user.email = json_data['email']
        
        if 'password' in json_data:
            user.password = hash_password(json_data['password'])  # Hash the new password

        # Commit changes to the database
        db.session.commit()

        # Create a response data dictionary
        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }

        # Return the updated user data with a 200 OK status
        return data, HTTPStatus.OK
    """
    
    def delete(self, user_id):
        # Retrieve the user by ID
        user = User.query.get(user_id)
        if user is None:
            return {'message': 'User not found'}, HTTPStatus.NOT_FOUND

        # Delete the user
        user.delete()  # Make sure this method actually removes the user from the database

        # Commit the changes if using SQLAlchemy
        db.session.commit()  # Ensure you have imported 'db' from your extensions

        # Return a confirmation message
        return {'message': 'User deleted successfully'}, HTTPStatus.OK
    
    def patch(self, user_id):
        # Récupération de l'utilisateur par ID
        user = User.query.get(user_id)
        if user is None:
            return {'message': 'User not found'}, HTTPStatus.NOT_FOUND

        json_data = request.get_json()
        if json_data is None:
            return {'message': 'No input data provided'}, HTTPStatus.BAD_REQUEST

        # Mise à jour des champs d'utilisateur si fournis
        if 'username' in json_data:
            user.username = json_data['username']

        if 'email' in json_data:
            user.email = json_data['email']

        if 'password' in json_data:
            user.password = hash_password(json_data['password'])

        try:
            # Sauvegarde des modifications
            db.session.commit()
        except Exception as e:
            # Gérer les erreurs de commit
            db.session.rollback()
            return {'message': 'An error occurred while updating the user: {}'.format(str(e))}, HTTPStatus.INTERNAL_SERVER_ERROR

        # Création d'une réponse avec les données mises à jour
        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }

        return {
        'message': 'User updated successfully',
        'data': data
    }, HTTPStatus.OK