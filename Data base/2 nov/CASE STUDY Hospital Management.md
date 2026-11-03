CASE STUDY: Hospital Management \& Appointment System





============================================================

1\. BUSINESS SCENARIO

============================================================



A private hospital wants to develop a MySQL database to manage its daily operations.



The hospital has departments, doctors, patients, appointments, prescriptions and

medicines.



A patient can visit the hospital multiple times. Every visit is recorded as an

appointment between a patient and a doctor.



Each doctor belongs to a department.



After an appointment, the doctor may create a prescription. A prescription can

contain multiple medicines.



The hospital also wants the database to maintain historical records wherever

required.



Your task is to analyze the business requirements and design the database.





============================================================

2\. DEPARTMENT DATA

============================================================



department\_id | department\_name | floor\_no

\------------------------------------------------

101           | Cardiology       | 3

102           | Neurology        | 4

103           | Orthopedics      | 2

104           | Dermatology      | 1

|**create table department(department\_id int primary key,department\_name varchar(30) not null unique ,floor\_no int not null unique );<br /><br /><br /> select \* from department;<br />+---------------+-----------------+----------+<br />\| department\_id \| department\_name \| floor\_no \|<br />+---------------+-----------------+----------+<br />\|           101 \| Cardiology      \|        3 \|<br />\|           102 \| Neurology       \|        4 \|<br />\|           103 \| Orthopedics     \|        2 \|<br />\|           104 \| Dermatology     \|        1 \|<br />+---------------+-----------------+----------+<br />4 rows in set (0.00 sec)**|
|-|





============================================================

3\. DOCTOR DATA

============================================================



doctor\_id | doctor\_name      | specialization | department\_id

\----------------------------------------------------------------

201       | Dr. Rajesh Sharma| Cardiologist   | 101

202       | Dr. Neha Verma   | Neurologist    | 102

203       | Dr. Amit Jain    | Orthopedic     | 103

204       | Dr. Priya Singh  | Dermatologist  | 104

205       | Dr. Karan Mehta  | Cardiologist   | 101

|**create table doctor(doctor\_id int primary key ,doctor\_name varchar(30) not null unique,specialization varchar(30) not null ,department\_id int ,foreign key (department\_id) references department(department\_id) on delete set null ON UPDATE CASCADE);<br />Query OK, 0 rows affected (0.07 sec)<br /><br /> select \* from doctor;<br />+-----------+-------------------+----------------+---------------+<br />\| doctor\_id \| doctor\_name       \| specialization \| department\_id \|<br />+-----------+-------------------+----------------+---------------+<br />\|       201 \| Dr. Rajesh Sharma \| Cardiologist   \|           101 \|<br />\|       202 \| Dr. Neha Verma    \| Neurologist    \|           102 \|<br />\|       203 \| Dr. Amit Jain     \| Orthopedic     \|           103 \|<br />\|       204 \| Dr. Priya Singh   \| Dermatologist  \|           104 \|<br />\|       205 \| Dr. Karan Mehta   \| Cardiologist   \|           101 \|<br />+-----------+-------------------+----------------+---------------+<br />5 rows in set (0.00 sec)**|
|-|





============================================================

4\. PATIENT DATA

============================================================



patient\_id | patient\_name  | gender | city

\------------------------------------------------

301        | Rahul Verma   | Male   | Indore

302        | Sneha Sharma  | Female | Bhopal

303        | Amit Patel    | Male   | Indore

304        | Pooja Gupta   | Female | Ujjain

305        | Rohan Jain    | Male   | Dewas

306        | Neha Patel    | Female | Indore



