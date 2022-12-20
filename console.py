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

notes = " MY MOST CHALLENGING PATIENT AT ARKHAM. THE JOKER'S DERANGEMENT DEFIES EASY CLASS. HIS RAPIDLY CHANGING MOOD SWINGS HINT AT BORDERLINE PERSONALITY DISORDER, BUT HE HAS NO TRACE OF ASSOCIATED IDENTITY PROBLEMS. HE ALSO DISPLAYS SIGNS OF DEEP NARCISSISM, BUT NONETHELESS HE HAS A WELL-DEVELOPED SENSE OF OTHERS, AS HIS ABILITY TO MANIPULATE EVERYONE FROM ORDERLIES TO DOCTORS IN ARKHAM IS EXTRAORDINARILY WELL-DEVELOPED; HE ALSO SHOWS ALL THE SIGNS OF A HIGHLY FUNCTIONING SUFFERER OF ANTISOCIAL PERSONALITY. AT TIMES I ACTUALLY WONDER IF HE IS ACTUALLY INSANE AT ALL. ADDITIONAL NOTES: HIS CRIMINAL RECORD MAKES CLEAR THAT HE IS AN UNREPENTANT HOMICIDAL MANIAC. HE IS EXTREMELY MANIPULATIVE; THE FILE DETAILING HARLEY QUINN'S ASSOCIATIONS WITH HIM IS FASCINATING READING. IT'S UNFORTUNATE I WAS NOT ON STAFF AT THE TIME TO WITNESS HIS SEDUCTION OF HER FIRSTHAND. HIS PAST IS UNKNOWN, AND HIS ANSWERS TO ME ABOUT IT ARE WILDLY INCONSISTENT AND FREQUENTLY FANTASTICAL."

vigilante1 = Vigilante('BATMAN', 'VIGILANTE')
vigilante_repository.save(vigilante1)

vigilante2 = Vigilante('JAMES GORDEN', 'GCPD')
vigilante_repository.save(vigilante2)

doctor1 = Doctor('JOAN LELAND')
doctor_repository.save(doctor1)

doctor2 = Doctor('HARLEEN QUINZEL')
doctor_repository.save(doctor2)

patient1 = Patient('JOKER', 'UNKNOWN', 'UNKNOWN', False, vigilante1, doctor2, notes)
patient_repository.save(patient1)

patient2 = Patient('SCARECROW', 'JONATHAN CRANE', '33', False, vigilante2, doctor1, 'NOTES')
patient_repository.save(patient2)


pdb.set_trace()