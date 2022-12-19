from db.run_sql import run_sql

from models.doctor import Doctor
from models.patient import Patient
from models.vigilante import Vigilante

import repositories.vigilante_repository as vigilante_repository
import repositories.doctor_repository as doctor_repository

# Save new patient to the database
def save(patient):
    sql = "INSERT INTO patients(alias, name, age, enhanced, vigilante_id, doctor_id, treatment_notes) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    
    values = [patient.alias, patient.name, patient.age, patient.enhanced, patient.vigilante.id, patient.doctor.id, patient.treatment_notes]
    
    results = run_sql( sql, values )
    patient.id = results[0]['id']
    return patient


# Select all saved patients from database and return
def select_all():
    patients = []

    sql = "SELECT * FROM patients"
    results = run_sql(sql)

    for row in results:
        vigilante = vigilante_repository.select(row['vigilante_id'])
        doctor = doctor_repository.select(row['doctor_id'])

        patient = Patient(row['alias'], row['name'], row['age'], row['enhanced'], vigilante.name, doctor.name, row['treatment_notes'], row['id'])
        
        patients.append(patient)
    return patients


# Select one patient from the database and return
def select(id):
    patient = None

    sql = "SELECT * FROM patients WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    
    if results:
        result=results[0]

        vigilante = vigilante_repository.select(result['vigilante_id'])
        doctor = doctor_repository.select(result['doctor_id'])

        patient = Patient(result['alias'], result['name'], result['age'], result['enhanced'], vigilante, doctor, result['treatment_notes'], result['id'])
    return patient

# Delete all from patients table
def delete_all():
    sql = "DELETE  FROM patients"
    run_sql(sql)

def patients_by_vigilante(vigilante):
    patients = []

    sql = "SELECT * FROM patients WHERE vigilante_id = %s"
    values = [vigilante.id]
    results = run_sql(sql, values)
    if results: 
        for row in results:
            doctor = doctor_repository.select(row['doctor_id'])
            patient = Patient(row['alias'], row['name'], row['age'], row['enhanced'], vigilante, doctor, row['treatment_notes'], row['id'])
            patients.append(patient)
    return patients 

def patients_by_doctor(doctor):
    patients = []

    sql = "SELECT * FROM patients WHERE doctor_id = %s"
    values = [doctor.id]
    results = run_sql(sql, values)
    if results: 
        for row in results:
            vigilante = vigilante_repository.select(row['vigilante_id'])
            patient = Patient(row['alias'], row['name'], row['age'], row['enhanced'], vigilante, doctor, row['treatment_notes'], row['id'])
            patients.append(patient)
    return patients

def delete(id):
    sql = "DELETE  FROM patients WHERE id = %s"
    values = [id]
    run_sql(sql, values)

