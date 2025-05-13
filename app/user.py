from flask import Flask,jsonify,Blueprint,request
from.models import User
from.import db
user_Bp=Blueprint("user",__name__,url_prefix="/getuser")

@user_Bp.route("/user" ,methods=['GET'])
def Get_user():
    try:
        user=User.query.all()
        if not user:
            return jsonify({"message":"There is no user availabe"}),422
        return jsonify([u.to_dict() for u in user ])
    except Exception as e:
        return jsonify({"message":"internam server error","details":str(e)})
    
@user_Bp.route("/add",methods=['POST'])
def add_user():
    try:
     data=request.get_json()
     username=data.get('username','').strip()
     email=data.get('email','').strip()
     if not username or not email:
         return jsonify({"message":"all field are required"}),422
     user=User(email=email,username=username)
     db.session.add(user)
     db.session.commit()
     return jsonify(user.to_dict()),201 
    except Exception as e:
        return jsonify({"message":"internal server error","details":str(e)})