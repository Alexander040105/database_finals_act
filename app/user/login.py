from flask import Blueprint, render_template

#login blueprint
login = Blueprint("login", __name__, static_folder="static", template_folder="templates")

@login.route("/login", methods=['POST', 'GET'])
@login.route("/", methods=['POST', 'GET'])
def user_login():
    return render_template("user_login.html")