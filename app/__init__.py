from flask import Flask,jsonify
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
    app.config['JWT_SECRET_KEY'] = '23456789 am tired with u like damn cant generate '

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)



    # Custom JWT error handlers token inasumbua damn am tired 
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
              return jsonify({"msg": "Invalid token", "error": error}), 401
    @jwt.unauthorized_loader
    def missing_token_callback(error):
            return jsonify({"msg": "Missing Authorization Header", "error": error}), 401
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
          return jsonify({"msg": "Token expired"}), 401

     #the blue prints in it 
    from.auth import auth_Bp
    from .books import books_bp
    from .user import user_Bp
    
    app.register_blueprint(books_bp)
    app.register_blueprint(user_Bp)
    app.register_blueprint(auth_Bp)
    # create tables 
    with app.app_context():
        from.models import Book,User
       
        db.create_all()

    return app

