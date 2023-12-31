CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> f6ef26746327

ALTER TABLE medical_records ADD COLUMN doctor_id INTEGER NOT NULL;

ALTER TABLE medical_records ADD FOREIGN KEY(doctor_id) REFERENCES doctors (id);

ALTER TABLE patients MODIFY contact_number VARCHAR(100) NULL;

INSERT INTO alembic_version (version_num) VALUES ('f6ef26746327');