|**create table PATIENT(patient\_id int primary key, patient\_name varchar(30) not null ,gender enum ("male","female","others") not null, city varchar(30) not null);<br />Query OK, 0 rows affected (0.03 sec)<br /> select \* from PATIENT;<br />+------------+--------------+--------+--------+<br />\| patient\_id \| patient\_name \| gender \| city   \|<br />+------------+--------------+--------+--------+<br />\|        301 \| Rahul Verma  \| male   \| Indore \|<br />\|        302 \| Sneha Sharma \| female \| Bhopal \|<br />\|        303 \| Amit Patel   \| male   \| Indore \|<br />\|        304 \| Pooja Gupta  \| female \| Ujjain \|<br />\|        305 \| Rohan Jain   \| male   \| Dewas  \|<br />\|        306 \| Neha Patel   \| female \| Indore \|<br />+------------+--------------+--------+--------+<br />6 rows in set (0.00 sec)<br />**|
|-|



============================================================

5\. MEDICINE DATA

============================================================



medicine\_id | medicine\_name | manufacturer       | price

\----------------------------------------------------------

401         | Paracetamol   | ABC Pharma         | 30

402         | Azithromycin  | XYZ Pharma         | 120

403         | Pantoprazole  | MedLife            | 80

404         | Amoxicillin   | HealthCare Pharma  | 150

405         | Ibuprofen     | ABC Pharma         | 60

406         | Cetirizine    | MedLife            | 45



|**create table MEDICINE(medicine\_id int primary key ,medicine\_name varchar(30) not null unique,manufacturer varchar(40) not null , price decimal (10,2) not null);<br />Query OK, 0 rows affected (0.07 sec)<br /> SELECT \* FROM MEDICINE;<br />+-------------+---------------+-------------------+--------+<br />\| medicine\_id \| medicine\_name \| manufacturer      \| price  \|<br />+-------------+---------------+-------------------+--------+<br />\|         401 \| Paracetamol   \| ABC Pharma        \|  30.00 \|<br />\|         402 \| Azithromycin  \| XYZ Pharma        \| 120.00 \|<br />\|         403 \| Pantoprazole  \| MedLife           \|  80.00 \|<br />\|         404 \| Amoxicillin   \| HealthCare Pharma \| 150.00 \|<br />\|         405 \| Ibuprofen     \| ABC Pharma        \|  60.00 \|<br />\|         406 \| Cetirizine    \| MedLife           \|  45.00 \|<br />+-------------+---------------+-------------------+--------+<br />6 rows in set (0.00 sec)<br /><br />**|
|-|



============================================================

6\. APPOINTMENT

============================================================



The hospital wants to maintain appointment information.



Each appointment belongs to:

\- One patient

\- One doctor

\- One department



Therefore, the APPOINTMENT table will contain MULTIPLE FOREIGN KEYS.



Required columns:



appointment\_id

appointment\_date

appointment\_time

patient\_id

doctor\_id

department\_id

status





The following data must be inserted:



appointment\_id | date       | time  | patient\_id | doctor\_id | department\_id | status

\---------------------------------------------------------------------------------------

501             | 2026-09-01 | 10:00 | 301        | 201       | 101           | Completed

502             | 2026-09-01 | 11:00 | 302        | 202       | 102           | Completed

503             | 2026-09-02 | 09:30 | 303        | 203       | 103           | Completed

504             | 2026-09-02 | 12:00 | 304        | 204       | 104           | Cancelled

505             | 2026-09-03 | 10:30 | 301        | 205       | 101           | Completed

506             | 2026-09-03 | 11:30 | 305        | 203       | 103           | Completed

507             | 2026-09-04 | 09:00 | 306        | 201       | 101           | Scheduled

508             | 2026-09-04 | 14:00 | 302        | 202       | 102           | Scheduled



