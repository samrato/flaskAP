from flask import Flask,jsonify,Blueprint,request

user_Bp=Blueprint("user",__name__,url_prefix="/user/juma")

@user_Bp.route("/")
def list_user():
    return jsonify({
        "name":"kamau",
        "age":"16"
    })