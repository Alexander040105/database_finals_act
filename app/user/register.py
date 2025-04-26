from flask import Blueprint, render_template

#login blueprint
register = Blueprint("register", __name__, static_folder="static", template_folder="templates")

@register.route("/register", methods=['POST', 'GET'])
@register.route("/", methods=['POST', 'GET'])
def user_register():
    return render_template("user_register.html")