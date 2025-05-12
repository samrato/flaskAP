from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def create_app():
    app=Flask(__name__)
    #database cnnections 
    app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    db.init_app(app)

    from .books import books_bp
    from .user import user_Bp
    
    app.register_blueprint(books_bp)
    app.register_blueprint(user_Bp)
    # create tables 
    with app.app_context():
        from.models import Books
        db.create_all()

    return app

