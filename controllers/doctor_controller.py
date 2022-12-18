from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.doctor import Doctor

import repositories.doctor_repository as doctor_repository
import repositories.patient_repository as patient_repository

doctors_blueprint = Blueprint("doctors", __name__)

@doctors_blueprint.route("/doctors")
def select_all_doctors():
    doctors = doctor_repository.select_all()
    return render_template("doctors/index.html", doctors = doctors)

@doctors_blueprint.route("/doctors/<id>")
def select_doctor(id):
    doctor = doctor_repository.select(id)
    patients = patient_repository.patients_by_doctor(doctor)
    return render_template("doctors/show.html", doctor=doctor, patients=patients)

@doctors_blueprint.route("/doctors/<id>/delete", methods=['POST'])
def delete_doctor(id):
    doctor_repository.delete(id)
    return redirect('/doctors')

@doctors_blueprint.route("/patient",  methods=['POST'])
def create_doctor():
    name = request.form['name']
    doctor = Doctor(name)
    doctor_repository.save(doctor)
    return redirect('/doctors')