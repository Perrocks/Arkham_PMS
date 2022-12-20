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

notes = " My most challenging patient at Arkham. The Joker's derangement defies easy class. His rapidly changing mood swings hint at borderline personality disorder, but he has no trace of associated identity problems. He also displays signs of deep narcissism, but nonetheless he has a well-developed sense of others, as his ability to manipulate everyone from orderlies to doctors in Arkham is extraordinarily well-developed; he also shows all the signs of a highly functioning sufferer of antisocial personality. At times I actually wonder if he is actually insane at all. Additional notes: His criminal record makes clear that he is an unrepentant homicidal maniac. He is extremely manipulative; the file detailing Harley Quinn's associations with him is fascinating reading. It's unfortunate I was not on staff at the time to witness his seduction of her firsthand. His past is unknown, and his answers to me about it are wildly inconsistent and frequently fantastical."

vigilante1 = Vigilante('Batman', 'Vigilante')
vigilante_repository.save(vigilante1)

vigilante2 = Vigilante('James Gorden', 'GCPD')
vigilante_repository.save(vigilante2)

doctor1 = Doctor('Joan Leland')
doctor_repository.save(doctor1)

doctor2 = Doctor('Harleen Quinzel')
doctor_repository.save(doctor2)

patient1 = Patient('Joker', 'Unknown', 'Unknown', False, vigilante1, doctor2, notes)
patient_repository.save(patient1)

patient2 = Patient('Scarecrow', 'Jonathan Crane', '33', False, vigilante2, doctor1, 'asdafafaasd')
patient_repository.save(patient2)


pdb.set_trace()