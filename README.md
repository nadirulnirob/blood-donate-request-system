# Blood Donate & Request System

A Django-based web application that helps users find blood donors and create or manage blood requests. The system provides donor profiles, blood request management, filtering, authentication, and a simple responsive interface.

## Features

* User registration, login, and logout
* User profile creation and update
* Profile picture support
* Donor profile creation and update
* Donor availability management
* Search donors by:

  * Blood group
  * Location
  * Availability
* Create, view, edit, and delete blood requests
* Update blood request status
* Blood request status:

  * Pending
  * Fulfilled
  * Cancelled
* Filter blood requests by blood group, location, and status
* View complete donor details
* View complete blood request details
* Users can modify or delete only their own records
* Pagination for donor and blood request lists
* Django messages for user feedback
* Django Admin Panel
* Responsive design using Bootstrap
* Blood group validation
* Phone number validation
* Positive blood bag validation
* Required date validation
* Blood compatibility information

## Technologies Used

* Python
* Django
* SQLite
* HTML5
* CSS3
* Bootstrap 5
* Pillow

## Project Structure

```text
Blood Donate Request/
│
├── accounts/
├── blood_requests/
├── donors/
├── bloodsystem/
├── templates/
├── static/
├── media/
├── manage.py
├── requirements.txt
└── .gitignore
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/nadirulnirob/blood-donate-request-system.git
```

### 2. Open the project folder

```bash
cd blood-donate-request-system
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install the required packages

```bash
python -m pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create an admin account

```bash
python manage.py createsuperuser
```

### 8. Run the development server

```bash
python manage.py runserver
```

### 9. Open the website

Open the following address in your browser:

```text
http://127.0.0.1:8000/
```

## Admin Panel

The Django administration panel can be accessed from:

```text
http://127.0.0.1:8000/admin/
```

An admin account can be created using:

```bash
python manage.py createsuperuser
```

## Main Pages

* Home
* Register
* Login
* My Profile
* Find Donors
* Donor Details
* Become a Donor
* Blood Requests
* Request Details
* Create Blood Request
* My Requests
* Django Admin

## Blood Groups

The system supports the following blood groups:

* A+
* A-
* B+
* B-
* AB+
* AB-
* O+
* O-

## Security and Data Handling

The system uses Django authentication to protect user accounts. Users can edit or delete only their own donor profiles and blood requests.

Sensitive development files such as the virtual environment, SQLite database, Python cache files, and environment files are excluded using `.gitignore`.

## Purpose

The purpose of this project is to provide a simple platform where people can search for available blood donors and manage blood requests efficiently.

## Author

**Nadirul Nirob**

BSc in Computer Science and Engineering
IUBAT – International University of Business Agriculture and Technology

## License

This project was developed as an academic project for educational purposes.
