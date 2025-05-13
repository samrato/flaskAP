from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
# instanciate the events in the python after importing 

db=SQLAlchemy()
bcrypt=Bcrypt()
jwt=JWTManager()

def create_app():
    app=Flask(__name__)
    #database cnnections  
    app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    #the secrete key 
    app.config['JWT_SECRET_KEY'] = 'super-secret-key'

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
     #the blue prints in it 
    from.auth import auth_Bp
    from .books import books_bp
    from .user import user_Bp
    
    app.register_blueprint(books_bp)
    app.register_blueprint(user_Bp)
    # create tables 
    with app.app_context():
        from.models import Book,User
        db.create_all()

    return app

