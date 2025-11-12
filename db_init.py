from app.extensions import db
from app import create_app
from app.models.users import Users

app = create_app()

with app.app_context():
    db.create_all()
