# Mysite

A Django web application project.

## Project Structure

```
Mysite/
├── myapp/              # Django app directory
│   ├── migrations/     # Database migrations
│   ├── templates/      # HTML templates
│   ├── models.py       # Database models
│   ├── views.py        # View functions/classes
│   ├── urls.py         # App URL configuration
│   ├── admin.py        # Django admin configuration
│   └── tests.py        # Unit tests
├── mysite/             # Project configuration
│   ├── settings.py     # Project settings
│   ├── urls.py         # Project URL configuration
│   ├── wsgi.py         # WSGI configuration
│   └── asgi.py         # ASGI configuration
├── manage.py           # Django management script
└── db.sqlite3          # SQLite database
```

## Setup Instructions

1. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   ```

2. **Install dependencies:**
   ```bash
   pip install django
   ```

3. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

The application will be available at `http://127.0.0.1:8000/`

## Usage

- Access the main app at `/`
- Access Django admin panel at `/admin/`

## Available Commands

- `python manage.py runserver` - Start the development server
- `python manage.py makemigrations` - Create new migrations
- `python manage.py migrate` - Apply migrations to the database
- `python manage.py createsuperuser` - Create an admin user
- `python manage.py test` - Run tests
