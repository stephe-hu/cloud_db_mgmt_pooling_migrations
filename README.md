# cloud_db_mgmt_pooling_migrations

## Setup and configuration of connection pooling for Azure and GCP databases
### Azure:
1. Create a new Azure database instance using the following configurations: 
+ Compute + Storage: 
    + ```Compute tier: Burstable (1-20 vCores)``` 
    + ```Compute size: Standard_B1s (1 vCore, 1GiB memory, 400 max iops) ```
+ Networking:
    + Add Firewall rule: ```0.0.0.0 - 255.255.255.255```. 
2. Go to Server parameters and set the following configurations:
+ ```max_connections```: 20
+ ```connect_timeout```: 3

### GCP:
1. Create a new GCP database instance using the following configurations:
+ Cloud SQL Edition: 
    + ```Enterprise```
    + ```Sandbox```
+ Machine configuration: ```Shared core```
2. Go to Connections and add network ```0.0.0.0/0```

## Database schema structure
### My first table is the patients table with the patient_id as the PK. My second table is the doctors table with the doctor_id as the PK. My third table is the medical_records table with the medical_record_id as the PK and the patient_id and doctor_id as the FKs. This schema helps me to associate each medical record to the patient and doctor that it belongs to.

## Steps and challenges encountered during the database migration process
### Steps:
1. Alembic init migrations
``` 
alembic init migrations 
```

2. Edit alembic.ini to point to your database
``` 
sqlalchemy.url = mysql+mysqlconnector://username:password@host/database_name 
```

3. Edit env.py to point to your models
```
from db_schema import Base
target_metadata = Base.metadata 
```

4. Create a migration
``` 
alembic revision --autogenerate -m "create tables"
```

5. Run the migration
``` 
alembic upgrade head 
```

6. 
See history of migrations
```
alembic history
```
See the raw SQL that will be executed
```
alembic upgrade head --sql
``` 
Save the history of migrations
``` 
alembic upgrade head --sql > migration.sql 
```
7. Check the database
8. 
Revert the database schema to a previous migration version
```
alembic downgrade <target_revision>
```

Roll back to the previous migration version
```
alembic downgrade -1
```

### Challenges:
I did not encounter any challenges during the database migration process.