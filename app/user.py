from flask import Flaskj,jsonify,Blueprint,request

user_Bp=Blueprint("user",__name__,url_prefix="/user")

@user_Bp.route("/")
def list_user():
    return jsonify({
        "name":"kamau",
        "age":"16"
    })