class Patient:

    def __init__(self, alias, name, age, enhanced, arrested_by, assigned_doctor, treatment_notes, id = None):
      self.alias = alias
      self.name = name
      self.age = age
      self.enhanced = enhanced
      self.arrested_by = arrested_by
      self.assigned_doctor = assigned_doctor
      self.treatment_notes = treatment_notes
      self.id = id