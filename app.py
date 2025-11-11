
from flask import Flask, request, jsonify
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from database import db
from models.users import Users
from schemas.users import UserCreate, UserLogin, UserUpdate, UserUpdatePassword
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError
from middleware.sqlErrorHandler import SqlErrorHandler
from datetime import timedelta
from dotenv import load_dotenv
from os import environ

load_dotenv()


def create_app():
    app = Flask(__name__)
    login_manager = LoginManager()
    DURATION = int(environ.get('REMEMBER_COOKIE_DURATION'))
    app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
        'SQLALCHEMY_DATABASE_URI')
    app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=DURATION)
    app.config.update(
        SESSION_COOKIE_HTTPONLY=environ.get('SESSION_COOKIE_HTTPONLY'),
        SESSION_COOKIE_SECURE=environ.get('SESSION_COOKIE_SECURE'),
        SESSION_COOKIE_SAMESITE=environ.get('SESSION_COOKIE_SAMESITE'),
    )

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.filter_by(user_id=user_id).first()

    @login_manager.unauthorized_handler
    def unauthorized_callback():
        return jsonify({"message": "Authentication required. Please log in first."}), 401

    @app.route('/login', methods=['POST'])
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
        else:
            return jsonify({"message": "User or Password incorrect"}), 404

    @app.route('/logout', methods=["POST"])
    @login_required
    def logout():
        logout_user()
        response = jsonify({"message": "Logout successful"})
        response.set_cookie('session', '', expires=0)
        return response, 200

    @app.route("/user", methods=["GET"])
    def get_user():
        users = Users.query.all()
        return jsonify({"users": [u.to_dict() for u in users]})

    @app.route('/register', methods=['POST'])
    # @login_required
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

    @app.route("/user/<int:user_id>", methods=["PUT"])
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

    @app.route("/user/<int:user_id>/password", methods=["PATCH"])
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

    @app.route("/user/<int:user_id>", methods=['DELETE'])
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

    @app.errorhandler(405)
    def method_not_allowed(e):
        return jsonify({
            "error": "Method Not Allowed",
            "message": "This endpoint does not accept the requested method."
        }), 405

    return app


if __name__ == '__main__':
    app = create_app()

    app.run(debug=True, port=3333)
