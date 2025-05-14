# 📘 Flask REST API

This is a RESTful API built with Flask that allows users to register, login, and manage their personal items.

## 🔧 Features

- JWT Authentication
- User Registration and Login
- Create, Read, Update, Delete (CRUD) for user-specific items
- Protect routes for logged-in users
- GitHub Actions CI for testing

## 🚀 Technologies

- Python 3
- Flask
- Flask-JWT-Extended
- SQLAlchemy
- SQLite (or switchable to PostgreSQL/MySQL)
- GitHub Actions for CI

API Endpoints

    POST /register - Register new user

    POST /login - Login and get token

    GET /myitems - Get items for logged-in user

    POST /items - Add new item (auth required)

    PUT /items/<id> - Update an item (auth required)

    DELETE /items/<id> - Delete an item (auth required)

## ▶️ Setup

```bash
# Clone the repo
git clone https://github.com/samrato/flaskPi.git
cd flask-api

# Create virtual environment and activate
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
app run
