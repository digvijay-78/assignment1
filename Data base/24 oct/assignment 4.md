EMPLOYEE PAYROLL AND JOB MANAGEMENT SYSTEM



A company wants to maintain employee information in MySQL. You have been asked to design an employee table that strictly enforces the company's data rules using NOT NULL, UNIQUE and CHECK constraints.

1\. CREATE THE EMPLOYEE TABLE

Create a table named employee with the following columns.

emp\_id

INT

Employee ID, Primary Key, Auto Increment

emp\_name

VARCHAR(50)

Mandatory

email

VARCHAR(100)

Mandatory and must be unique

phone

VARCHAR(15)

Mandatory and must be unique

department

VARCHAR(30)

Mandatory

designation

VARCHAR(30)

Mandatory

age

INT

Mandatory, employee must be between 21 and 60



salary

DECIMAL(10,2)

Mandatory, salary must be greater than 15000



experience

INT

Mandatory, experience must be between 0 and 35 years



joining\_year

INT

Mandatory



status

VARCHAR(20)

Mandatory, only Active, Inactive or On Leave



bonus

DECIMAL(10,2)

Mandatory, cannot be negative



2\. APPLY THE CONSTRAINTS



NOT NULL CONSTRAINTS



The following columns cannot contain NULL.



emp\_name

email

phone

department

designation

age

salary

experience

joining\_year

status

bonus





UNIQUE CONSTRAINTS



The following values must be unique across employees.



email

phone



Two employees cannot have the same email or phone number.





CHECK CONSTRAINTS ON INDIVIDUAL COLUMNS



1\. Age must be between 21 and 60.



2\. Salary must be greater than 15000.



3\. Experience must be between 0 and 35 years.



4\. Bonus must be greater than or equal to 0.



5\. Status can only be Active, Inactive or On Leave.

|create table EMPLOYEE (emp\_id int  Primary Key Auto\_Increment,emp\_name VARCHAR(50) not null , email  VARCHAR(100) not null unique ,phone VARCHAR(15) not null unique,department VARCHAR(30) not null , designation VARCHAR(30) not null, age int not null check (age between 21 and 60),salary DECIMAL(10,2) not null check (salary >15000),experience int not null check (experience between 0 and 35),joining\_year int not null ,status VARCHAR(20) not null check (status in ("Active", "Inactive" , "On Leave")),bonus DECIMAL(10,2) not null check (bonus >=0));<br />Query OK, 0 rows affected (0.08 sec)<br /><br />mysql> desc EMPLOYEE;<br />+--------------+---------------+------+-----+---------+----------------+<br />\| Field        \| Type          \| Null \| Key \| Default \| Extra          \|<br />+--------------+---------------+------+-----+---------+----------------+<br />\| emp\_id       \| int           \| NO   \| PRI \| NULL    \| auto\_increment \|<br />\| emp\_name     \| varchar(50)   \| NO   \|     \| NULL    \|                \|<br />\| email        \| varchar(100)  \| NO   \| UNI \| NULL    \|                \|<br />\| phone        \| varchar(15)   \| NO   \| UNI \| NULL    \|                \|<br />\| department   \| varchar(30)   \| NO   \|     \| NULL    \|                \|<br />\| designation  \| varchar(30)   \| NO   \|     \| NULL    \|                \|<br />\| age          \| int           \| NO   \|     \| NULL    \|                \|<br />\| salary       \| decimal(10,2) \| NO   \|     \| NULL    \|                \|<br />\| experience   \| int           \| NO   \|     \| NULL    \|                \|<br />\| joining\_year \| int           \| NO   \|     \| NULL    \|                \|<br />\| status       \| varchar(20)   \| NO   \|     \| NULL    \|                \|<br />\| bonus        \| decimal(10,2) \| NO   \|     \| NULL    \|                \|<br />+--------------+---------------+------+-----+---------+----------------+<br />12 rows in set (0.02 sec)|
|-|





3\. COMBINATION CHECK CONSTRAINTS

Rule 1: Experience and Age

An employee cannot have more experience than realistically possible based on age.

Create a CHECK constraint such that:

experience must be less than or equal to age minus 21.

Example:

Age 25 and Experience 4 is valid.

Age 25 and Experience 10 is invalid.

Rule 2: Salary and Experience

Employees with more experience must have an appropriate minimum salary.

If experience is greater than or equal to 10, salary must be greater than or equal to 50000.

Example:

Experience 12 and Salary 60000 is valid.

Experience 12 and Salary 35000 is invalid.

Rule 3: Department and Designation

The company allows only certain designation combinations.

IT

Developer

Tester

Team Lead

HR

HR Executive

HR Manager

Finance

Accountant

Finance Manager

Sales

Sales Executive

Sales Manager

Examples:

IT and Developer is valid.

IT and HR Manager is invalid.

HR and Developer is invalid.

Finance and Accountant is valid.

Implement this using a CHECK constraint involving both department and designation.

Rule 4: Status and Bonus

Business rules:

Active employees can receive bonus.

Inactive employees must have bonus equal to 0.

On Leave employees can have a bonus, but it cannot exceed 20 percent of salary.

Examples:

Active with salary 50000 and bonus 10000 is valid.

Inactive with salary 50000 and bonus 5000 is invalid.

Inactive with salary 50000 and bonus 0 is valid.

On Leave with salary 50000 and bonus 10000 is valid.

On Leave with salary 50000 and bonus 15000 is invalid.

Rule 5: Joining Year and Experience

Assume the current year is 2026.

The employee's experience cannot be greater than the number of years since joining.

Example:

Joining year 2020 and Experience 6 is valid.

Joining year 2020 and Experience 10 is invalid.

Joining year cannot be greater than 2026.



