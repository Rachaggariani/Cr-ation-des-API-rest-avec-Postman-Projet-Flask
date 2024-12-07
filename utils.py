"""
from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password):
Fonction pour hacher un mot de passe en utilisant werkzeug.
    return generate_password_hash(password)

def verify_password(stored_password, provided_password):
Fonction pour vérifier si le mot de passe fourni correspond au mot de passe stocké.
    return check_password_hash(stored_password, provided_password)
"""

from passlib.context import CryptContext

# Create a context for managing hashing algorithms
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password):
    """Function to hash a password using Passlib."""
    return pwd_context.hash(password)

def verify_password(stored_password, provided_password):
    """Function to verify if the provided password matches the stored password."""
    return pwd_context.verify(provided_password, stored_password)
