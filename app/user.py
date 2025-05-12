from flask import Flaskj,jsonify,Blueprint,request

user_Bp=Blueprint("user",__name__)

@user_Bp.route("/")
def list_user():
    return jsonify({
        "name":"kamau",
        "age":"16"
    })