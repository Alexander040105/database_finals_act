from db import db

#got help from our friendly neighborhood AIs to setup the class nung mga tables HASDHASFDH nakaktamad gawin one by one e
#1:1 na toh with the existing tables na nasa script_draft2.sql file 
class Department(db.Model):
    __tablename__ = 'department'
    department_id = db.Column(db.Integer, primary_key=True, nullable=False)
    department_name = db.Column(db.String(200))
    department_description = db.Column(db.Text)

class WebsiteUsers(db.Model):
    __tablename__ = 'website_users'
    employee_id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)
    user_password = db.Column(db.Text)
    user_role = db.Column(db.String(200))
    department_id = db.Column(db.Integer, db.ForeignKey('department.department_id'))

class Employee(db.Model):
    __tablename__ = 'employee'
    employee_id = db.Column(db.Integer, db.ForeignKey('website_users.employee_id'), primary_key=True)
    phone_number = db.Column(db.BigInteger)
    home_address = db.Column(db.Text)
    date_hired = db.Column(db.Date)
    employee_position = db.Column(db.String(200))
    department_id = db.Column(db.Integer, db.ForeignKey('department.department_id'))

class EmployeeLeave(db.Model):
    __tablename__ = 'employee_leave'
    leave_id = db.Column(db.Integer, primary_key=True, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.employee_id'))
    leave_type = db.Column(db.String(200))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    date_filed = db.Column(db.Date)
    leave_reason = db.Column(db.Text)
    leave_status = db.Column(db.String(200))
    approved_by = db.Column(db.Integer, db.ForeignKey('employee.employee_id'))

    def to_dict(self):
        return {
            "leave_id": self.leave_id,
            "employee_id": self.employee_id,
            "leave_type": self.leave_type,
            "start_date": str(self.start_date),
            "end_date": str(self.end_date),
            "date_filed": str(self.date_filed),
            "status": self.leave_status,
            "leave_reason": self.leave_reason,
            "approved_by": self.approved_by
        }
