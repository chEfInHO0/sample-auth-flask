from flask import Blueprint, request, jsonify
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy.exc import IntegrityError
from pydantic import ValidationError
from os import environ

from app.extensions import db
from app.models.users import Users
from app.schemas.users import UserCreate, UserLogin, UserUpdate, UserUpdatePassword
from app.middleware.sqlErrorHandler import SqlErrorHandler

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/", methods=["POST"])
@login_required
def admin():
    if current_user.role != 'admin':
        return jsonify({"message":"Access Denied"}),401
    if not request.get_json():
        return jsonify({"message":"Missing content"}),400
    try:
        data = UserCreate(**request.get_json())
    except ValidationError as e:
        return jsonify({"message": e.errors()})
    data.role = 'admin'
    try:
        user = Users(**data.model_dump())
        db.session.add(user)
        db.session.commit()
    except IntegrityError as e:
        error_details = SqlErrorHandler(e).errors()
        return jsonify(error_details), error_details.get("status_code")

    return jsonify({"message": user.to_dict()}), 201
        