|**create table APPOINTMENT(appointment\_id int primary key ,appointment\_date date not null,appointment\_time time not null,patient\_id int ,doctor\_id int,department\_id int ,status enum("Completed",'Scheduled','Cancelled'),foreign key (patient\_id) references patient(patient\_id) on delete cascade,foreign key (doctor\_id) references doctor(doctor\_id) on delete set null,foreign key(department\_id) references department(department\_id) on delete set null on update cascade);<br />Query OK, 0 rows affected (0.44 sec)<br /><br />SELECT \* FROM APPOINTMENT;<br />+----------------+------------------+------------------+------------+-----------+---------------+-----------+<br />\| appointment\_id \| appointment\_date \| appointment\_time \| patient\_id \| doctor\_id \| department\_id \| status    \|<br />+----------------+------------------+------------------+------------+-----------+---------------+-----------+<br />\|            501 \| 2026-09-01       \| 10:00:00         \|        301 \|       201 \|           101 \| Completed \|<br />\|            502 \| 2026-09-01       \| 11:00:00         \|        302 \|       202 \|           102 \| Completed \|<br />\|            503 \| 2026-09-02       \| 09:30:00         \|        303 \|       203 \|           103 \| Completed \|<br />\|            504 \| 2026-09-02       \| 12:00:00         \|        304 \|       204 \|           104 \| Cancelled \|<br />\|            505 \| 2026-09-03       \| 10:30:00         \|        301 \|       205 \|           101 \| Completed \|<br />\|            506 \| 2026-09-03       \| 11:30:00         \|        305 \|       203 \|           103 \| Completed \|<br />\|            507 \| 2026-09-04       \| 09:00:00         \|        306 \|       201 \|           101 \| Scheduled \|<br />\|            508 \| 2026-09-04       \| 14:00:00         \|        302 \|       202 \|           102 \| Scheduled \|<br />+----------------+------------------+------------------+------------+-----------+---------------+-----------+<br />8 rows in set (0.00 sec)<br />**|
|-|



============================================================

7\. PRESCRIPTION

============================================================



After an appointment, a doctor can create a prescription.



Each prescription belongs to:

\- One appointment

\- One patient

\- One doctor



Required columns:



prescription\_id

prescription\_date

appointment\_id

patient\_id

doctor\_id

remarks





Data:



prescription\_id | date       | appointment\_id | patient\_id | doctor\_id | remarks

\--------------------------------------------------------------------------------

601             | 2026-09-01 | 501            | 301        | 201       | BP observation

602             | 2026-09-01 | 502            | 302        | 202       | Migraine treatment

603             | 2026-09-02 | 503            | 303        | 203       | Knee pain

604             | 2026-09-03 | 505            | 301        | 205       | Heart checkup

605             | 2026-09-03 | 506            | 305        | 203       | Back pain



|**create table PRESCRIPTION(prescription\_id int primary key, PRESCRIPTION\_date date not null,appointment\_id int,patient\_id int, doctor\_id int,remarks varchar(30) not null,foreign key (appointment\_id) references APPOINTMENT(APPOINTMENT\_id) ON DELETE CASCADE,foreign key (patient\_id) references patient(patient\_id) , foreign key ( doctor\_id) references  doctor(doctor\_id) ON UPDATE SET NULL** ON DELETE SET NULL**);<br />Query OK, 0 rows affected (0.08 sec)<br /><br />SELECT \* FROM PRESCRIPTION;<br />+-----------------+-------------------+----------------+------------+-----------+--------------------+<br />\| prescription\_id \| PRESCRIPTION\_date \| appointment\_id \| patient\_id \| doctor\_id \| remarks            \|<br />+-----------------+-------------------+----------------+------------+-----------+--------------------+<br />\|             601 \| 2026-09-01        \|            501 \|        301 \|       201 \| BP observation     \|<br />\|             602 \| 2026-09-01        \|            502 \|        302 \|       202 \| Migraine treatment \|<br />\|             603 \| 2026-09-02        \|            503 \|        303 \|       203 \| Knee pain          \|<br />\|             604 \| 2026-09-03        \|            505 \|        301 \|       205 \| Heart checkup      \|<br />\|             605 \| 2026-09-03        \|            506 \|        305 \|       203 \| Back pain          \|<br />+-----------------+-------------------+----------------+------------+-----------+--------------------+<br />5 rows in set (0.00 sec)**|
|-|



