from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30), unique=True)
    is_adm: Mapped[bool] = mapped_column(Boolean(), default=False)

    def __repr__(self):
        return f"User {self.id} - {self.name}"
