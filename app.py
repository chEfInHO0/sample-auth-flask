
from flask import Flask, request, jsonify
from database import db
from models.users import Users
from schemas.users import UserCreate
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError
from middleware.sqlErrorHandler import SqlErrorHandler


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "your_secret_key"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

    db.init_app(app)

    @app.route("/user", methods=["GET"])
    def get_user():
        users = Users.query.all()
        return jsonify({"users":[u.to_dict() for u in users]})

    @app.route('/user', methods=['POST'])
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
            return jsonify(error_details),error_details.get("status_code")
        return jsonify({"message": user.to_dict()}), 201
    return app


if __name__ == '__main__':
    app = create_app()

    app.run(debug=True, port=3333)
