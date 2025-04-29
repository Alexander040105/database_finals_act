from flask import Blueprint, render_template, redirect, session, flash, url_for, make_response
from flask_login import login_required
from models import Department, WebsiteUsers, Employee, EmployeeLeave
import json

user = Blueprint("user", __name__, static_folder="static", template_folder="templates")

def get_leave():
    leave_applications = EmployeeLeave.query.filter_by(employee_id=session['employee_id']).all()

    if leave_applications:
        leave_dicts = [leave.to_dict() for leave in leave_applications]
        session['employee_leave'] = leave_dicts
        print(leave_dicts)
        return leave_dicts
    
    return None

@login_required
@user.route("/user/dashboard/id/<int:user_id>", methods=['POST', 'GET'])
def user_dashboard(user_id):
    if 'user_role' not in session or session['user_role'] != "User":
        flash("Unauthorized access", "error")
        return redirect(url_for("login.user_login"))
    
    #finds user again for the session
    user = WebsiteUsers.query.get(user_id)
    if not user or user.user_role != "User":
        flash("Invalid user account", "error")
        return redirect(url_for("login.user_login"))
    employee_info = Employee.query.filter_by(employee_id=user_id).first()
    if not employee_info:
        flash("No employee info found.", "error")
        return redirect(url_for("login.user_login"))
    
    session['employee_id'] = user_id
    session['user_role'] = user.user_role
    session['user_name'] = f'{user.first_name} {user.last_name}'
    session['department_id'] = user.department_id
    session['phone_number'] = employee_info.phone_number
    session['home_address'] = employee_info.home_address
    session['date_hired'] = employee_info.date_hired
    session['employee_position'] = employee_info.employee_position

    employee_leaves = get_leave()

    #para wala nang data cachee di na mababalikan yung data pag nagsession clearrr
    response = make_response(render_template("user_home.html", username=session['user_name'], employee_leaves=employee_leaves))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    return response


@user.route("/logout", methods=['POST', 'GET'])
@user.route("/", methods=['POST', 'GET'])
def user_logout(): 
    session.clear()
    return redirect(url_for("login.user_login"))
