from sqlalchemy.orm import Session
from models import User, FaceEncoding, AttendanceLog


def create_user(db: Session, name: str, student_no: str):
    user = User(
        name=name,
        student_no=student_no,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_student_number(db: Session, student_no: str):
    return db.query(User).filter(User.student_no == student_no).first()


def add_face_encoding(db: Session, user_id, encoding: str):
    face = FaceEncoding(
        user_id=user_id,
        encoding=encoding,
    )
    db.add(face)
    db.commit()
    db.refresh(face)
    return face


def add_attendance_log(db: Session, user_id, status: str):
    log = AttendanceLog(
        user_id=user_id,
        status=status,
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log


def get_attendance_logs(db: Session):
    return db.query(AttendanceLog).order_by(AttendanceLog.timestamp.desc()).all()
