# Task 04 – REST API with Flask

## Objective
Build a simple REST API to manage user data with CRUD operations.

## Tech Stack
- Python
- Flask

## How to Run
```bash
pip install flask
python app.py
```

## API Endpoints

| Method | Endpoint           | Description            |
|--------|--------------------|------------------------|
| POST   | /users             | Create a new user      |
| GET    | /users             | Get all users          |
| GET    | /users/<username>  | Get a user by username |
| PUT    | /users/<username>  | Update user data       |
| DELETE | /users/<username>  | Delete a user          |

## Example Request Body for POST/PUT
```json
{
  "username": "john",
  "email": "john@example.com",
  "age": 25
}
```

## Example Response
```json
{
  "message": "User created successfully"
}
```

## Files in Repo
- `app.py` → Main Flask API code
- `README.md` → This file
-  screenshots

## Outcome
A functional REST API using Flask with basic CRUD operations, tested using Postman or curl.