============================================================

8\. PRESCRIPTION\_MEDICINE

============================================================



One prescription can contain multiple medicines.



One medicine can be used in multiple prescriptions.



Therefore, this is a MANY-TO-MANY relationship.



Create a bridge table:



prescription\_medicine



Required columns:



prescription\_id

medicine\_id

dosage

duration\_days

quantity



Use a COMPOSITE PRIMARY KEY:



PRIMARY KEY (prescription\_id, medicine\_id)





Data:



prescription\_id | medicine\_id | dosage | duration\_days | quantity

\-----------------------------------------------------------------

601             | 401         | 1-0-1  | 5             | 10

601             | 403         | 1-0-0  | 5             | 5

602             | 403         | 1-0-0  | 7             | 7

602             | 406         | 0-0-1  | 5             | 5

603             | 405         | 1-0-1  | 5             | 10

603             | 403         | 1-0-0  | 5             | 5

604             | 401         | 1-0-1  | 3             | 6

604             | 403         | 1-0-0  | 3             | 3

605             | 405         | 1-0-1  | 7             | 14



|**create table PRESCRIPTION\_MEDICINE(prescription\_id int ,medicine\_id int ,dosage varchar (20) not null,duration\_days int not null ,quantity int not null,primary key(prescription\_id, medicine\_id), foreign key(medicine\_id) references medicine(medicine\_id) ON DELETE RESTRICT,foreign key (prescription\_id) references prescription(prescription\_id) ON DELETE CASCADE);<br />Query OK, 0 rows affected (0.08 sec)<br /><br /><br /> select \* from PRESCRIPTION\_MEDICINE;<br />+-----------------+-------------+--------+---------------+----------+<br />\| prescription\_id \| medicine\_id \| dosage \| duration\_days \| quantity \|<br />+-----------------+-------------+--------+---------------+----------+<br />\|             601 \|         401 \| 1-0-1  \|             5 \|       10 \|<br />\|             601 \|         403 \| 1-0-0  \|             5 \|        5 \|<br />\|             602 \|         403 \| 1-0-0  \|             7 \|        7 \|<br />\|             602 \|         406 \| 0-0-1  \|             5 \|        5 \|<br />\|             603 \|         403 \| 1-0-0  \|             5 \|        5 \|<br />\|             603 \|         405 \| 1-0-1  \|             5 \|       10 \|<br />\|             604 \|         401 \| 1-0-1  \|             3 \|        6 \|<br />\|             604 \|         403 \| 1-0-0  \|             3 \|        3 \|<br />\|             605 \|         405 \| 1-0-1  \|             7 \|       14 \|<br />+-----------------+-------------+--------+---------------+----------+<br />9 rows in set (0.00 sec)**|
|-|



============================================================

9\. RELATIONSHIPS TO IDENTIFY

============================================================



Identify and implement the following relationships:



1\. Department -> Doctor



2\. Patient -> Appointment



3\. Doctor -> Appointment



4\. Department -> Appointment



5\. Appointment -> Prescription



6\. Patient -> Prescription



7\. Doctor -> Prescription



8\. Prescription -> Prescription\_Medicine



9\. Medicine -> Prescription\_Medicine





IMPORTANT:



Do not simply create the tables randomly.



Analyze which table is the PARENT and which table is the CHILD.





============================================================

10\. ON DELETE BUSINESS REQUIREMENTS

============================================================



You must choose the correct ON DELETE action based on the following

business scenarios.





SCENARIO A - DEPARTMENT CLOSED

\--------------------------------



Department 104 (Dermatology) is closed permanently.



However, doctors who worked in that department should NOT be deleted.



Their department\_id should become NULL.



Requirement:



Department -> Doctor



