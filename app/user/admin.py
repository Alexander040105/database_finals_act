# user_admin.py
from flask import Blueprint, render_template


admin = Blueprint("admin", __name__, static_folder="static", template_folder="templates")

@admin.route("/admin", methods=['POST', 'GET'])
def user_admin():
    return "Admin Test"
