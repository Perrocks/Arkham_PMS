from db.run_sql import run_sql

from models.vigilante import Vigilante
from models.patient import Patient


# Save new vigilante to the database
def save(vigilante):
    sql = "INSERT INTO vigilantes(name, type) VALUES ( %s, %s ) RETURNING id"
    values = [vigilante.name, vigilante.type]
    results = run_sql( sql, values )
    vigilante.id = results[0]['id']
    return vigilante


# Select all saved vigilantes from database and return
def select_all():
    vigilantes = []

    sql = "SELECT * FROM vigilantes"
    results = run_sql(sql)

    for row in results:
        vigilante = Vigilante(row['name'], row['type'], row['id'])
        vigilantes.append(vigilante)
    return vigilantes


# Select one vigilante from the database and return
def select(id):
    vigilante = None

    sql = "SELECT * FROM vigilantes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        vigilante = Vigilante(result['name'], result['type'], result['id'] )
    return vigilante

# Delete all from vigilantes table
def delete_all():
    sql = "DELETE FROM vigilantes"
    run_sql(sql)

# Delete one vigilante from table
def delete(id):
    sql = "DELETE  FROM vigilantes WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# Update the details of selected vigilante
def update(vigilante):
    sql = "UPDATE vigilantes SET (name, type) =(%s, %s) WHERE id = %s"

    values = [vigilante.name, vigilante.type, vigilante.id]
    
    run_sql( sql, values )