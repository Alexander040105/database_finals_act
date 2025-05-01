from flask import Blueprint, render_template, request, flash, redirect, session, url_for
#importing the tables uli for hereee
from models import Department, WebsiteUsers, Employee, EmployeeLeave
from db import db
#encryption library thingy
from werkzeug.security import generate_password_hash, check_password_hash


#login blueprint
profile = Blueprint("profile", __name__, static_folder="static", template_folder="templates")