Use an appropriate ON DELETE action so that:



Doctor remains

department\_id becomes NULL

| **delete from department where department\_id=104;<br />Query OK, 1 row affected (0.04 sec)<br /><br /> select \* from doctor;<br />+-----------+-------------------+----------------+---------------+<br />\| doctor\_id \| doctor\_name       \| specialization \| department\_id \|<br />+-----------+-------------------+----------------+---------------+<br />\|       201 \| Dr. Rajesh Sharma \| Cardiologist   \|           101 \|<br />\|       202 \| Dr. Neha Verma    \| Neurologist    \|           102 \|<br />\|       203 \| Dr. Amit Jain     \| Orthopedic     \|           103 \|<br />\|       204 \| Dr. Priya Singh   \| Dermatologist  \|          NULL \|<br />\|       205 \| Dr. Karan Mehta   \| Cardiologist   \|           101 \|<br />+-----------+-------------------+----------------+---------------+<br />5 rows in set (0.00 sec)<br />**|
|-|





SCENARIO B - DOCTOR LEAVES THE HOSPITAL

\-----------------------------------------



Doctor 203 leaves the hospital.



The hospital wants to retain historical appointment records.



Therefore, deleting the doctor must NOT delete the appointments.



The doctor reference in existing appointments should become NULL.



Requirement:



Doctor -> Appointment



Use:



ON DELETE SET NULL

|**delete from doctor where doctor\_id=203;  <br /><br /><br /> select \* from Appointment;<br />+----------------+------------------+------------------+------------+-----------+---------------+-----------+<br />\| appointment\_id \| appointment\_date \| appointment\_time \| patient\_id \| doctor\_id \| department\_id \| status    \|<br />+----------------+------------------+------------------+------------+-----------+---------------+-----------+<br />\|            501 \| 2026-09-01       \| 10:00:00         \|        301 \|       201 \|           101 \| Completed \|<br />\|            502 \| 2026-09-01       \| 11:00:00         \|        302 \|       202 \|           102 \| Completed \|<br />\|            503 \| 2026-09-02       \| 09:30:00         \|        303 \|      NULL \|           103 \| Completed \|<br />\|            504 \| 2026-09-02       \| 12:00:00         \|        304 \|       204 \|          NULL \| Cancelled \|<br />\|            505 \| 2026-09-03       \| 10:30:00         \|        301 \|       205 \|           101 \| Completed \|<br />\|            506 \| 2026-09-03       \| 11:30:00         \|        305 \|      NULL \|           103 \| Completed \|<br />\|            507 \| 2026-09-04       \| 09:00:00         \|        306 \|       201 \|           101 \| Scheduled \|<br />\|            508 \| 2026-09-04       \| 14:00:00         \|        302 \|       202 \|           102 \| Scheduled \|<br />+----------------+------------------+------------------+------------+-----------+---------------+-----------+<br />8 rows in set (0.00 sec)<br /><br />**|
|-|





SCENARIO C - TEST PATIENT IS DELETED

\-------------------------------------



Patient 306 is test/demo data and management wants to permanently

remove this patient.



Appointments belonging to this test patient should also be removed.



Requirement:



Patient -> Appointment



Use:



ON DELETE CASCADE



