from flask import Flask ,request,jsonify,Blueprint
from .import db,bcrypt
from.models import User



auth_Bp=Blueprint("auth",__name__,url_prefix="getauth")
