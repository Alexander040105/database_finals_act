from flask import Blueprint, render_template, request, flash, redirect, session, url_for
#importing the tables uli for hereee
from models import Department, WebsiteUsers, Employee, EmployeeLeave
from db import db
from datetime import datetime #timestamp


#employee__leave blueprint
employee_leave = Blueprint("employee_leave", __name__, static_folder="static", template_folder="templates")

@employee_leave.route('/request_leave', methods=['GET', 'POST'])
def request_leave():
    if request.method == 'POST':

        #user must be logged in bago mag file ng leave
        employee_id = session.get('employee_id')
        if not employee_id:
            flash("You must be logged in to request leave", category="error")
            return redirect(request.url)

        leave_type = request.form.get('leave_type')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        leave_reason = request.form.get('leave_reason')

        if not all([leave_type, start_date, end_date, leave_reason]):
            flash("Please fill in all fields", category="error")
            print("Please fill in all fields", "error")
            return redirect(request.url)
        
        #leave request
        new_leave = EmployeeLeave(
            employee_id = employee_id,
            leave_type = leave_type,
            start_date = start_date,
            end_date = end_date,
            date_filed = datetime.now().date(),
            leave_reason = leave_reason,
            leave_status = "Pending",
            approved_by = None,
        )

        db.session.add(new_leave)
        db.session.commit()
        flash("Leave request submitted successfully", category="success")
        return redirect(request.url)

    return render_template('anong_html_dit.html')



