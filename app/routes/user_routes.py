from flask import Blueprint, request, jsonify
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy.exc import IntegrityError
from pydantic import ValidationError
from os import environ

from app.extensions import db
from app.models.users import Users
from app.schemas.users import UserCreate, UserLogin, UserUpdate, UserUpdatePassword
from app.middleware.sqlErrorHandler import SqlErrorHandler

user_bp = Blueprint("user", __name__)


@user_bp.route("/login", methods=["POST"])
def login():
    if current_user.is_authenticated:
        return jsonify({"message": "User already logged in"}), 401
    if not request.get_json():
        return jsonify({"message": "Missing content"}), 400

    try:
        data = UserLogin(**request.get_json())
    except ValidationError as e:
        return jsonify({"message": e.errors()}), 400

    user = Users.query.filter_by(email=data.email).first()
    
    if user and user.verify_password(data.password):
        login_user(user, remember=environ.get("REMEMBER_USER"))
        return jsonify({"message": "Login Successful"})
    return jsonify({"message": "User or Password incorrect"}), 404


@user_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    response = jsonify({"message": "Logout successful"})
    response.set_cookie("session", "", expires=0)
    return response, 200


@user_bp.route("/", methods=["GET"])
@login_required
def get_users():
    if current_user.role != 'admin':
        return jsonify({"message":"This feature is admin only"}),401
    users = Users.query.all()
    return jsonify({"users": [u.to_dict() for u in users]})

@user_bp.route("/<int:user_id>", methods=["GET"])
@login_required
def get_one_user(user_id):
    if current_user.role != 'admin':
        return jsonify({"message":"This feature is admin only"}),401
    user = Users.query.filter_by(user_id=user_id).first()
    if user:
        return jsonify({"user":user.to_dict()})
    return jsonify({"message":"User not found"}),404

@user_bp.route("/", methods=["POST"])
@login_required
def deprecated_user_post():
    return jsonify({"message": "Use /user/register instead"}), 301

@user_bp.route("/register", methods=["POST"])
def post_user():
    if not request.get_json():
        return jsonify({"message": "Content missing"}), 400
    try:
        data = UserCreate(**request.get_json())
    except ValidationError as e:
        return jsonify({"message": e.errors()}), 400

    try:
        user = Users(**data.model_dump())
        db.session.add(user)
        db.session.commit()
    except IntegrityError as e:
        error_details = SqlErrorHandler(e).errors()
        return jsonify(error_details), error_details.get("status_code")

    return jsonify({"message": user.to_dict()}), 201


@user_bp.route("/<int:user_id>", methods=["PUT"])
@login_required
def put_user(user_id):
    if current_user.id != user_id:
        return jsonify({"message": "Forbidden"}), 403
    try:
        data = UserUpdate(**request.get_json())
    except ValidationError as e:
        return jsonify({"message": e.errors()}), 400

    user = Users.query.filter_by(user_id=user_id).first()
    if not user:
        return jsonify({"message": "User not found"}), 404

    try:
        user.username = data.username
        user.email = data.email
        user.password = data.password
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        error_details = SqlErrorHandler(e).errors()
        return jsonify(error_details), error_details.get("status_code")

    return jsonify({"message": "User updated successfully", "user": user.to_dict()}), 200


@user_bp.route("/<int:user_id>/password", methods=["PATCH"])
@login_required
def patch_user_password(user_id):
    if current_user.id != user_id:
        return jsonify({"message": "Forbidden"}), 403

    try:
        data = UserUpdatePassword(**request.get_json())
    except ValidationError as e:
        return jsonify({"message": e.errors()}), 400

    user = Users.query.filter_by(user_id=user_id).first()
    if not user:
        return jsonify({"message": "User not found"}), 404

    user.password = data.password
    db.session.commit()

    return jsonify({"message": "Password updated successfully"}), 200


@user_bp.route("/<int:user_id>", methods=["DELETE"])
@login_required
def delete_user(user_id):
    if current_user.id != user_id:
        return jsonify({"message": "You are not authorized to modify this account."}), 403
    user = Users.query.filter_by(user_id=user_id).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return "", 204
    return jsonify({"message": "User not found"}), 404
