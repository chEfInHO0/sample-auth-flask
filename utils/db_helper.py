from sqlalchemy.orm import Session
from flask import jsonify
from models import db

def commit_session(obj):
    """
    Adiciona um objeto à sessão e faz o commit de forma segura.
    Retorna True em caso de sucesso, ou uma mensagem de erro.
    """
    try:
        with Session(db.engine) as session:
            session.add(obj)
            session.commit()
        return True, None
    except Exception as e:
        return False, str(e)
