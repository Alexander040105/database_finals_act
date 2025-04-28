from flask import Blueprint, render_template, request, flash, redirect
#importing the tables uli for hereee
from models import Department, WebsiteUsers, Employee, EmployeeLeave
from db import db
#encryption library thingy
from werkzeug.security import generate_password_hash, check_password_hash


#login blueprint
login = Blueprint("login", __name__, static_folder="static", template_folder="templates")

def verify_login():
    #parameters ng check_password_hash =  hashed_password_from_db, user_input_password
    if check_password_hash():
        # password is correct
        pass
    else:
        # password is wrong
        pass

@login.route("/login", methods=['POST', 'GET'])
@login.route("/", methods=['POST', 'GET'])
def user_login():   
    return render_template("user_login.html")