|**DELETE FROM PATIENT WHERE PATIENT\_ID=306;<br />Query OK, 1 row affected (0.01 sec)<br /><br />mysql> select \* from Appointment;<br />+----------------+------------------+------------------+------------+-----------+---------------+-----------+<br />\| appointment\_id \| appointment\_date \| appointment\_time \| patient\_id \| doctor\_id \| department\_id \| status    \|<br />+----------------+------------------+------------------+------------+-----------+---------------+-----------+<br />\|            501 \| 2026-09-01       \| 10:00:00         \|        301 \|       201 \|           101 \| Completed \|<br />\|            502 \| 2026-09-01       \| 11:00:00         \|        302 \|       202 \|           102 \| Completed \|<br />\|            503 \| 2026-09-02       \| 09:30:00         \|        303 \|      NULL \|           103 \| Completed \|<br />\|            504 \| 2026-09-02       \| 12:00:00         \|        304 \|       204 \|          NULL \| Cancelled \|<br />\|            505 \| 2026-09-03       \| 10:30:00         \|        301 \|       205 \|           101 \| Completed \|<br />\|            506 \| 2026-09-03       \| 11:30:00         \|        305 \|      NULL \|           103 \| Completed \|<br />\|            508 \| 2026-09-04       \| 14:00:00         \|        302 \|       202 \|           102 \| Scheduled \|<br />+----------------+------------------+------------------+------------+-----------+---------------+-----------+<br />7 rows in set (0.00 sec)**|
|-|



SCENARIO D - APPOINTMENT IS DELETED

\------------------------------------



Appointment 501 is removed from the system.



Any prescription created specifically for that appointment should

also be removed.



Requirement:



Appointment -> Prescription



Use:



ON DELETE CASCADE

|**DELETE FROM APPOINTMENT WHERE APPOINTMENT\_ID =501;<br />Query OK, 1 row affected (0.01 sec)<br /><br />mysql> select \* from Prescription;
<br />+-----------------+-------------------+----------------+------------+-----------+--------------------+<br />\| prescription\_id \| PRESCRIPTION\_date \| appointment\_id \| patient\_id \| doctor\_id \| remarks            \|<br />+-----------------+-------------------+----------------+------------+-----------+--------------------+<br />\|             602 \| 2026-09-01        \|            502 \|        302 \|       202 \| Migraine treatment \|<br />\|             603 \| 2026-09-02        \|            503 \|        303 \|      NULL \| Knee pain          \|<br />\|             604 \| 2026-09-03        \|            505 \|        301 \|       205 \| Heart checkup      \|<br />\|             605 \| 2026-09-03        \|            506 \|        305 \|      NULL \| Back pain          \|<br />+-----------------+-------------------+----------------+------------+-----------+--------------------+<br />4 rows in set (0.00 sec)<br />**|
|-|





SCENARIO E - PRESCRIPTION IS DELETED

\-------------------------------------



Prescription 601 is deleted.



Its records from prescription\_medicine should automatically be removed.



Requirement:



Prescription -> Prescription\_Medicine



Use:



ON DELETE CASCADE

|**DELETE FROM PRESCRIPTION WHERE PRESCRIPTION\_ID=601;<br />Query OK, 0 rows affected (0.00 sec)<br /><br />mysql> select \* from Prescription\_medicine;<br />+-----------------+-------------+--------+---------------+----------+<br />\| prescription\_id \| medicine\_id \| dosage \| duration\_days \| quantity \|<br />+-----------------+-------------+--------+---------------+----------+<br />\|             602 \|         403 \| 1-0-0  \|             7 \|        7 \|<br />\|             602 \|         406 \| 0-0-1  \|             5 \|        5 \|<br />\|             603 \|         403 \| 1-0-0  \|             5 \|        5 \|<br />\|             603 \|         405 \| 1-0-1  \|             5 \|       10 \|<br />\|             604 \|         401 \| 1-0-1  \|             3 \|        6 \|<br />\|             604 \|         403 \| 1-0-0  \|             3 \|        3 \|<br />\|             605 \|         405 \| 1-0-1  \|             7 \|       14 \|<br />+-----------------+-------------+--------+---------------+----------+<br />7 rows in set (0.00 sec)<br />**|
|-|





SCENARIO F - MEDICINE IS IN USE

\--------------------------------



Medicine 406 is already being used in existing prescriptions.



The hospital wants to protect historical prescription data.



Therefore, a medicine that is referenced by prescription\_medicine

should NOT be deleted.



Requirement:



Medicine -> Prescription\_Medicine



