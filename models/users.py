from database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Users(db.Model, UserMixin):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password_hash = db.Column(db.String(256), nullable=False)  # 🔹 alterado

    def __repr__(self):
        return f"{self.user_id} - {self.username} - {self.email}"

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email
        }

    @property
    def id(self):
        return self.user_id

    @property
    def password(self):
        raise AttributeError("Cannot access this property directly.")

    @password.setter
    def password(self, password_plain):
        self.password_hash = generate_password_hash(password_plain)

    def verify_password(self, password_plain):
        return check_password_hash(self.password_hash, password_plain)
