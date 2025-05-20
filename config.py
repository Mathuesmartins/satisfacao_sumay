import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://usuario:senha@localhost/satisfacao_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'seuemail@gmail.com'
    MAIL_PASSWORD = 'suasenha'
