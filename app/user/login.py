from flask import Blueprint, render_template, request, flash, redirect, session 
#importing the tables uli for hereee
from models import Department, WebsiteUsers, Employee, EmployeeLeave
from db import db
#encryption library thingy
from werkzeug.security import generate_password_hash, check_password_hash


#login blueprint
login = Blueprint("login", __name__, static_folder="static", template_folder="templates")

def verify_login(hashed_password_from_db, user_input_password):
    #parameters ng check_password_hash =  hashed_password_from_db, user_input_password
    return check_password_hash(hashed_password_from_db, user_input_password)

@login.route("/login", methods=['POST', 'GET'])
@login.route("/", methods=['POST', 'GET'])

def user_login(): 
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not all([email, password]):
            flash("Please fill in all fields", "error")
            return redirect(request.url)

        #finds user
        user = WebsiteUsers.query.filter_by(email=email).first()


        #authentication process
        if user:
            if verify_login(user.password, password):
                flash("Login successful", category="success")
            else:
                flash("Invalid username or password", category="error")
        else:
            flash("Email does not exist", category="error")
    
    session.clear()  
    return render_template("user_login.html", boolean=True)