from flask import Flask, jsonify
from flask_login import LoginManager
from datetime import timedelta
from dotenv import load_dotenv
from os import environ

from app.extensions import db
from app.models.users import Users
from app.routes.user_routes import user_bp
from app.routes.admin_route import admin_bp

load_dotenv()


def create_app():
    app = Flask(__name__)

    # Configurações
    DURATION = int(environ.get('REMEMBER_COOKIE_DURATION', 7))
    app.config.from_object('app.config.Config')
    app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=DURATION)

    # Inicializações
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.filter_by(user_id=user_id).first()

    @login_manager.unauthorized_handler
    def unauthorized_callback():
        return jsonify({"message": "Authentication required. Please log in first."}), 401

    # Registrar blueprints
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(admin_bp, url_prefix="/admin")    
    
    # Erro global
    @app.errorhandler(405)
    def method_not_allowed(e):
        return jsonify({
            "error": "Method Not Allowed",
            "message": "This endpoint does not accept the requested method."
        }), 405

    return app
