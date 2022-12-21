from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.vigilante import Vigilante

import repositories.vigilante_repository as vigilante_repository
import repositories.patient_repository as patient_repository

vigilantes_blueprint = Blueprint("vigilantes", __name__)

# Displays a list of vigilantes
# ---------------------------------
@vigilantes_blueprint.route("/vigilantes")
def select_all_vigilantes():
    vigilantes = vigilante_repository.select_all()
    return render_template("vigilantes/index.html", vigilantes = vigilantes)

# Displays the details of one vigilante
# ---------------------------------
@vigilantes_blueprint.route("/vigilantes/<id>")
def select_vigilante(id):
    vigilante = vigilante_repository.select(id)
    patients = patient_repository.patients_by_vigilante(vigilante)
    return render_template("vigilantes/show.html", vigilante=vigilante, patients=patients)

# Deletes selected vigilante
# ---------------------------------
@vigilantes_blueprint.route("/vigilantes/<id>/delete", methods=['POST'])
def delete_vigilante(id):
    vigilante_repository.delete(id)
    return redirect('/vigilantes')

# Allows user to save a new patient to the database
# ---------------------------------
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

# Allows user to update details of selected vigilante
# ---------------------------------
@vigilantes_blueprint.route("/vigilantes/<id>", methods=['POST'])
def update_vigilante(id):
    name = request.form['name']
    type = request.form['type']

    vigilante = Vigilante(name, type, id)
    
    vigilante_repository.update(vigilante)
    return redirect('/vigilantes')

@vigilantes_blueprint.route("/vigilantes/<id>/edit", methods=['GET'])
def edit_vigilante(id):
    vigilante = vigilante_repository.select(id)
    patients = patient_repository.select_all()
    return render_template("vigilantes/edit.html", patients = patients, vigilante = vigilante)

# Just for fun
# ---------------------------------
@vigilantes_blueprint.route("/thebat", methods=['GET'])
def the_bat():
    return render_template("thebat.html")