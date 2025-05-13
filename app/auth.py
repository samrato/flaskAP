from flask import Flask ,request,jsonify,Blueprint
from .import db,bcrypt
from.models import User
from flask_jwt_extended import create_access_token,jwt_required,get_jwt_identity


auth_Bp=Blueprint("auth",__name__,url_prefix="getauth")
