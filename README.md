# EMPLOYEE RECORD MANAGEMENT SYSTEM


Overview

The Employee Record Management System (ERMS) is a web-based application that simplifies the process of managing employee 
information within an organization. It utilizes Django Rest Framework (DRF) for the backend and MySQL for
the database, offering a robust, scalable, and flexible solution for storing and managing employee records.<br><br>

Features<br>
    CRUD Operations: Create, Read, Update, and Delete employee records.<br>
    Database Integration: Secure storage of employee information using MySQL.<br>
    RESTful API: Designed with Django Rest Framework to ensure API flexibility.<br>
    Scalable: Easily adaptable to larger datasets as the organization grows.<br>
<br>
Project Structure<br>
    api/                : Contains the API logic and routes.<br>
    emp_rec_management/ :  Main Django app folder with settings and configurations.<br>
    screenshots/        : Folder containing images to showcase the UI.<br>
    manage.py           : Django’s command-line utility for administrative tasks.<br>
<br>
Setup Instructions

   Clone the repository:
  
    git clone https://github.com/versatile-vidya/employee_record_management.git

Install the dependencies:

    pip install -r requirements.txt

Configure the database settings in settings.py:

python

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
    }

Run the database migrations:

    python manage.py migrate

Start the development server:
         
     python manage.py runserver
##Technologies Used<br>
   Django Rest Framework
    MySQL
    Python
