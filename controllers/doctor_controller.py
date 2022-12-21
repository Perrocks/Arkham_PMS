from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.doctor import Doctor

import repositories.doctor_repository as doctor_repository
import repositories.patient_repository as patient_repository

doctors_blueprint = Blueprint("doctors", __name__)

# Displays a list of doctors
# ---------------------------------
@doctors_blueprint.route("/doctors")
def select_all_doctors():
    doctors = doctor_repository.select_all()
    return render_template("doctors/index.html", doctors = doctors)

# Displays the details of one doctor
# ---------------------------------
@doctors_blueprint.route("/doctors/<id>")
def select_doctor(id):
    doctor = doctor_repository.select(id)
    patients = patient_repository.patients_by_doctor(doctor)
    return render_template("doctors/show.html", doctor=doctor, patients=patients)

# Deletes selected doctor
# ---------------------------------
@doctors_blueprint.route("/doctors/<id>/delete", methods=['POST'])
def delete_doctor(id):
    doctor_repository.delete(id)
    return redirect('/doctors')

# Allows user to save a new doctor to the database
# ---------------------------------
@doctors_blueprint.route("/doctors",  methods=['POST'])
def create_doctor():
    name = request.form['name']
    doctor = Doctor(name)
    doctor_repository.save(doctor)
    return redirect('/doctors')

@doctors_blueprint.route("/doctors/new", methods=['GET'])
def new_doctor():
    doctors = doctor_repository.select_all()
    return render_template("doctors/new.html", doctors = doctors)

# Allows user to update details of selected doctor
# ---------------------------------
@doctors_blueprint.route("/doctors/<id>", methods=['POST'])
def update_doctor(id):
    name = request.form['name']

    doctor = Doctor(name, id)
    
    doctor_repository.update(doctor)
    return redirect('/doctors')

@doctors_blueprint.route("/doctors/<id>/edit", methods=['GET'])
def edit_doctor(id):
    doctor = doctor_repository.select(id)
    patients = patient_repository.select_all()
    return render_template("doctors/edit.html", patients = patients, doctor = doctor)