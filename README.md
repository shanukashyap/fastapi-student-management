# FastAPI Student Management API

A RESTful Student Management API built using **FastAPI, Pydantic, SQLAlchemy, and SQLite**.

The application provides APIs to create, retrieve, update, and delete student records with request validation and proper HTTP status codes.

## Features

* Create a student
* Get all students
* Get a student by ID
* Update a student
* Delete a student
* Pydantic request validation
* Email validation
* Age validation
* Duplicate email prevention
* SQLite database
* SQLAlchemy ORM
* Swagger UI documentation
* Proper HTTP status codes
* Separation of API, schema, database, model, and CRUD logic

## Technologies

* Python
* FastAPI
* Uvicorn
* Pydantic
* SQLAlchemy
* SQLite
* Swagger UI

## Project Structure

```text
fastapi-student-management/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── crud.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone https://github.com/shanukashyap/fastapi-student-management.git
```

Move into the project:

```bash
cd fastapi-student-management
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## Swagger Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI can be used to test all API endpoints.

## API Endpoints

| Method | Endpoint                 | Description      |
| ------ | ------------------------ | ---------------- |
| POST   | `/students`              | Create a student |
| GET    | `/students`              | Get all students |
| GET    | `/students/{student_id}` | Get one student  |
| PUT    | `/students/{student_id}` | Update a student |
| DELETE | `/students/{student_id}` | Delete a student |

## Student Fields

Each student contains:

* `id`
* `name`
* `email`
* `age`
* `course`

## Create Student

### Request

```http
POST /students
```

Example:

```json
{
  "name": "Ananya Sharma",
  "email": "ananya@example.com",
  "age": 22,
  "course": "Generative AI"
}
```

### Response

```json
{
  "id": 1,
  "name": "Ananya Sharma",
  "email": "ananya@example.com",
  "age": 22,
  "course": "Generative AI"
}
```

## Get All Students

```http
GET /students
```

Returns all students stored in the database.

## Get Student by ID

```http
GET /students/1
```

Returns the student whose ID is `1`.

If the student doesn't exist:

```json
{
  "detail": "Student 1 not found"
}
```

## Update Student

```http
PUT /students/1
```

Example:

```json
{
  "name": "Ananya Sharma",
  "email": "ananya@example.com",
  "age": 23,
  "course": "Generative AI Engineering"
}
```

## Delete Student

```http
DELETE /students/1
```

Response:

```json
{
  "message": "Student deleted successfully",
  "student_id": 1
}
```

## Pydantic Validation

The API validates incoming student data.

### Name

The name must contain between 2 and 100 characters.

### Email

The email must have a valid email format.

### Age

The age must be between 5 and 100.

### Course

The course must contain between 2 and 100 characters.

Invalid data is rejected automatically by FastAPI and Pydantic.

## Error Handling

The API uses appropriate HTTP status codes.

| Status Code | Meaning                                  |
| ----------- | ---------------------------------------- |
| 200         | Successful request                       |
| 201         | Student successfully created             |
| 400         | Duplicate email or invalid business rule |
| 404         | Student not found                        |
| 422         | Request validation failed                |

## Database

The application uses SQLite.

The database file is:

```text
students.db
```

SQLAlchemy is used as the ORM to interact with the database.

The database file is included in `.gitignore` and is not pushed to GitHub.

## Application Flow

```text
Client
   ↓
FastAPI Endpoint
   ↓
Pydantic Validation
   ↓
CRUD Function
   ↓
SQLAlchemy
   ↓
SQLite Database
   ↓
Response
```

## Testing

The APIs can be tested using:

* Swagger UI
* Postman

Recommended testing scenarios:

1. Create a valid student.
2. Get all students.
3. Get a student by ID.
4. Update a student.
5. Delete a student.
6. Try an invalid email.
7. Try an invalid age.
8. Try a duplicate email.
9. Request a student ID that does not exist.

## Learning Outcomes

Through this project, I learned:

* FastAPI application development
* REST API design
* HTTP methods
* Pydantic validation
* SQLAlchemy ORM
* SQLite database integration
* CRUD operations
* Dependency injection
* HTTP status codes
* Error handling
* Swagger API testing
* Git and GitHub project management

## GitHub Repository

https://github.com/shanukashyap/fastapi-student-management

