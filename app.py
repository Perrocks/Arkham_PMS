from flask import Flask, render_template

from controllers.patient_controller import patients_blueprint
from controllers.doctor_controller import doctors_blueprint
from controllers.vigilante_controller import vigilantes_blueprint

app = Flask(__name__)

app.register_blueprint(patients_blueprint)
app.register_blueprint(doctors_blueprint)
app.register_blueprint(vigilantes_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)