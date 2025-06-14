# Activity Tracker API

A Django REST Framework (DRF) based backend for tracking user activities with statuses and metadata. 

---

## 📌 Features

- Token or Basic authentication support (default: BasicAuth)
- Filterable logs by status, user, or action
- Separate endpoint for status-only updates
- Django admin and browsable API
- Swagger UI for documentation
- Test coverage for models and views

---

## ⚙️ Setup Instructions

- ### Clone the Repository
    ```bash
    git clone https://github.com/jisan09/activity-tracker.git
    cd activity-tracker
    ```
- ### Create and Activate a Virtual Environment
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
- ### Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```
- ### Apply Migrations
    ```bash
    python manage.py migrate
    ```
- ### Create Superuser
    ```bash
    python manage.py createsuperuser
    ```
- ### Run Development Server
    ```bash
    python manage.py runserver
    ```
- ### To populate sample data (optional)
    ```bash
    python manage.py seed_activity
    ```
  
## ✅ Running Tests
`python manage.py test apps.activity.tests --keepdb`

## 📄 API Documentation
- #### Swagger UI: http://127.0.0.1:8000/swagger/

- #### Django Admin: http://127.0.0.1:8000/admin/

- ##### Use your superuser credentials to access the admin panel. 
  ```
  # Sample credenatials for the DB (shared on mail) data
    - userID= mdjisan
    - password= Jisan123
    ```
## 📁 Project Structure
```
activity_tracker/
├── apps
│     ├── __init__.py
│     └── activity
│         ├── __init__.py
│         ├── admin.py
│         ├── apps.py
│         ├── filters.py
│         ├── management
│         │     └── commands
│         │         └── seed_activity.py
│         ├── migrations
│         │     ├── 0001_initial.py
│         │     └── __init__.py
│         ├── models.py
│         ├── serializers.py
│         ├── tests
│         │     ├── __init__.py
│         │     ├── test_model.py
│         │     └── test_view.py
│         ├── tests.py
│         ├── urls.py
│         └── views.py
├── core
│     ├── __init__.py
│     ├── settings.py
│     ├── urls.py
│     └── wsgi.py
├── README.md
├── manage.py
└── requirements.txt

```

## 🔀 Sample API Calls (cURL)

<details> <summary><strong>🔹 Create a Log Entry</strong></summary>

```bash
curl -su mdjisan:Jisan123 -X POST "http://127.0.0.1:8000/api/logs/" \
-H "Content-Type: application/json" \
-d '{
  "action": "UPLOAD_FILE",
  "status": "PENDING",
  "metadata": {
    "filename": "sample.txt"
  }
}' | python3 -m json.tool
```

</details> <details> <summary><strong>🔹 List All Logs</strong></summary>

```bash
curl -su mdjisan:Jisan123 "http://127.0.0.1:8000/api/logs/" | python3 -m json.tool
```

</details> <details> <summary><strong>🔹 Filter Logs by Status</strong></summary>

```bash
curl -su mdjisan:Jisan123 "http://127.0.0.1:8000/api/logs/?status=PENDING" | python3 -m json.tool
```

</details> <details> <summary><strong>🔹 Filter Logs by User</strong></summary>

```bash
curl -su mdjisan:Jisan123 "http://127.0.0.1:8000/api/logs/?user_id=2" | python3 -m json.tool
```

</details> <details> <summary><strong>🔹 Retrieve Log by ID</strong></summary>

```bash
curl -su mdjisan:Jisan123 "http://127.0.0.1:8000/api/logs/20/" | python3 -m json.tool
```

</details> <details> <summary><strong>🔹 Update Log (PUT)</strong></summary>

```bash
curl -su mdjisan:Jisan123 -X PUT "http://127.0.0.1:8000/api/logs/20/" \
-H "Content-Type: application/json" \
-d '{
  "action": "UPLOAD_FILE",
  "status": "DONE",
  "metadata": {
    "filename": "updated.txt"
  }
}' | python3 -m json.tool
```

</details> <details> <summary><strong>🔹 Update Status Only (PATCH)</strong></summary>

```bash
curl -su mdjisan:Jisan123 -X PATCH "http://127.0.0.1:8000/api/logs/20/update-status/" \
-H "Content-Type: application/json" \
-d '{
  "status": "IN_PROGRESS"
}' | python3 -m json.tool
```

</details> <details> <summary><strong>🔹 Delete Log</strong></summary>

```bash
curl -su mdjisan:Jisan123 -X DELETE "http://127.0.0.1:8000/api/logs/33/" | python3 -m json.tool
```
</details>