DROP DATABASE IF EXISTS human_resources_db;
CREATE DATABASE human_resources_db;
USE human_resources_db;

CREATE TABLE department (
    department_id INT PRIMARY KEY NOT NULL,
    department_name VARCHAR(200),
    department_description TEXT
);

CREATE TABLE website_users (
    employee_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(200),
    last_name VARCHAR(200),
    email VARCHAR(200) UNIQUE,
    user_password TEXT,
    user_role VARCHAR(200),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES department(department_id)
);

CREATE TABLE employee (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    phone_number BIGINT,
    home_address TEXT,
    date_hired DATE,
    employee_position VARCHAR(200),
    department_id INT,
    FOREIGN KEY (employee_id) REFERENCES website_users(employee_id),
    FOREIGN KEY (department_id) REFERENCES department(department_id)
);

CREATE TABLE employee_leave (
    leave_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
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


INSERT INTO department (department_id, department_name, department_description) VALUES
(1, 'Human Resources', 'Handles recruitment, employee relations, and company policies.'),
(2, 'Finance', 'Manages company budgeting, accounting, and payroll.'),
(3, 'Information Technology', 'Maintains technical infrastructure, software development, and cybersecurity.'),
(4, 'Marketing', 'Promotes the company through advertising, campaigns, and public relations.'),
(5, 'Sales', 'Focuses on customer acquisition, client relationships, and revenue generation.'),
(6, 'Operations', 'Oversees daily activities and ensures smooth business processes.'),
(7, 'Customer Service', 'Handles client inquiries, complaints, and support services.'),
(8, 'Legal', 'Manages contracts, company compliance, and legal matters.'),
(9, 'Research and Development', 'Innovates and develops new products and services.'),
(10, 'Administration', 'Provides general support services, office management, and supplies.');
