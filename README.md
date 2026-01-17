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

---

# Python Django Rest API Notes

Here we document the Python Django concepts that have been learned.

## 1. Django Installation Check

To verify if Django is installed on the server:
```bash
python -m m django --version
```

## 2. Virtual Environment Setup

Create and activate a virtual environment:
```bash
python -m venv .venv
.\\.venv\\Scripts\\activate.bat  # On Windows
```

## 3. Django Project Setup

Initialize a Django project and create an app:
```bash
django-admin startproject <project_name>
cd <project_name>
python manage.py startapp <app_name>
```

## 4. Creating Endpoints (Views)

Create endpoints in `views.py`:
```python
from django.http import HttpResponse

def endpoint_name(request):
    return HttpResponse("Response content")
```

## 5. URL Configuration

Update `urls.py` to map endpoints:
```python
path("", views.endpoint_name)
```

Also create an `urls.py` file inside the app directory and include it in the project's main `urls.py` file.

## 6. Database Models

Create models in `models.py`:
```python
class Items(models.Model):
    item_name = models.CharField(max_length=100)
    item_desc = models.TextField()
    item_price = models.FloatField()
```

## 7. Migrations

Apply database changes:
```bash
python manage.py makemigrations  # Create migrations (run each time you create new models)
python manage.py migrate         # Apply migrations to the database
```

## 8. Admin Panel Registration

Register models in the admin panel by updating `admin.py`:
```python
from .models import Items

admin.site.register(Items)
```

## 9. Creating a Superuser Account

Create an admin account:
```bash
python manage.py createsuperuser
```

Access the admin panel at `http://127.0.0.1:8000/admin/`

## 10. Interacting with the Database via Shell

Access the Django shell to insert data manually:
```bash
python manage.py shell

>>> data = Items(item_name="Burger", item_desc="Veg Burger", item_price=8)
>>> data.save()
```
