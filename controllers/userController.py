from flask import jsonify
from sqlalchemy.orm import Session
from models import db, User
from utils.db_helper import commit_session, fetch_all

class userController:
    def create(self,**kwargs):
        valid_cols = {cols.name for cols in User.__table__.columns}
        filtered = {key:value for key,value in kwargs.items() if key in valid_cols}
        user = User(**filtered)
        success,error = commit_session(user)
        if success:
            return jsonify({"message":"User added to database"}),201
        else:
            return jsonify({"message":error}),400
    def read(self):
        users, error = fetch_all(User)
        if error:
            return jsonify({"error": error}), 400

        return jsonify([{
            "id": u.id,
            "name": u.name,
            "email": u.email,
            "is_adm": u.is_adm
        } for u in users]), 200
    def update(self):
        pass
    def update_(self):
        pass
    def delete(self):
        pass