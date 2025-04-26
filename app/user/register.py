from flask import Blueprint, render_template

#login blueprint
login = Blueprint("login", __name__, static_folder="static", template_folder="templates")

@login.route("/register", methods=['POST', 'GET'])
@login.route("/", methods=['POST', 'GET'])
def user_register():
    return render_template("user_register.html")