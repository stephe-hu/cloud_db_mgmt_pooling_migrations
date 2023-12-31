CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 9b38f5eea7c4

INSERT INTO alembic_version (version_num) VALUES ('9b38f5eea7c4');

-- Running upgrade 9b38f5eea7c4 -> 582986bdf07b

ALTER TABLE medical_records ADD COLUMN doctor_id INTEGER NOT NULL;

ALTER TABLE medical_records ADD FOREIGN KEY(doctor_id) REFERENCES doctors (id);

UPDATE alembic_version SET version_num='582986bdf07b' WHERE alembic_version.version_num = '9b38f5eea7c4';

