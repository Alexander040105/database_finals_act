from flask import Blueprint, render_template, request, flash, redirect, session, url_for
#importing the tables uli for hereee
from models import Department, WebsiteUsers, Employee, EmployeeLeave
from db import db
#encryption library thingy
from werkzeug.security import generate_password_hash, check_password_hash


#login blueprint
profile = Blueprint("profile", __name__, static_folder="static", template_folder="templates")

@profile.route('/employee/<int:employee_id>', methods=['GET'])

#fetch from database
def get_employee_details(employee_id):

    #find user record
    user = WebsiteUsers.query.filter_by(employee_id=employee_id).first()

    if not user:
        return {"error": "User not found"}, 404
    
    #get employee record linked to the user
    employee = Employee.query.filter_by(employee_id=employee_id).first()

    

    employee_details = {
        "employee_id": user.employee_id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "phone_number": employee.phone_number if employee else None,
        "home address": employee.home_address if employee else None,
        "date_hired": employee.date_hired.strftime("%Y-%m-%d") if employee and employee.date_hired else None,
        "employee_position": employee.employee_position if employee else None,
        "department_id": employee.department_id if employee else None,
    }
        
    return render_template("to_do.html", employee_details=employee_details)