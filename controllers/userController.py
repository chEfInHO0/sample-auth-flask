from flask import jsonify
from sqlalchemy.orm import Session
from models import db, User
from utils.db_helper import commit_session

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
        pass
    def update(self):
        pass
    def update_(self):
        pass
    def delete(self):
        pass