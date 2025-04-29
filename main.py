from flask import Flask, request, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import re
import random
import time
import mysql.connector
from app.user.login import login as user_login
from app.user.register import register as user_register
from app.user.admin import admin
from db import db

#importing the tables from the models.py na 1:1 with our mysql database
from models import Department, WebsiteUsers, Employee, EmployeeLeave


app = Flask(__name__)
app.register_blueprint(user_login, url_prefix="/user/login")
app.register_blueprint(user_register, url_prefix="/user/register")
app.register_blueprint(admin, url_prefix="/user/admin")

#trying out sqlalchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# format pls change the password based sa mysql nyo app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:passowrd@localhost/human_resources_db'
#use the mysql_scripts na nasa folder sa workbench, para magamit nyo yung db na nilagay ko here sa app.config hihi:?
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Jade_040105_092004_Aki@localhost/human_resources_db'
app.config['SECRET_KEY'] = 'secret_key'
# db = SQLAlchemy(app)
db.init_app(app)

# draft boolean logic lang just to try out the login and register URL routes
user_logged_in = False
@app.route("/", methods=['POST', 'GET'])
def default():
    if user_logged_in == False:
        return redirect("/user/login")
    else:
        return redirect("/user/register")

if __name__ == "__main__":
    app.run(debug=True)
