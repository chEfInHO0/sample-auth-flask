<div align="center">

[Check the current state of the project here!](https://github.com/chEfInHO0/sample-auth-flask/tree/dev)

# 🔐 Flask Auth Demo

A simple **authentication demo** built with **Flask** and **SQLite**, showcasing the complete process of **user registration and login** with best practices in **backend architecture**, **validation**, and **error handling**.

---

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Database-07405e?logo=sqlite&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Active-success)

</div>

---

## 🚀 About the Project

This project is a **Flask-based authentication demo**, designed to illustrate the full workflow of **user registration, authentication, and database management**, using **a clean modular architecture** and **custom SQL error handling**.

The main goal is to demonstrate how to structure a maintainable backend API with solid foundations for scaling or integrating with front-end frameworks like React or Vue.

---

## 🧠 Features

✅ User registration
✅ Login with credential verification
✅ Secure password hashing
✅ SQL error handling middleware
✅ Centralized logging system
✅ Modular and scalable architecture

---

## 🧩 Tech Stack

| Category          | Technologies          |
| ----------------- | --------------------- |
| **Language**      | Python 3.12+          |
| **Web Framework** | Flask                 |
| **Database**      | SQLite                |
| **ORM**           | SQLAlchemy            |
| **Validation**    | Pydantic              |
| **Migrations**    | Flask-Migrate         |
| **Logs**          | Python Logging module |

---

## 📂 Project Structure

```bash
sample-auth-flask/
│
├── logs/                 # Log files (runtime errors, events, etc.)
│
├── middleware/           # Custom middlewares
│   └── sqlErrorHandler.py
│
├── models/               # SQLAlchemy models
│   └── user_model.py
│
├── schemas/              # Pydantic schemas for validation
│   └── user_schema.py
│
├── __init__.py           # Marks directory as a Python package
├── .env.example          # Example environment configuration
├── .gitignore            # Git ignore file
├── app.py                # Flask application entry point
├── database.py           # Database configuration and initialization
├── db_init.py            # Script for initial table creation
├── README.md             # Project documentation
└── requirements.txt      # Project dependencies
```

---

## ⚙️ How to Run the Project

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/flask-auth-demo.git
   cd flask-auth-demo
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux / macOS
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your `.env` file**

   Copy `.env.example` to `.env` and configure your environment variables:

   ```bash
   cp .env.example .env
   ```

   ### `.env.example`

   ```env
   # Flask secret key
   SECRET_KEY="your_secret_key"

   # Database connection string
   SQLALCHEMY_DATABASE_URI="sqlite:///your_database.db"

   # Session configuration
   SESSION_COOKIE_HTTPONLY=True  # Protects cookies from client-side scripts
   SESSION_COOKIE_SECURE=True    # Use False for local development
   SESSION_COOKIE_SAMESITE="Lax"

   # Remember-me configuration
   REMEMBER_COOKIE_DURATION=7    # Days
   REMEMBER_USER=True

   # Docker-Compose ENV

   MYSQL_ROOT_PASSWORD=MYSQL_PASSWORD
   MYSQL_DATABASE=MYSQL_DATABASE
   MYSQL_USER=MYSQL_USER
   MYSQL_PASSWORD=MYSQL_PASSWORD
   MYSQL_PORT=MYSQL_PORT
   ```

5. **Initialize the database (if required)**

   ```bash
   python db_init.py
   ```

6. **Start the Flask server**

   ```bash
   flask run
   ```

---

## 📬 Main Endpoints

| Method | Endpoint    | Description              |
| ------ | ----------- | ------------------------ |
| `POST` | `/register` | Register a new user      |
| `POST` | `/login`    | Authenticate and get JWT |

**Example request (register):**

```json
{
  "email": "user@example.com",
  "password": "123456"
}
```

**Example response (handled error):**

```json
{
  "message": "Email already registered.",
  "error": "UNIQUE constraint failed: users.email",
  "status_code": 409
}
```

---

## 🧾 Error Handling & Logging

This project includes a **custom SQL error handler middleware** that intercepts database exceptions and returns structured JSON responses while also logging details to both file and console.

```python
class SqlErrorHandler:
    def __init__(self, error):
        self.error = error

    def errors(self):
        ...
        logger.error(f"[{code}] {error_type}: {error_msg}")
        return {"message": message, "status_code": code}
```

Logs are automatically saved in the `/logs` directory.

---

## 🧭 Roadmap

- [ ] Add JWT authentication
- [ ] Implement refresh tokens
- [ ] Create unit tests with `pytest`
- [ ] Add CI/CD using GitHub Actions
- [ ] Add Docker containerization

---

## 👨‍💻 Author

**Luccas Santos**
Backend Developer • Python • Flask • FastAPI • Node.js

📧 [luccaselias0@gmail.com](mailto:luccaselias0@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/luccas-santos-3)

---

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with 💙 by **Luccas Santos**
If you liked it, ⭐ the repository and contribute!

</div>

---
