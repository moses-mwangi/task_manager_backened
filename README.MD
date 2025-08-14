# Task Management API

A simple **Django REST Framework (DRF)** backend for managing tasks.  
Supports **CRUD operations**, **filtering**, **pagination**, and **bulk creation**.

---

## Features

- Create, Read, Update, Delete (CRUD) tasks
- Filter tasks by `is_completed` status
- Pagination (5 tasks per page)
- Bulk create tasks (send a list of tasks in one request)
- Unit tests covering all endpoints

- GET /api/tasks/ # List tasks
- POST /api/tasks/ # Create single or multiple tasks
- GET /api/tasks/?is_completed=false&page=1

- GET /api/tasks/<id>/ # Retrieve task
- PUT /api/tasks/<id>/ # Update full task
- PATCH /api/tasks/<id>/ # Update partial task
- DELETE /api/tasks/<id>/ # Delete task

---

## Tech Stack

- Python 3.10.18
- Django 5.2
- Django REST Framework
- django-filter

---

## Installation

1️⃣ **Clone the repository**

```bash
git clone <your-repo-url>
cd task_project
```

python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows

## Install dependencies

pip install -r requirements.txt
pip freeze > requirements.txt

## Apply migrations

python manage.py migrate

## Run the development server

python manage.py runserver

## Run the development server for Testing

python manage.py test

## Python version

## Python version: 3.10.18

git@github.com:moses-mwangi/task_manager_frontend.git
