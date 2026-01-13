# Human Resources Management System

A comprehensive web-based Human Resources Management System built with Flask and MySQL, designed to streamline employee management, leave requests, and administrative operations.

---

## Project Background

This Human Resources Management System is a full-stack web application developed to support organizational HR operations. The system is built for companies of any size that need to efficiently manage employee information, track leave requests, and maintain centralized HR records.

**Key Features:**

- **Employee Management:** Centralized employee database with personal and professional information
- **Leave Management:** Streamlined leave request submission and approval workflow
- **Admin Dashboard:** Administrative tools for monitoring and managing employee data
- **User Authentication:** Secure login and registration system with encrypted passwords
- **Department Organization:** Organizational structure with department-based categorization

---

## Data Structure & Initial Checks

The application's database consists of four main tables with the following structure:

### Database Tables:

- **Department:** Stores department information including department ID, name, and description

  - `department_id` (Primary Key)
  - `department_name`
  - `department_description`
- **WebsiteUsers:** Contains user authentication and basic employee information

  - `employee_id` (Primary Key)
  - `first_name`, `last_name`
  - `email` (Unique)
  - `user_password` (Hashed)
  - `user_role` (Admin/Employee)
  - `department_id` (Foreign Key)
- **Employee:** Extended employee details linked to WebsiteUsers

  - `employee_id` (Foreign Key to WebsiteUsers)
  - `phone_number`
  - `home_address`
  - `date_hired`
  - `employee_position`
  - `department_id` (Foreign Key)
- **EmployeeLeave:** Records all leave requests and approvals

  - `leave_id` (Primary Key)
  - `employee_id` (Foreign Key)
  - `leave_type` (Sick, Vacation, Paternity, Maternity, Emergency, Bereavement, Birthday)
  - `start_date`, `end_date`
  - `date_filed`
  - `leave_reason`
  - `leave_status` (Pending/Approved/Rejected)
  - `approved_by` (Employee ID of approver)

**Entity Relationship:** The system maintains referential integrity through foreign keys, with WebsiteUsers as the central table linking to Department and Employee tables, and EmployeeLeave referencing Employee information.

---

## Technology Stack

**Backend:**

- Flask (Python web framework)
- Flask-SQLAlchemy (ORM)
- Flask-Login (Authentication)
- Flask-WTF & WTForms (Form handling)
- Flask-Bcrypt (Password encryption)
- Werkzeug (Security utilities)

**Database:**

- MySQL with PyMySQL connector

**Frontend:**

- HTML/CSS templates
- Responsive web design

**Additional Libraries:**

- Python-dotenv (Environment variables)
- Gunicorn (Production server)

---

## Installation & Setup

### Prerequisites

- Python 3.7+
- MySQL Server
- pip (Python package manager)

### Steps

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd database_finals_act2
   ```
2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
4. **Setup the database:**

   - Create a MySQL database named `human_resources_db`
   - Run the SQL scripts in the `sql_scripts/` folder to initialize tables:
     ```bash
     mysql -u root -p human_resources_db < sql_scripts/script_draft2.sql
     ```
5. **Configure database connection:**

   - Update the database URI in `main.py` with your MySQL credentials:
     ```python
     app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:yourpassword@localhost/human_resources_db'
     ```
6. **Run the application:**

   ```bash
   python main.py
   ```

   The application will be available at `http://localhost:5000`

---

## Features & Functionality

### User Authentication

- **Login:** Secure login with email and password
- **Registration:** New user registration with validation
- **Role-based Access:** Different permissions for Admin and Employee roles

### Employee Dashboard

- View personal profile and information
- Apply for leave with detailed forms
- Track leave request status
- View approved and pending leave requests

### Admin Dashboard

- Monitor all employees and their information
- Review and approve/reject leave requests
- View department-wise employee distribution
- Manage user roles and permissions

### Leave Management

**Supported Leave Types:**

- Sick Leave
- Vacation Leave
- Paternity Leave
- Maternity Leave
- Emergency Leave
- Bereavement Leave
- Birthday Leave

