from flask import Flask, request, render_template, session, redirect, url_for
import re
import random
import time
from app.admin.login import login as admin_login

app = Flask(__name__)
app.register_blueprint(admin_login, url_prefix="/admin")


@app.route("/", methods=['POST', 'GET'])
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
