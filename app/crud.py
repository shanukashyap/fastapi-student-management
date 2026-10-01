from sqlalchemy.orm import Session

from . import models


def create_student(db: Session, student_data):
    student = models.Student(
        name=student_data.name,
        email=student_data.email,
        age=student_data.age,
        course=student_data.course
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return student


def get_students(db: Session):
    return db.query(models.Student).all()


def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()


def update_student(db: Session, student_id: int, student_data):
    student = get_student(db, student_id)

    if not student:
        return None

    student.name = student_data.name
    student.email = student_data.email
    student.age = student_data.age
    student.course = student_data.course

    db.commit()
    db.refresh(student)

    return student


def delete_student(db: Session, student_id: int):
    student = get_student(db, student_id)

    if not student:
        return None

    db.delete(student)
    db.commit()

    return student