
# Django Backend for Blog Application

## Overview

This is the backend of the blog application, built with Django and Django REST Framework. The backend provides RESTful API endpoints for user registration, authentication, blog post management, and comment management.

## Project Structure

```plaintext
blog_app_backend/
├── blog_app/
│   ├── __init__.py
│   ├── __pycache__/
│   ├── admin.py
│   ├── apps.py
│   ├── management/
│   │   └── commands/
│   │       ├── __pycache__/
│   │       └── generate_dummy_data.py
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── blog_app_backend/
│   ├── __init__.py
│   ├── __pycache__/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```
# Structure Definition

- blog_app/: Contains the main application logic.

- models.py: Defines the database models for Post, and Comment.

- views.py: Contains the views for handling requests and returning responses.

- serializers.py: Handles the serialization and deserialization of data for API requests and responses.

- urls.py: Maps URL routes to views.

- management/commands/: Custom Django management commands, including generate_dummy_data.py for generating sample data.

- tests.py: Contains the tests for the application.
- blog_app_backend/: Contains the settings and configuration files for the Django project.

- settings.py: Configuration file for Django settings, including database - configuration and installed apps.

- urls.py: Root URL configuration for the Django project.

- asgi.py and wsgi.py: ASGI and WSGI configuration files for deploying the application.

- manage.py: Django’s command-line utility for administrative tasks.

- requirements.txt: Lists the Python packages required by the project.


## Setup Instructions

1. **Clone the Repository:**
   ```
   git clone https://github.com/Moolfel/blog_app.git
   cd blog_app
   ```
2. **Create a Virtual Environment:**
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```
4. **Run Migrations:**
   ```
   python manage.py migrate
   ```
5. **Create a Superuser:**
   ```
   python manage.py createsuperuser
   ```
6. **Run the Development Server:**
   ```
   python manage.py runserver
   ```
7. **Note:** You can generate dummy data by running the following command:
   ```
   python manage.py generate_dummy_data
   ```
8. **Access the Admin Panel:**
   - Go to http://127.0.0.1:8000/admin
   
   ### Log in with the superuser credentials created earlier.

   - You can create new users, posts, and comments from the admin panel and
   Assign roles to users by adding them to the groups.

## Additional Notes
**Proxy Configuration for Frontend:**

proxy.conf.json is added in frontend project to configure the proxy settings for the frontend application.

This setup was done intentionally to manage API calls and proxy settings for development purposes.
