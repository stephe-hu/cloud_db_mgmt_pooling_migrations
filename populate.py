import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from faker import Faker
import random
from datetime import date

# Load environment variables
load_dotenv()

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
)

# Create a database engine
db_engine = create_engine(conn_string, echo=False)
fake = Faker()

specializations = ['Cardiology', 'Neurology', 'Pediatrics', 
                   'Orthopedics', 'Radiology', 'General Practice']

diagnoses = ['Diabetes', 'Aortic Aneurysm', 'Malnutrition', 'Concussion', 'Arrhythmia', 'Arthritis']

treatments = ['Exercise', 'Diet', 'Get Enough Sleep']

genders = ['Male', 'Female']

def insert_fake_data(engine, num_patients=50, num_medical_records=70, num_doctors=7):
    with engine.connect() as connection:
        # Insert fake patients
        for _ in range(num_patients):
            first_name = fake.first_name()
            last_name = fake.last_name()
            date_of_birth = fake.date_of_birth(minimum_age=10, maximum_age=90)
            gender = random.choice(genders)
            contact_number = fake.phone_number()
            query = text(
                "INSERT INTO patients (first_name, last_name, date_of_birth, gender, contact_number)"
                "VALUES (:first_name, :last_name, :date_of_birth, :gender, :contact_number)"
            )
            connection.execute(query, {
                "first_name": first_name,
                "last_name": last_name,
                "date_of_birth": date_of_birth,
                "gender": gender, 
                "contact_number": contact_number
            })

        # Insert fake doctors
        for _ in range(num_doctors):
            first_name = fake.first_name()
            last_name = fake.last_name()
            specialization = random.choice(specializations)
            contact_number = fake.phone_number()
            query = text(
                "INSERT INTO doctors (first_name, last_name, specialization, contact_number) "
                "VALUES (:first_name, :last_name, :specialization, :contact_number)"
            )
            connection.execute(query, {
                "first_name": first_name,
                "last_name": last_name,
                "specialization": specialization,
                "contact_number": contact_number
            })

        # Fetch all patient IDs, medication IDs, and provider IDs
        query = text("SELECT id FROM patients")
        patient_ids = [row[0] for row in connection.execute(query).fetchall()]
        query3 = text("SELECT id FROM doctors")
        doctor_ids = [row[0] for row in connection.execute(query3).fetchall()]

        # Insert fake medical records
        for _ in range(num_medical_records):
            patient_id = random.choice(patient_ids)
            doctor_id = random.choice(doctor_ids)
            diagnosis = random.choice(diagnoses)
            treatment = random.choice(treatments)
            admission_date = fake.date_between_dates(date_start=date(2010, 1, 1), date_end=date(2023, 10, 23))
            discharge_date = fake.date_between_dates(date_start=admission_date, date_end=date(2023, 10, 23))
            query = text(
                "INSERT INTO medical_records (patient_id, doctor_id, diagnosis, treatment, admission_date, discharge_date) "
                "VALUES (:patient_id, :doctor_id, :diagnosis, :treatment, :admission_date, :discharge_date)"
            )
            connection.execute(query, {
                "patient_id": patient_id,
                "doctor_id": doctor_id,
                "diagnosis": diagnosis,
                "treatment": treatment,
                "admission_date": admission_date,
                "discharge_date": discharge_date
            })

        connection.commit() 
        
if __name__ == "__main__":
    insert_fake_data(db_engine)
    print("Fake data insertion complete!")
