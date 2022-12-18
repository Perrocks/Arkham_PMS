from flask import Flask, render_template

from controllers.patient_controller import patient_blueprint
from controllers.doctor_controller import doctor_blueprint
from controllers.vigilante_controller import vigilante_blueprint

app = Flask(__name__)

app.register_blueprint(patient_blueprint)
app.register_blueprint(doctor_blueprint)
app.register_blueprint(vigilante_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)