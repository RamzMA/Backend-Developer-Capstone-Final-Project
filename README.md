# 🍋 Little Lemon API

A REST API for the Little Lemon restaurant — built with Django REST Framework. Supports menu management, table bookings, and token-based user authentication via Djoser.

---

## 🚀 Getting Started

```bash
pipenv install
pipenv shell
python manage.py migrate
python manage.py runserver
```

---

## 📌 API Endpoints

### 1. 🍽️ Menu Items

- **GET/POST:** `http://127.0.0.1:8000/menu-item/`
  - Example request body:

```json
{
  "title": "salad",
  "price": "9.99",
  "inventory": 10
}
```

- **GET/PUT/DELETE** (Single Item): `http://127.0.0.1:8000/menu-item/{id}`

---

### 2. 📅 Table Bookings

- **GET/POST:** `http://127.0.0.1:8000/restaurant/booking/tables/`
  - Example request body:

```json
{
  "first_name": "ramz",
  "reservation_date": "2026-04-09",
  "no_of_guests": 2
}
```

---

### 3. 🔐 User Authentication (Djoser)

- **Registration:** `http://127.0.0.1:8000/auth/users/`
- **Login (Token):** `http://127.0.0.1:8000/auth/token/login/`
- **Logout:** `http://127.0.0.1:8000/auth/token/logout/`

---

## 🔑 Protected Endpoints

To access protected endpoints, include the following header in your request:

```
Authorization: Token <your_token>
```

---

## 🛠️ Tech Stack

- **Backend** — Django, Django REST Framework
- **Auth** — Djoser + Token Authentication
- **Database** — MySQL