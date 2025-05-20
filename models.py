from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

class Resposta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    atendimento = db.Column(db.Integer, nullable=False)
    tempo = db.Column(db.Integer, nullable=False)
    satisfacao = db.Column(db.Integer, nullable=False)
    observacao = db.Column(db.Text)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
