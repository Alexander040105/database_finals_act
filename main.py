from flask import Flask, request, render_template, session, redirect, url_for
import re
import random
import time


app = Flask(__name__)

@app.route("/reset", methods=['POST', 'GET'])
def reset():
    pass


@app.route("/login", methods=['POST', 'GET'])
def login():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
