from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from . import schemas
from . import crud
from . import models


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Student Management API",
    description="REST API for managing students using FastAPI, Pydantic and SQLite",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Student Management API is running",
        "docs": "/docs"
    }


# CREATE STUDENT
@app.post(
    "/students",
    response_model=schemas.StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(
    student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):
    existing_student = db.query(
        models.Student
    ).filter(
        models.Student.email == student.email
    ).first()

    if existing_student:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Student with this email already exists"
        )

    return crud.create_student(
        db,
        student
    )


# GET ALL STUDENTS
@app.get(
    "/students",
    response_model=list[schemas.StudentResponse]
)
def get_students(
    db: Session = Depends(get_db)
):
    return crud.get_students(db)


# GET SINGLE STUDENT
@app.get(
    "/students/{student_id}",
    response_model=schemas.StudentResponse
)
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = crud.get_student(
        db,
        student_id
    )

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student {student_id} not found"
        )

    return student


# UPDATE STUDENT
@app.put(
    "/students/{student_id}",
    response_model=schemas.StudentResponse
)
def update_student(
    student_id: int,
    student: schemas.StudentUpdate,
    db: Session = Depends(get_db)
):
    existing_student = crud.get_student(
        db,
        student_id
    )

    if not existing_student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student {student_id} not found"
        )

    duplicate_email = db.query(
        models.Student
    ).filter(
        models.Student.email == student.email,
        models.Student.id != student_id
    ).first()

    if duplicate_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Another student already uses this email"
        )

    return crud.update_student(
        db,
        student_id,
        student
    )


# DELETE STUDENT
@app.delete(
    "/students/{student_id}"
)
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    deleted_student = crud.delete_student(
        db,
        student_id
    )

    if not deleted_student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student {student_id} not found"
        )

    return {
        "message": "Student deleted successfully",
        "student_id": student_id
    }