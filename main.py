from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import engine, Base, get_db
import crud

app = FastAPI(title="AI Attendance Backend")

# (선택) 개발 단계에서만 사용
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "AI Attendance API running"}


@app.post("/users")
def create_user(name: str, student_no: str, db: Session = Depends(get_db)):
    existing = crud.get_user_by_student_number(db, student_no)
    if existing:
        raise HTTPException(status_code=400, detail="Student already exists")
    return crud.create_user(db, name, student_no)


@app.post("/attendance")
def attendance(user_id: str, status: str, db: Session = Depends(get_db)):
    return crud.add_attendance_log(db, user_id, status)


@app.get("/attendance")
def attendance_logs(db: Session = Depends(get_db)):
    return crud.get_attendance_logs(db)
