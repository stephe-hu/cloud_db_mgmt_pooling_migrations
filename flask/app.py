from flask import Flask, render_template
from sqlalchemy import create_engine
import pandas as pd
from pandas import read_sql
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect

app = Flask(__name__)

load_dotenv()  # Load environment variables from .env file

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    "?charset=utf8mb4"
)

# Database connection settings
# Database connection settings
db_engine = create_engine(conn_string, echo=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/patients')
def patients():
    query_patients = "SELECT * FROM patients"
    df_patients = read_sql(query_patients, db_engine)
    data_patients = df_patients.to_dict(orient='records')
    return render_template('patients.html', data=data_patients)

@app.route('/medicalrecords')
def medicalrecords():
    query_medical_records = "SELECT * FROM medical_records"
    df_medical_records = read_sql( query_medical_records, db_engine)
    data_medical_records = df_medical_records.to_dict(orient='records')
    return render_template('medical_records.html', data=data_medical_records)

@app.route('/doctors')
def doctors():
    query_doctors = "SELECT * FROM doctors"
    df_doctors = read_sql(query_doctors, db_engine)
    data_doctors = df_doctors.to_dict(orient='records')
    return render_template('doctors.html', data=data_doctors)

if __name__ == '__main__':
    app.run(debug=True)