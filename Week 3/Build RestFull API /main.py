from fastapi import FastAPI, HTTPException
from models import StudentCreate, Student
from typing import List

app = FastAPI()

students = []
current_id = 1

@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Manager API!"}

@app.post("/students/", response_model=Student, status_code=201)
def create_student(student: StudentCreate):
    global current_id
    new_student = Student(id=current_id, **student.dict())
    students.append(new_student)
    current_id += 1
    return new_student

@app.get("/students/", response_model=List[Student])
def read_students():
    return students

@app.get("/students/{student_id}", response_model=Student)
def read_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, updated_student: StudentCreate):
    for idx, student in enumerate(students):
        if student.id == student_id:
            students[idx] = Student(id=student_id, **updated_student.dict())
            return students[idx]
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{student_id}", status_code=204)
def delete_student(student_id: int):
    for idx, student in enumerate(students):
        if student.id == student_id:
            del students[idx]
            return
    raise HTTPException(status_code=404, detail="Student not found")
