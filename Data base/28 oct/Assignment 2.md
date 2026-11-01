DELETE COMMAND ASSIGNMENT

Table Name: staff\_delete

Column Data Type

staff\_id INT PRIMARY KEY AUTO\_INCREMENT

staff\_name VARCHAR(50)

department VARCHAR(30)

city VARCHAR(30)

salary DECIMAL(10,2)

experience INT

age INT

joining\_date DATE

status VARCHAR(20)

|create Table staff\_delete\_28oct (staff\_id INT PRIMARY KEY AUTO\_INCREMENT,staff\_name VARCHAR(50),department VARCHAR(30),<br />    -> city VARCHAR(30),<br />    -> salary DECIMAL(10,2),<br />    -> experience INT,<br />    -> age INT,<br />    -> joining\_date DATE,<br />    -> status VARCHAR(20));<br />Query OK, 0 rows affected (0.04 sec)|
|-|



DATA

('Aarav', 'IT', 'Indore', 48000, 3, 26, '2022-04-15', 'Active'),

('Bhavna', 'HR', 'Bhopal', 56000, 5, 31, '2020-08-20', 'Active'),

('Chetan', 'Finance', 'Delhi', 62000, 7, 35, '2018-03-10', 'Active'),

('Divya', 'IT', 'Pune', 78000, 9, 38, '2016-11-05', 'Active'),

('Eshan', 'Sales', 'Indore', 51000, 4, 29, '2021-06-18', 'Inactive'),

('Farah', 'HR', NULL, 68000, 6, 34, '2019-01-25', 'Active'),

('Gaurav', 'Finance', 'Mumbai', 74000, 8, 40, '2017-09-12', 'Active'),

('Heena', 'IT', 'Delhi', 59000, 5, 30, '2020-02-17', 'Inactive'),

('Ishaan', 'Sales', 'Pune', 45000, 2, 25, '2023-01-10', 'Active'),

('Jaya', 'HR', 'Indore', 72000, 7, 36, '2018-07-22', 'Active');

| insert into staff\_delete\_28oct (staff\_name,department,city,salary,experience,age,joining\_date,status)values(<br />    -> 'Bhavna', 'HR', 'Bhopal', 56000, 5, 31, '2020-08-20', 'Active'),<br />    -> ('Chetan', 'Finance', 'Delhi', 62000, 7, 35, '2018-03-10', 'Active'),<br />    -> ('Divya', 'IT', 'Pune', 78000, 9, 38, '2016-11-05', 'Active'),<br />    -> ('Eshan', 'Sales', 'Indore', 51000, 4, 29, '2021-06-18', 'Inactive'),<br />    -> ('Farah', 'HR', NULL, 68000, 6, 34, '2019-01-25', 'Active'),<br />    -> ('Gaurav', 'Finance', 'Mumbai', 74000, 8, 40, '2017-09-12', 'Active'),<br />    -> ('Heena', 'IT', 'Delhi', 59000, 5, 30, '2020-02-17', 'Inactive'),<br />    -> ('Ishaan', 'Sales', 'Pune', 45000, 2, 25, '2023-01-10', 'Active'),<br />    -><br />    -> ('Jaya', 'HR', 'Indore', 72000, 7, 36, '2018-07-22', 'Active');<br />Query OK, 9 rows affected (0.01 sec)<br />Records: 9  Duplicates: 0  Warnings: 0<br /><br />mysql> select \* from staff\_delete\_28oct;<br />+----------+------------+------------+--------+----------+------------+------+--------------+----------+<br />\| staff\_id \| staff\_name \| department \| city   \| salary   \| experience \| age  \| joining\_date \| status   \|<br />+----------+------------+------------+--------+----------+------------+------+--------------+----------+<br />\|        1 \| Aarav      \| IT         \| Indore \| 48000.00 \|          3 \|   26 \| 2022-04-15   \| Active   \|<br />\|        2 \| Bhavna     \| HR         \| Bhopal \| 56000.00 \|          5 \|   31 \| 2020-08-20   \| Active   \|<br />\|        3 \| Chetan     \| Finance    \| Delhi  \| 62000.00 \|          7 \|   35 \| 2018-03-10   \| Active   \|<br />\|        4 \| Divya      \| IT         \| Pune   \| 78000.00 \|          9 \|   38 \| 2016-11-05   \| Active   \|<br />\|        5 \| Eshan      \| Sales      \| Indore \| 51000.00 \|          4 \|   29 \| 2021-06-18   \| Inactive \|<br />\|        6 \| Farah      \| HR         \| NULL   \| 68000.00 \|          6 \|   34 \| 2019-01-25   \| Active   \|<br />\|        7 \| Gaurav     \| Finance    \| Mumbai \| 74000.00 \|          8 \|   40 \| 2017-09-12   \| Active   \|<br />\|        8 \| Heena      \| IT         \| Delhi  \| 59000.00 \|          5 \|   30 \| 2020-02-17   \| Inactive \|<br />\|        9 \| Ishaan     \| Sales      \| Pune   \| 45000.00 \|          2 \|   25 \| 2023-01-10   \| Active   \|<br />\|       10 \| Jaya       \| HR         \| Indore \| 72000.00 \|          7 \|   36 \| 2018-07-22   \| Active   \|<br />+----------+------------+------------+--------+----------+------------+------+--------------+----------+<br />10 rows in set (0.00 sec)|
|-|



