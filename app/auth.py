from flask import Flask ,request,jsonify,Blueprint
from .import db,bcrypt
from.models import User
from flask_jwt_extended import create_access_token,jwt_required,get_jwt_identity

auth_Bp=Blueprint("auth",__name__,url_prefix="/autheticate")

@auth_Bp.route('/register',methods=['POST'])
def register_user():
    try:
        data=request.get_json()
        username = data.get('username', '').strip()
        email = data.get('email', '').strip().lower()
        password = data.get('password', '').strip()  
        if not username or not email or not password:
            return jsonify({"message":"Fill in all field"}),422
        if len(username)<3:
            return jsonify({"message":"User name its too short"}),422
        if len(password)<6:
            return jsonify({"message":"Password should greater than 6 characters"})
        existing_user=User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({"message":"email already exist"}),422
        hashed_password=bcrypt.generate_password_hash(password).decode('utf-8') 
        new_user=User(username=username,email=email,password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        access_token=create_access_token(identity=new_user.userId)
        return jsonify({
            "token":access_token,
             "user":new_user.to_dict()
            # {
            # #     "userId":new_user.id,
            # #     "username":new_user.username,
            # #     "email":new_user.email,
            # #     "password":new_user.password,
            # #     "createdAt":new_user.create_At.isoformat()
            # # }
        }),201
    except Exception as e:
        return jsonify({"message":"Internal server error","details":str(e)})    
    
@auth_Bp('/login',methods=['POST'])
def login_user():
    try:
       data=request.get_json() 
       email=data.get('email','').strip().lower()
       password=data.get('password','').strip()
       if not email or not password:
           return jsonify("mesage":"all fields are required"),422
       user=User.query
    except Exception as e:
        return jsonify({"message":"internal server error","details":str(e)})