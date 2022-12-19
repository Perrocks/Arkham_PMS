DROP TABLE patients;
DROP TABLE doctors;
DROP TABLE vigilantes;

CREATE TABLE vigilantes (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  type VARCHAR(255)
);

CREATE TABLE doctors (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE patients (
  id SERIAL PRIMARY KEY,
  alias VARCHAR(255),
  name VARCHAR(255),
  age VARCHAR(255),
  enhanced BOOLEAN,
  vigilante_id INT NOT NULL REFERENCES vigilantes(id) ON DELETE CASCADE,
  doctor_id INT NOT NULL REFERENCES doctors(id) ON DELETE CASCADE,
  treatment_notes TEXT

);