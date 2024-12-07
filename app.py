from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from config.Config import Config 
from extensions import db
from resources.user import UserListResource 
import pymysql

# Install MySQLdb for pymysql compatibility
pymysql.install_as_MySQLdb()
app = Flask(__name__)
# Create a Flask application
def create_app():
    app.config.from_object(Config)  # Load configuration from Config
    print(app.config)  # Print configuration for debugging
    register_extensions(app)
    register_resources(app)
    return app

# Register extensions like SQLAlchemy and Flask-Migrate
def register_extensions(app):
    db.init_app(app)
    Migrate(app, db)

# Register API resources
def register_resources(app):
    api = Api(app)
    api.add_resource(UserListResource, '/users', '/users/<int:user_id>')  # Allow user_id in URL

# Define a simple home route
@app.route('/')

def home():
    return "L'exécution peut se faire avec Postman pour tester les APIs."

# Main entry point to run the app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5003)  # Use debug=True without quotes
