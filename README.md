Little Lemon API - Test Paths

1. Menu Items:
   - GET/POST: http://127.0.0.1:8000/menu-item/
     - Example:

```json
{
  "title": "salad",
  "price": "99",
  "inventory": 10
}
```
   - GET/PUT/DELETE (Single Item): http://127.0.0.1:8000/menu-item/{id}

2. Table Bookings:
   - GET/POST: http://127.0.0.1:8000/restaurant/booking/tables/
     - Example:

```json
{
  "first_name": "ramz",
  "reservation_date": "2026-04-09",
  "no_of_guests": 2
}
```

3. User Authentication (Djoser):
   - Registration: http://127.0.0.1:8000/auth/users/
   - Login (Token): http://127.0.0.1:8000/auth/token/login/
   - Logout: http://127.0.0.1:8000/auth/token/logout/

Note: To test protected endpoints, include the 'Authorization: Token <your_token>' header.
