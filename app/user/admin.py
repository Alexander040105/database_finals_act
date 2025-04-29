# user_admin.py
from flask import Blueprint, render_template, redirect, session, flash, url_for
from flask_login import login_required
from models import Department, WebsiteUsers, Employee, EmployeeLeave

admin = Blueprint("admin", __name__, static_folder="static", template_folder="templates")

    

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

    return render_template("admin_home.html", username=session['user_name'])
