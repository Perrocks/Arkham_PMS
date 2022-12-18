from db.run_sql import run_sql

from models.doctor import Doctor
from models.patient import Patient
from models.vigilante import Vigilante

# Save new patient to the database
def save(patient):
    sql = "INSERT INTO patients(alias, name, age, enhanced, arrested_by, assigned_doctor, treatment_notes) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [patient.alias, patient.name, patient.age, patient.enhanced, patient.arrested_by, patient.assigned_doctor, patient.treatment_notes]
    results = run_sql( sql, values )
    patient.id = results[0]['id']
    return patient


# Select all saved patients from database and return
def select_all():
    patients = []

    sql = "SELECT * FROM patients"
    results = run_sql(sql)

    for row in results:
        patient = Patient(row['alias'], row['name'], row['age'], row['enhanced'], row['arrested_by'], row['assigned_doctor'], row['treatment_notes'], row['id'])
        patients.append(patient)
    return patients


# Select one patient from the database and return
def select(id):
    patient = None

    sql = "SELECT * FROM patients WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        patient = Patient(result['alias'], result['name'], result['age'], result['enhanced'], result['arrested_by'], result['assigned_doctor'], result['treatment_notes'], result['id'])
    return patient