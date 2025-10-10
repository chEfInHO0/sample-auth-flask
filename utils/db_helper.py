from sqlalchemy.orm import Session
from sqlalchemy import select
from models import db

def commit_session(obj):
    try:
        with Session(db.engine) as session:
            session.add(obj)
            session.commit()
        return True, None
    except Exception as e:
        return False, str(e)

def fetch_all(model, filters=None):
    """
    Executa um SELECT * FROM model com filtros opcionais.
    Retorna uma lista de objetos.
    """
    try:
        with Session(db.engine) as session:
            stmt = select(model)
            if filters:
                stmt = stmt.filter_by(**filters)
            result = session.execute(stmt)
            return result.scalars().all(),None
    except Exception as e:
        return None, str(e)

def fetch_one(model, filters=None):
    """
    Executa um SELECT com filtros e retorna apenas um resultado.
    """
    try:
        with Session(db.engine) as session:
            stmt = select(model)
            if filters:
                stmt = stmt.filter_by(**filters)
            result = session.execute(stmt)
            return result.scalars().first(),None
    except Exception as e:
        return None, str(e)
