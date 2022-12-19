from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.vigilante import Vigilante

import repositories.vigilante_repository as vigilante_repository
import repositories.patient_repository as patient_repository

vigilantes_blueprint = Blueprint("vigilantes", __name__)

@vigilantes_blueprint.route("/vigilantes")
def select_all_vigilantes():
    vigilantes = vigilante_repository.select_all()
    return render_template("vigilantes/index.html", vigilantes = vigilantes)

@vigilantes_blueprint.route("/vigilantes/<id>")
def select_vigilante(id):
    vigilante = vigilante_repository.select(id)
    patients = patient_repository.patients_by_vigilante(vigilante)
    return render_template("vigilantes/show.html", vigilante=vigilante, patients=patients)

@vigilantes_blueprint.route("/vigilantes/<id>/delete", methods=['POST'])
def delete_vigilante(id):
    vigilante_repository.delete(id)
    return redirect('/vigilantes')


@vigilantes_blueprint.route("/vigilantes",  methods=['POST'])
def create_vigilante():
    name = request.form['name']
    type = request.form['type']
    vigilante = Vigilante(name, type)
    vigilante_repository.save(vigilante)
    return redirect('/vigilantes')

@vigilantes_blueprint.route("/vigilantes/new", methods=['GET'])
def new_vigilante():
    vigilantes = vigilante_repository.select_all()
    return render_template("vigilantes/new.html", vigilantes = vigilantes)