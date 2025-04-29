# user_admin.py
from flask import Blueprint, render_template, redirect, session, flash, url_for, make_response, request
from flask_login import login_required
from models import Department, WebsiteUsers, Employee, EmployeeLeave
import json
from db import db

admin = Blueprint("admin", __name__, static_folder="static", template_folder="templates")

def get_leave():
    leave_applications = EmployeeLeave.query.filter_by(employee_id=session['employee_id']).all()

    if leave_applications:
        leave_dicts = [leave.to_dict() for leave in leave_applications]
        session['employee_leave'] = leave_dicts
        return leave_dicts
    
    return None


def check_applications():
    leave_applications = EmployeeLeave.query.all()
    if leave_applications:
        company_leave_dicts = [leave.to_dict() for leave in leave_applications]
        return company_leave_dicts
    return None

@login_required
@admin.route("/admin/dashboard/id/<int:user_id>", methods=['POST', 'GET'])
def user_admin_dashboard(user_id):
    if 'user_role' not in session or session['user_role'] != "Admin":
        flash("Unauthorized access", "error")
        return redirect(url_for("login.user_login"))
    
    #finds user again for the session
    user = WebsiteUsers.query.get(user_id)
    if not user or user.user_role != "Admin":
        flash("Invalid admin account", "error")
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
    response = make_response(render_template("admin_home.html", username=session['user_name'], employee_leaves=employee_leaves))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    return response


@admin.route("/logout", methods=['POST', 'GET'])
@admin.route("/", methods=['POST', 'GET'])
def user_logout(): 
    session.clear()
    return redirect(url_for("login.user_login"))


@login_required
@admin.route("/admin/dashboard/applications/id/<int:user_id>", methods=['POST', 'GET'])
def user_admin_approval(user_id):
    if 'user_role' not in session or session['user_role'] != "Admin":
        flash("Unauthorized access", "error")
        return redirect(url_for("login.user_login"))
    
    leave_responses = ['Pending','Approve', 'Reject']
    company_leave_applications = check_applications()

    if request.method == 'POST':
        statuses = request.form.getlist('leave_statuses')
        leave_ids = request.form.getlist('leave_ids')
        approver = session['employee_id']

        for leave_id, new_status in zip(leave_ids, statuses):
            leave = EmployeeLeave.query.get(int(leave_id))
            if leave:
                leave.leave_status = new_status
                leave.approved_by = approver
        
        db.session.commit()
        flash("Leave applications updated successfully.", "success")
    else:
        flash("Leave application not found.", "error")

    response = make_response(render_template("admin_leave_checker.html", username=session['user_name'], company_leave_applications=company_leave_applications, leave_responses=leave_responses))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    return response