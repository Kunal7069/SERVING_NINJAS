from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from app.database.config import SessionLocal
from app.schemas.appointment_schema import AppointmentCreate, AppointmentResponse
from app.models.doctor import Doctor
from app.services.appointment_service import create_appointment,get_appointments_by_patient_name,get_appointments_by_doctor_id
from app.services.doctor_service import get_all_doctors_with_slots

import smtplib
from email.message import EmailMessage

router = APIRouter(prefix="/appointment", tags=["Appointments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class EmailRequest(BaseModel):
    receiver_email: EmailStr
    body: str
     
@router.post("/send-email")
def send_email(request: EmailRequest):
    sender_email = 'tarsamsabbarwal9@gmail.com'
    subject = 'Booking Confirmed'
    app_password = 'rwji ibyu ynof woav'  

    # Compose email
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = request.receiver_email
    msg['Subject'] = subject
    msg.set_content(request.body)

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(msg)
        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")

@router.post("/", response_model=AppointmentResponse)
def book_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    return create_appointment(db, appointment.dict())

class PatientNameRequest(BaseModel):
    patient_name: str

@router.post("/by-patient")
def get_appointments_for_patient(data: PatientNameRequest, db: Session = Depends(get_db)):
    appointments = get_appointments_by_patient_name(db, data.patient_name)
    result = []
    if not appointments:
        return result
    return appointments

class DoctorIdRequest(BaseModel):
    doctor_name: str

@router.post("/by-doctor")
def get_appointments_for_doctor(data: DoctorIdRequest, db: Session = Depends(get_db)):
    doctor = db.query(Doctor).filter(Doctor.doctor_name == data.doctor_name).first()

    appointments = get_appointments_by_doctor_id(db, doctor.id)
    result=[]
    if not appointments:
        return result
    return appointments