Use an appropriate action such as:



ON DELETE RESTRICT



Students must explain why ON DELETE CASCADE would be dangerous

in this situation.



|DELETE FROM MEDICINE WHERE MEDICINE\_ID=406;<br />ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails (`hospital\_management`.`prescription\_medicine`, CONSTRAINT `prescription\_medicine\_ibfk\_1` FOREIGN KEY (`medicine\_id`) REFERENCES `medicine` (`medicine\_id`) ON DELETE RESTRICT)<br />mysql>|
|-|



============================================================

11\. ON UPDATE CASCADE

============================================================



The hospital wants to change some department IDs during a data migration.



For example:



101 -> 1001

102 -> 1002

103 -> 1003

104 -> 1004



When a department ID changes, related foreign key values should

automatically change.



For example:



department.department\_id

101 -> 1001



The related values in:



doctor.department\_id

appointment.department\_id



should automatically change from:



101 -> 1001



Requirement:



Use ON UPDATE CASCADE wherever appropriate.



Students must demonstrate this using an UPDATE statement.



|UPDATE department SET department\_ID=1001 WHERE  department\_ID=101;<br />Query OK, 1 row affected (0.01 sec)<br />Rows matched: 1  Changed: 1  Warnings:<br /><br /><br /><br />SELECT \* FROM DOCTOR;<br />+-----------+-------------------+----------------+---------------+<br />\| doctor\_id \| doctor\_name       \| specialization \| department\_id \|<br />+-----------+-------------------+----------------+---------------+<br />\|       201 \| Dr. Rajesh Sharma \| Cardiologist   \|          1001 \|<br />\|       202 \| Dr. Neha Verma    \| Neurologist    \|           102 \|<br />\|       204 \| Dr. Priya Singh   \| Dermatologist  \|          NULL \|<br />\|       205 \| Dr. Karan Mehta   \| Cardiologist   \|          1001 \|<br />+-----------+-------------------+----------------+---------------+<br />4 rows in set (0.00 sec)<br /><br />mysql> SELECT \* FROM APPOINTMENT;<br />+----------------+------------------+------------------+------------+-----------+---------------+-----------+<br />\| appointment\_id \| appointment\_date \| appointment\_time \| patient\_id \| doctor\_id \| department\_id \| status    \|<br />+----------------+------------------+------------------+------------+-----------+---------------+-----------+<br />\|            502 \| 2026-09-01       \| 11:00:00         \|        302 \|       202 \|           102 \| Completed \|<br />\|            503 \| 2026-09-02       \| 09:30:00         \|        303 \|      NULL \|           103 \| Completed \|<br />\|            504 \| 2026-09-02       \| 12:00:00         \|        304 \|       204 \|          NULL \| Cancelled \|<br />\|            505 \| 2026-09-03       \| 10:30:00         \|        301 \|       205 \|          1001 \| Completed \|<br />\|            506 \| 2026-09-03       \| 11:30:00         \|        305 \|      NULL \|           103 \| Completed \|<br />\|            508 \| 2026-09-04       \| 14:00:00         \|        302 \|       202 \|           102 \| Scheduled \|<br />+----------------+------------------+------------------+------------+-----------+---------------+-----------+<br />6 rows in set (0.00 sec)<br />|
|-|



============================================================

12\. ON UPDATE SET NULL

============================================================



The hospital also wants to test a different update behavior.



Suppose doctor ID 203 is changed to 250 during an administrative

migration.



For a relationship configured with ON UPDATE SET NULL, the old

doctor reference in child records should become NULL rather than

automatically changing to 250.



Demonstrate:



UPDATE doctor

SET doctor\_id = 250

WHERE doctor\_id = 203;



Then check the related child records.


 update doctor  set doctor_id=250 where doctor_id=203;
Query OK, 0 rows affected (0.01 sec)
Rows matched: 0  Changed: 0  Warnings: 0

