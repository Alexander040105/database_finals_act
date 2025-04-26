-- DROP DATABASE human_resources_db;
-- CREATE DATABASE human_resources_db;
USE human_resources_db;

#table ng users for their website account
CREATE TABLE human_resources_db.website_users(
	employee_id INT PRIMARY KEY NOT NULL,
    first_name VARCHAR(200),
    last_name VARCHAR(200),
    email VARCHAR(200), # wag na magusername HAHAHAAH email na lang din pang login
    user_password TEXT, # prolly encrypted na yung nandito kung gagamit tayo ng flask_bcrypt kaya text datatype na lang para unli characters
    user_role VARCHAR(200), #admin or user
    FOREIGN KEY(department_id) REFERENCES department(department_id)
);

#table ng users for their employee info na ipapakita natin sa dashboard for their accounts and pag naview ng admin
CREATE TABLE human_resources_db.employee(
	FOREIGN KEY(employee_id) REFERENCES website_users(employee_id),
    FOREIGN KEY(first_name) REFERENCES website_users(first_name),
    FOREIGN KEY(last_name) REFERENCES website_users(last_name),
    FOREIGN KEY(email) REFERENCES website_users(email),
    phone_number INT,
    home_address TEXT,
    date_hired DATE,
    employee_position VARCHAR(200),
	FOREIGN KEY(department_id) REFERENCES department(department_id),
	FOREIGN KEY(deparment_name) REFERENCES department(department_name)
);

CREATE TABLE human_resources_db.employee_leave(
	leave_id INT PRIMARY KEY NOT NULL,
    FOREIGN KEY(employee_id) REFERENCES employee(employee_id),
    leave_type VARCHAR(200), # Sick, Emergency, Vacation, etc.
    start_date  DATE,
    end_date DATE, 
    date_filed DATE, 
    leave_reason TEXT, 
    leave_status VARCHAR(200), # pending, approved, rejected
    approved_by INT # ireference na lang sa empployee id
);

CREATE TABLE human_resoures_db.department(
	department_id INT PRIMARY KEY NOT NULL,
    department_name VARCHAR(200),
    department_description TEXT
);
