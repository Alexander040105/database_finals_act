DROP DATABASE IF EXISTS human_resources_db;
CREATE DATABASE human_resources_db;
USE human_resources_db;

CREATE TABLE department (
    department_id INT PRIMARY KEY NOT NULL,
    department_name VARCHAR(200),
    department_description TEXT
);

CREATE TABLE website_users (
    employee_id INT PRIMARY KEY NOT NULL,
    first_name VARCHAR(200),
    last_name VARCHAR(200),
    email VARCHAR(200) UNIQUE,
    user_password TEXT,
    user_role VARCHAR(200),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES department(department_id)
);

CREATE TABLE employee (
    employee_id INT PRIMARY KEY,
    phone_number BIGINT,
    home_address TEXT,
    date_hired DATE,
    employee_position VARCHAR(200),
    department_id INT,
    FOREIGN KEY (employee_id) REFERENCES website_users(employee_id),
    FOREIGN KEY (department_id) REFERENCES department(department_id)
);

CREATE TABLE employee_leave (
    leave_id INT PRIMARY KEY NOT NULL,
    employee_id INT,
    leave_type VARCHAR(200),
    start_date DATE,
    end_date DATE,
    date_filed DATE,
    leave_reason TEXT,
    leave_status VARCHAR(200),
    approved_by INT,
    FOREIGN KEY (employee_id) REFERENCES employee(employee_id),
    FOREIGN KEY (approved_by) REFERENCES employee(employee_id)
);