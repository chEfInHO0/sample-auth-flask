
from flask import Flask
from models import db, User


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "your_secret_key"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

    db.init_app(app)

    @app.route("/", methods=["GET"])
    def home():
        user_count = db.session.execute(db.select(User)).scalars().all()
        return f"Home. Total de usuários no DB: {len(user_count)}"

    return app


if __name__ == '__main__':
    app = create_app()

    with app.app_context():
        db.create_all()

    app.run(debug=True)
