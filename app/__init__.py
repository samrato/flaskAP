from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def create_app():
    app=Flask(__name__)

    from .books import books_bp
    from .user import user_Bp
    
    app.register_blueprint(books_bp)
    app.register_blueprint(user_Bp)


    return app
