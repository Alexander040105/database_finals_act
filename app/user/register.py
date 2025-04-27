from flask import Blueprint, render_template, request, flash, redirect
#importing the tables uli for hereee
from models import Department, WebsiteUsers, Employee, EmployeeLeave
from db import db
#login blueprint
register = Blueprint("register", __name__, static_folder="static", template_folder="templates")
from werkzeug.security import generate_password_hash, check_password_hash

def if_acc_exists(email):
    user = WebsiteUsers.query.filter_by(email=email).first()
    return user is not None


def create_employee_account(role, first_name, last_name, email, password, phone_number, home_address,
                            employee_position, date_hired, department_id):
    # Set role based on department idefault na lang natin na pag galing sa HR, Admin na agad HASHASFD
    if department_id == 1:
        role = 'Admin'
    else:
        role = 'User'

    # Hash the password
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')        # Create new WebsiteUser
    new_user = WebsiteUsers(
        first_name=first_name,
        last_name=last_name,
        email=email,
        user_password=hashed_password,
        user_role=role,
        department_id=department_id
    )

    try:
        # icocommit na sa db yung new user
        db.session.add(new_user)
        db.session.commit()

        # Create new Employee instance
        new_employee = Employee(
            employee_id=new_user.employee_id,  # Use the generated employee_id
            phone_number=phone_number,
            home_address=home_address,
            date_hired=date_hired,
            employee_position=employee_position,
            department_id=department_id
        )

        # Add and commit the new employee
        db.session.add(new_employee)
        db.session.commit()

        flash('You are now registered')
        print('You are now registered')
        return redirect("/user/login")
    except Exception as e:
        db.session.rollback()
        flash(f'An error occurred: {str(e)}', 'error')
        print(f'An error occurred: {str(e)}', 'error')
        return redirect('/user/register')


#the routeeee that gets the dataaa from the forms ng user_register.html
@register.route("/register", methods=['POST', 'GET'])
@register.route("/", methods=['POST', 'GET'])
def user_register():
    departments = Department.query.all()
    if request.method == 'POST':
        role = None
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        phone_number = request.form['phone_number']
        home_address = request.form['home_address']
        employee_position = request.form['employee_position']
        date_hired = request.form['date_hired']
        department_id = int(request.form['department_id'])

        if not if_acc_exists(email):
            return create_employee_account(role, first_name, last_name, email, password, phone_number, 
                                            home_address, employee_position, date_hired, department_id)
        else:
            flash('An account with this email already exists.', 'error')
            return redirect("/register")
    return render_template("user_register.html", departments=departments)