Expected behavior for the relationship configured with

ON UPDATE SET NULL:



Old doctor reference -> NULL



Students must explain the difference between:



ON UPDATE CASCADE

and

ON UPDATE SET NULL





============================================================

13\. REQUIRED TASKS

============================================================



TASK 1

\------



Create a database named:



hospital\_management





TASK 2

\------



Create all required tables:



1\. department

2\. doctor

3\. patient

4\. appointment

5\. medicine

6\. prescription

7\. prescription\_medicine





TASK 3

\------



Identify the PRIMARY KEY of every table.





TASK 4

\------



Identify every FOREIGN KEY.





TASK 5

\------



Implement all relationships correctly.





TASK 6

\------



For every FOREIGN KEY, decide and implement the appropriate:



ON DELETE

ON UPDATE





TASK 7

\------



Insert all the given data.





TASK 8

\------



Display every table using:



SELECT \* FROM table\_name;





TASK 9

\------



Test INVALID FOREIGN KEY.



Try inserting a child record using a parent ID that does not exist.



Example:



patient\_id = 999



Observe the error and explain why MySQL rejected the record.





TASK 10

\-------



Test ON DELETE CASCADE.



Delete a patient having appointments.



Check the appointment table before and after deletion.



Explain what happened.





TASK 11

\-------



Test ON DELETE SET NULL.



Delete a doctor.



Check the appointment table.



Verify that the appointment remains but doctor\_id becomes NULL.





TASK 12

\-------



Test ON DELETE RESTRICT.



Try deleting a medicine that is referenced by

prescription\_medicine.



Observe the error.



Explain why MySQL rejected the deletion.





TASK 13

\-------



Test ON UPDATE CASCADE.



Change a department primary key.



Verify that the related foreign keys are automatically updated.





TASK 14

\-------



Test ON UPDATE SET NULL.



Change a doctor primary key.



Verify that the configured child foreign key becomes NULL.





============================================================

14\. IMPORTANT QUESTIONS TO ANSWER

============================================================



Answer the following questions in your submission.



1\. Why does the appointment table contain multiple foreign keys?



2\. Which tables are parent tables and which are child tables?



3\. What is the relationship between Patient and Appointment?



4\. What is the relationship between Doctor and Appointment?



5\. What is the relationship between Prescription and Medicine?



6\. Why is prescription\_medicine required?



7\. Why is prescription\_medicine using a composite primary key?



8\. Why should deleting a doctor NOT delete historical appointments?



9\. Why is ON DELETE SET NULL suitable for Department -> Doctor?



10\. Why is ON DELETE CASCADE suitable for Patient -> Appointment

&#x20;   in the given test-data scenario?



11\. Why can ON DELETE CASCADE be dangerous for Medicine ->

&#x20;   Prescription\_Medicine?



12\. What is the difference between ON DELETE CASCADE and

&#x20;   ON DELETE SET NULL?



13\. What is the difference between ON UPDATE CASCADE and

&#x20;   ON UPDATE SET NULL?



14\. What happens if you try to insert a child record with a

&#x20;   non-existing parent ID?



15\. What happens if you try to delete a parent record when

&#x20;   ON DELETE RESTRICT is configured?





============================================================

15\. SUBMISSION REQUIREMENTS

============================================================



Your submission must contain:



1\. Database creation command

2\. CREATE TABLE statements

3\. PRIMARY KEY definitions

4\. FOREIGN KEY definitions

5\. ON DELETE definitions

6\. ON UPDATE definitions

7\. INSERT statements

8\. SELECT \* output for all tables

9\. Invalid FK test

10\. ON DELETE CASCADE test

11\. ON DELETE SET NULL test

12\. ON DELETE RESTRICT test

13\. ON UPDATE CASCADE test

14\. ON UPDATE SET NULL test

15\. Answers to all theory questions





============================================================

GOOD LUCK!

