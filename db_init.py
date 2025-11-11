from database import db
from app import create_app
from models.users import Users

app = create_app()

with app.app_context():
    db.create_all()
