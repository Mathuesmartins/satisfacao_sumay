from app import app
from models import db, Produto

with app.app_context():
    db.session.add_all([
        Produto(nome="Notebook"),
        Produto(nome="Celular"),
        Produto(nome="Tablet")
    ])
    db.session.commit()
