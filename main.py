from flask import Flask, request, render_template, session, redirect, url_for
import re
import random
import time
from app.user.login import login as user_login

app = Flask(__name__)
app.register_blueprint(user_login, url_prefix="/user")


@app.route("/", methods=['POST', 'GET'])
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
