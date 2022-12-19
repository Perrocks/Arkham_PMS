import pdb

from models.doctor import Doctor
from models.vigilante import Vigilante
from models.patient import Patient

import repositories.doctor_repository as doctor_repository
import repositories.vigilante_repository as vigilante_repository
import repositories.patient_repository as patient_repository

patient_repository.delete_all()
vigilante_repository.delete_all()
doctor_repository.delete_all()

vigilante1 = Vigilante('Batman', 'Vigilante')
vigilante_repository.save(vigilante1)

vigilante2 = Vigilante('James Gorden', 'GCPD')
vigilante_repository.save(vigilante2)

doctor1 = Doctor('Joan Leland')
doctor_repository.save(doctor1)

doctor2 = Doctor('Harleen Quinzel')
doctor_repository.save(doctor2)

patient1 = Patient('Joker', 'Unknown', 'Unknown', False, vigilante1, doctor2, 'asdafafaasd')
patient_repository.save(patient1)

patient2 = Patient('Scarecrow', 'Jonathan Crane', '33', False, vigilante2, doctor1, 'asdafafaasd')
patient_repository.save(patient2)


pdb.set_trace()