2\.



Create a table Patients with:



PatientID (INT, Primary Key)

PatientName (VARCHAR(50), NOT NULL)

Age (INT, should be between 1 and 100)

AdmissionStatus (VARCHAR(15), should be 'Admitted' or 'Discharged', DEFAULT 'Admitted')

TreatmentCost (DECIMAL(10,2), should be at least 1000)

Insert records and check constraints:



(201, 'Michael', 25, 'Admitted', 5000)

(202, 'Linda', 105, 'Admitted', 8000) (Should fail due to Age constraint)

(203, 'David', 40, DEFAULT, 1200) (Should insert 'Admitted' as default)

(204, 'Sarah', 30, 'Discharged', 700) (Should fail due to TreatmentCost constraint)

|create table Patients (PatientID INT Primary Key,PatientName VARCHAR(50) NOT NULL, age int,AdmissionStatus VARCHAR(15) default "admitted",TreatmentCost decimal (10,2) ,check ( Age between 1 and 100 and AdmissionStatus IN ('Admitted', 'Discharged') AND TreatmentCost >= 1000))  ;<br />Query OK, 0 rows affected (0.02 sec)<br /><br /><br />mysql> insert into patients values(201, 'Michael', 25, 'Admitted', 5000)<br />    -> ;<br />Query OK, 1 row affected (0.01 sec)<br /><br />mysql> SELECT \* FROM patients;<br />+-----------+-------------+------+-----------------+---------------+<br />\| PatientID \| PatientName \| age  \| AdmissionStatus \| TreatmentCost \|<br />+-----------+-------------+------+-----------------+---------------+<br />\|       201 \| Michael     \|   25 \| Admitted        \|       5000.00 \|<br />+-----------+-------------+------+-----------------+---------------+<br />1 row in set (0.00 sec)<br /><br />mysql> insert into patients values (202, 'Linda', 105, 'Admitted', 8000);<br />ERROR 3819 (HY000): Check constraint 'patients\_chk\_1' is violated.<br />mysql> insert into patients values (203, 'David', 40, DEFAULT, 1200);<br />Query OK, 1 row affected (0.01 sec)<br /><br />mysql> insert into patients values (204, 'Sarah', 30, 'Discharged', 700);<br />ERROR 3819 (HY000): Check constraint 'patients\_chk\_1' is violated.<br />mysql><br /><br />|
|-|