|ALTER TABLE employee<br />    -> ADD CHECK (experience <= age - 21);<br />Query OK, 0 rows affected (0.21 sec)<br />Records: 0  Duplicates: 0  Warnings: 0<br /><br /><br /><br />mysql> ALTER TABLE employee add check (experience <10 or salary >=50000);<br />Query OK, 0 rows affected (0.11 sec)<br />Records: 0  Duplicates: 0  Warnings: 0<br /><br /><br /> alter table employee add check ((department ="IT" and Designation in ("Developer","tester","team lead") )or (department ="hr" and Designation in("HR Executive","HR Manager")) or (department ="Finance" and Designation in ("Accountant","Finance Manager")) or  (department ="Sales" and Designation in("Sales Executive","Sales Manager")));<br />Query OK, 0 rows affected (0.15 sec)<br />Records: 0  Duplicates: 0  Warnings: 0<br /><br /><br /> alter table employee add check ((status ="inactive" and bonus =0) or (status ="On Leave" and bonus <= salary\*0.20) or (status="active"));<br />Query OK, 0 rows affected (0.15 sec)<br /><br /><br />alter table employee add check ((2026 -joining\_year>=experience) and  (joining\_year<=2026));<br />Query OK, 0 rows affected (0.14 sec)<br />Records: 0  Duplicates: 0  Warnings: 0|
|-|





4\. INSERT VALID RECORDS



Insert at least 10 valid employees satisfying all constraints simultaneously.



Your records should cover:



Multiple departments

Multiple designations

Different experience levels

Different salary ranges

All three statuses

Different bonus values





|INSERT INTO employee<br />    -> (emp\_name,email,phone,department,designation,age,salary,experience,joining\_year,status,bonus)<br />    -> VALUES<br />    -> (NULL,'test1@gmail.com','9000000001','IT','Developer',25,30000,3,2023,'Active',2000);<br />ERROR 1048 (23000): Column 'emp\_name' cannot be null<br />mysql> INSERT INTO employee<br />    -> (emp\_name,email,phone,department,designation,age,salary,experience,joining\_year,status,bonus)<br />    -> VALUES<br />    -> ('Test2',NULL,'9000000002','IT','Developer',25,30000,3,2023,'Active',2000);<br />ERROR 1048 (23000): Column 'email' cannot be null<br />mysql> INSERT INTO employee<br />    -> (emp\_name,email,phone,department,designation,age,salary,experience,joining\_year,status,bonus)<br />    -> VALUES<br />    -> ('Test2',NULL,'9000000002','IT','Developer',25,30000,3,2023,'Active',2000);<br />ERROR 1048 (23000): Column 'email' cannot be null<br />mysql> INSERT INTO employee<br />    -> (emp\_name,email,phone,department,designation,age,salary,experience,joining\_year,status,bonus)<br />    -> VALUES<br />    -> ('Test2',NULL,'9000000002','IT','Developer',25,30000,3,2023,'Active',2000);<br />ERROR 1048 (23000): Column 'email' cannot be null<br />mysql> INSERT INTO employee<br />    -> (emp\_name,email,phone,department,designation,age,salary,experience,joining\_year,status,bonus)<br />    -> VALUES<br />    -> ('Test6','test6@gmail.com','9000000006','IT','Developer',18,30000,0,2026,'Active',2000);<br />ERROR 3819 (HY000): Check constraint 'employee\_chk\_1' is violated.<br />mysql> INSERT INTO employee<br />    -> (emp\_name,email,phone,department,designation,age,salary,experience,joining\_year,status,bonus)<br />    -> VALUES<br />    -> ('Test7','test7@gmail.com','9000000007','IT','Developer',25,10000,3,2023,'Active',1000);<br />ERROR 3819 (HY000): Check constraint 'employee\_chk\_2' is violated.<br />mysql> INSERT INTO employee<br />    -> (emp\_name,email,phone,department,designation,age,salary,experience,joining\_year,status,bonus)<br />    -> VALUES<br />    -> ('Test8','test8@gmail.com','9000000008','IT','Developer',25,30000,-2,2023,'Active',2000);<br />ERROR 3819 (HY000): Check constraint 'employee\_chk\_3' is violated.<br />mysql> INSERT INTO employee<br />    -> (emp\_name,email,phone,department,designation,age,salary,experience,joining\_year,status,bonus)<br />    -> VALUES<br />    -> ('Test9','test9@gmail.com','9000000009','IT','Developer',25,30000,3,2023,'Active',-500);<br />ERROR 3819 (HY000): Check constraint 'employee\_chk\_5' is violated.<br />mysql> INSERT INTO employee<br />    -> (emp\_name,email,phone,department,designation,age,salary,experience,joining\_year,status,bonus)<br />    -> VALUES<br />    -> ('Test10','test10@gmail.com','9000000010','IT','Developer',25,30000,3,2023,'Retired',2000);<br />ERROR 3819 (HY000): Check constraint 'employee\_chk\_4' is violated.<br />mysql> INSERT INTO employee<br />    -> (emp\_name,email,phone,department,designation,age,salary,experience,joining\_year,status,bonus)<br />    -> VALUES<br />    -> ('Test10','test10@gmail.com','9000000010','IT','Developer',25,30000,3,2023,'Retired',2000);<br />ERROR 3819 (HY000): Check constraint 'employee\_chk\_4' is violated.<br />mysql> INSERT INTO employee<br />    -> (emp\_name,email,phone,department,designation,age,salary,experience,joining\_year,status,bonus)<br />    -> VALUES<br />    -> ('Test12','test12@gmail.com','9000000012','IT','Developer',40,35000,12,2014,'Active',2000);<br />ERROR 3819 (HY000): Check constraint 'employee\_chk\_7' is violated.<br />mysql>|
|-|