Questions





Q1. Delete the employee whose name is Aarav using his staff\_id.



|delete from staff\_delete\_28oct where staff\_id=1;|
|-|



Q2. Delete all employees who belong to the Sales department.

|delete from staff\_delete\_28oct where department="sales";|
|-|





Q3. Delete all employees whose salary is below ₹50,000.

| delete from staff\_delete\_28oct where salary<50000;|
|-|



&#x09;

Q4. Delete all employees who belong to HR and have at least 5 years of experience.

|delete from staff\_delete\_28oct where department="hr" and experience>=5;|
|-|





Q5. Delete all employees who are from Indore or Bhopal.

| delete from staff\_delete\_28oct where city in ("indore","Bhopal");|
|-|



Q6. Delete all employees who belong to neither IT nor Finance.

|delete from staff\_delete\_28oct where department not in ("it","Finance");|
|-|





Q7. Delete all employees whose salary is between ₹50,000 and ₹65,000, inclusive.

| delete from staff\_delete\_28oct where salary between 50000 and 65000;|
|-|





Q8. Delete all employees who have less than 5 years of experience and whose status is Inactive.

|delete from staff\_delete\_28oct where experience<5 and status="inactive";|
|-|





Q9. Delete all employees whose names start with the letter D.

| delete from staff\_delete\_28oct where staff\_name like ("d%");|
|-|





Q10. Delete all employees whose city is NULL.

|delete from staff\_delete\_28oct where city is null;|
|-|



Q11. Delete all employees who joined before January 1, 2020 and have a salary of at least ₹60,000.

| delete from staff\_delete\_28oct where joining\_date<"2020-01-01" and salary>=60000;|
|-|





Q12. Delete all employees who belong to IT or HR, have at least 3 years of experience, and earn less than ₹70,000.

| delete from staff\_delete\_28oct where department in ("it","hr") and experience>=3 and salary<70000;|
|-|





Q13. Delete all employees who are not from Sales, have salary above ₹55,000, and are currently Active.

| delete from staff\_delete\_28oct where department !="Sales" and status="active" and salary>55000;|
|-|





Q14. Delete all employees who belong to Finance or HR and have a salary below ₹65,000.

| delete from staff\_delete\_28oct where department in ("Finance","hr") and salary<65000;|
|-|



Q15. Delete the employee with the lowest salary from the table. If multiple employees have the same lowest salary, delete only one employee.

|delete  from staff\_delete\_28oct order by  salary limit 1;|
|-|





Q16. Delete the employee with the highest salary from the table. If multiple employees have the same highest salary, delete only one employee.

| delete  from staff\_delete\_28oct order by  salary desc limit 1;|
|-|





Q17. Delete only the lowest-paid employee who belongs to IT or HR, has at least 3 years of experience, and earns less than ₹70,000.

| delete  from staff\_delete\_28oct where department in ("it","hr") and experience>=3 and salary <70000 order by  salary limit 1;|
|-|





Q18. Delete only the highest-paid Active employee having at least 5 years of experience.

|delete  from staff\_delete\_28oct where status="active" and experience>=5  order by  salary desc limit 1;         |
|-|



Q19. Delete only the lowest-paid employee who is neither from HR nor Sales, has at least 3 years of experience, and earns below ₹70,000.

| delete  from staff\_delete\_28oct where department not in ("sales","hr") and experience>=3 and salary < 70000 order by  salary  limit 1;|
|-|





Q20. Delete all employees who satisfy either of the following conditions:



IT employees having at least 5 years of experience and salary below ₹80,000

Finance employees having salary below ₹65,000

| delete  from staff\_delete\_28oct where (department ="it" and experience>=5 and salary < 80000 ) or (department ="Finance" and salary <65000) ;|
|-|



