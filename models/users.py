from pathlib import Path
from sqlalchemy import create_engine, String, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


cwd = Path(__file__).parent
# will be stored in a .env file in the future
DB_PATH = f"{cwd}/database.sqlite"


class Base(DeclarativeBase):
    pass


class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))
    is_adm: Mapped[bool] = mapped_column(Boolean(), default=False)

    def __repr__(self):
        return f"User {self.id} - {self.name}"


engine = create_engine(f"sqlite:///{DB_PATH}")
Base.metadata.create_all(bind=engine)
