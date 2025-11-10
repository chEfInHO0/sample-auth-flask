from database import db
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    
    def __repr__(self):
        return f"{self.user_id} - {self.username} - {self.email}"

    def to_dict(self):
        return {
            "user_id":self.user_id,
            "username":self.username,
            "email":self.email
        }
