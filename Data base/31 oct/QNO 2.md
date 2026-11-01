QNO 2:-



A hospital wants to store patient records and their assigned doctors. If a doctor leaves, all related patient records should be deleted.



Tasks:

Create a Doctors table:





DoctorID (PRIMARY KEY, AUTO\_INCREMENT)

DoctorName (NOT NULL)

Specialization (NOT NULL, UNIQUE)

|create table Doctors\_31oct(DrID int primary key auto\_increment,drname varchar(50) not null, Specialization varchar (50) not null unique );<br />Query OK, 0 rows affected (0.07 sec)|
|-|



Create a Patients table:



PatientID (PRIMARY KEY, AUTO\_INCREMENT)

PatientName (NOT NULL)

DoctorID (FOREIGN KEY)

| create table Patients\_31oct(PatientID int PRIMARY KEy auto\_increment ,PatientName varchar (30) not null , DrID int not null , foreign key (drid) references Doctors\_31oct(drid) on delete cascade );<br />Query OK, 0 rows affected (0.07 sec)<br />|
|-|



Insert sample data (at least 3 doctors and 5 patients).



Delete a doctor and check if related patients are removed automatically.

|<br />mysql> select \* from Doctors\_31oct;<br />+------+------------+----------------+<br />\| DrID \| drname     \| Specialization \|<br />+------+------------+----------------+<br />\|    2 \| Neha Verma \| Neurology      \|<br />\|    3 \| Raj Patel  \| Dermatology    \|<br />+------+------------+----------------+<br />2 rows in set (0.00 sec)<br /><br />mysql> select \* from Patients\_31oct;<br />+-----------+-------------+------+<br />\| PatientID \| PatientName \| DrID \|<br />+-----------+-------------+------+<br />\|         3 \| Riya        \|    2 \|<br />\|         4 \| Karan       \|    2 \|<br />\|         5 \| Nitin       \|    3 \|<br />+-----------+-------------+------|
|-|





Update a patient’s doctor to a new doctor.

| update Patients\_31oct  set drid=3 where PatientID=2;<br />Query OK, 0 rows affected (0.00 sec)<br />Rows matched: 0  Changed: 0  Warnings: 0<br /><br />mysql>|
|-|