**Leave Workflow:**

1. Employee submits leave request with dates and reason
2. Admin reviews the request
3. Admin approves or rejects the request
4. Employee receives notification of status

### Profile Management

- View and edit personal information
- Update contact details
- View employment history

---

## Project Structure

```
database_finals_act2/
├── main.py                    # Main Flask application entry point
├── db.py                      # Database initialization
├── models.py                  # SQLAlchemy ORM models
├── requirements.txt           # Project dependencies
├── README.md                  # This file
├── app/
│   └── user/
│       ├── login.py           # Login functionality
│       ├── register.py        # Registration functionality
│       ├── admin.py           # Admin dashboard routes
│       ├── user.py            # Employee routes
│       ├── leave.py           # Leave management routes
│       └── profile.py         # Profile management routes
├── templates/
│   ├── user_login.html        # Login page
│   ├── user_register.html     # Registration page
│   ├── user_home.html         # Employee dashboard
│   ├── admin_home.html        # Admin dashboard
│   ├── leave_application.html # Leave request form
│   ├── admin_leave_checker.html # Leave approval interface
│   └── employee_profile.html  # Profile page
├── static/
│   └── css/
│       └── main.css           # Stylesheet
├── sql_scripts/
│   ├── script_draft.sql       # Database schema (draft)
│   └── script_draft2.sql      # Database schema (final)
└── __pycache__/               # Python cache files
```

---

## Key Routes

### Authentication

- `GET/POST /user/login/` - User login
- `GET/POST /user/register/` - User registration

### Employee Routes

- `GET /user/home/<user_role>/id/<user_id>` - Employee dashboard
- `GET/POST /user/<user_role>/request_leave/id/<user_id>` - Request leave
- `GET /user/profile/<user_role>/id/<user_id>` - View profile

### Admin Routes

- `GET /user/admin/<user_role>/id/<user_id>` - Admin dashboard
- `GET /user/admin/leave_checker/<user_role>/id/<user_id>` - Review leave requests
- `POST /user/admin/approve_leave/<leave_id>` - Approve leave
- `POST /user/admin/reject_leave/<leave_id>` - Reject leave

---

## Security Features

- **Password Encryption:** All passwords are hashed using Werkzeug's security utilities (bcrypt)
- **Session Management:** Secure session handling with Flask-Login
- **Input Validation:** Form validation using WTForms and custom validators
- **Email Validation:** Email-validator for valid email addresses
- **SQL Injection Protection:** SQLAlchemy ORM prevents SQL injection attacks

---

## Future Enhancements

- Email notifications for leave approval/rejection
- Advanced reporting and analytics
- Mobile-responsive interface improvements
- Integration with HR metrics and KPIs
- Multi-language support
- API endpoints for third-party integrations
- Automated leave balance calculations
- Document upload for leave requests

---

## Assumptions & Caveats

- The system assumes a single organization with multiple departments
- All dates are stored in YYYY-MM-DD format
- Employee ID is unique and serves as the primary identifier across all systems
- Leave requests require manager approval before being finalized
- The system operates on a fiscal or calendar year basis for leave balance tracking
- Password reset functionality is not yet implemented (future enhancement)
- Email notifications are pending implementation

---

## Troubleshooting

**Database Connection Error:**

- Verify MySQL server is running
- Check database credentials in `main.py`
- Ensure the database name matches configuration

**Migration Issues:**

- Clear the `__pycache__` directories and restart the application
- Verify all required packages are installed: `pip install -r requirements.txt`

**Login Issues:**

- Ensure database tables are properly initialized from SQL scripts
- Verify user email exists in the WebsiteUsers table

---

## Contributors

Manaog, Christian Joshua
Solis, Alexander Jon S.
Torreno, Lerrica Jeremy
Virata, Sean Maverick A.

Developed as a Final Activity project for Database Management course.

---

## License

This project is provided as-is for educational purposes.
