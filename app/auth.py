from flask import Flask ,request,jsonify,Blueprint

auth_Bp=Blueprint("auth",__name__,url_prefix="getauth")
