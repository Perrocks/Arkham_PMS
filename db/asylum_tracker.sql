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

CREATE TABLE patient (
  id SERIAL PRIMARY KEY,
  alias VARCHAR(255),
  name VARCHAR(255),
  age VARCHAR(255),
  enhanced BOOLEAN,
  arrested_by VARCHAR(255),
  assigned_doctor VARCHAR(255),
  treatment_notes TEXT

);