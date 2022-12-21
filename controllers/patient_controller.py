from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.patient import Patient

import repositories.patient_repository as patient_repository
import repositories.doctor_repository as doctor_repository
import repositories.vigilante_repository as vigilante_repository

patients_blueprint = Blueprint("patients", __name__)

# Displays a list of patients
# ---------------------------------
@patients_blueprint.route("/patients")
def show_all_patients():
    patients = patient_repository.select_all()
    return render_template("patients/index.html", patients = patients)

# Displays the details of one patient
# ---------------------------------
@patients_blueprint.route("/patients/<id>")
def show(id):
    patient = patient_repository.select(id)
    return render_template("patients/show.html", patient=patient)

# Allows user to save a new patient to the database
# ---------------------------------
@patients_blueprint.route("/patients/new", methods=['GET'])
def new_patient():
    doctors = doctor_repository.select_all()
    vigilantes = vigilante_repository.select_all()
    return render_template("patients/new.html", doctors = doctors, vigilantes = vigilantes)

@patients_blueprint.route("/patient",  methods=['POST'])
def create_patient():

    alias = request.form['alias']
    name = request.form['name']
    age = request.form['age']
    enhanced = True if 'enhanced' in request.form else False
    vigilante_id = request.form['vigilante_id']
    doctor_id = request.form['doctor_id']
    treatment_notes = request.form['treatment_notes']

    doctor = doctor_repository.select(doctor_id)
    vigilante = vigilante_repository.select(vigilante_id)

    patient = Patient(alias, name, age, enhanced, vigilante, doctor, treatment_notes )
    patient_repository.save(patient)
    return redirect('/patients')

# Deletes selected patient
# ---------------------------------
@patients_blueprint.route("/patients/<id>/delete", methods=['POST'])
def delete_patient(id):
    patient_repository.delete(id)
    return redirect('/patients')

# Allows user to update details of selected patient
# ---------------------------------
@patients_blueprint.route("/patients/<id>/edit", methods=['GET'])
def edit_patient(id):
    patient = patient_repository.select(id)
    doctors = doctor_repository.select_all()
    vigilantes = vigilante_repository.select_all()
    return render_template("patients/edit.html", patient = patient, doctors = doctors, vigilantes = vigilantes)

@patients_blueprint.route("/patients/<id>", methods=['POST'])
def update_patient(id):
    alias = request.form['alias']
    name = request.form['name']
    age = request.form['age']
    enhanced = True if 'enhanced' in request.form else False
    vigilante_id = request.form['vigilante_id']
    doctor_id = request.form['doctor_id']
    treatment_notes = request.form['treatment_notes']

    doctor = doctor_repository.select(doctor_id)
    vigilante = vigilante_repository.select(vigilante_id)

    patient = Patient(alias, name, age, enhanced, vigilante, doctor, treatment_notes, id)
    patient_repository.update(patient)
    return redirect('/patients')