Assignment 1:



&#x20;Employee Salary Analysis

Use the following employees table to solve the questions below.



NOTE:-use your friends names in the given table.

Table: employees

id name department job\_role salary hire\_date

1 Alice HR       Manager       6000.00 2022-01-15

2 Bob HR Recruiter 4000.00 2023-03-20

3 Charlie IT Developer 5000.00 2022-07-25

4 David IT Developer 5500.00 2021-12-05

5 Eve IT Tester 4500.00 2023-06-10

6 Frank IT Tester 4800.00 2023-09-12

7 Grace Finance Analyst 5200.00 2021-11-18

8 Hank Finance Analyst 5300.00 2022-04-30

9 Ivy Finance Manager 7000.00 2023-08-14

10 Jack HR Recruiter 4200.00 2022-10-05

Questions

Find the total number of employees in each department.

|select department, count(\*) from employees28oct GROUP BY DEPARTMENT ;<br />+------------+----------+<br />\| department \| count(\*) \|<br />+------------+----------+<br />\| HR         \|        3 \|<br />\| IT         \|        4 \|<br />\| Finance    \|        3 \|<br />+------------+----------+|
|-|



Find the average salary of employees in each job role.

|select job\_role, AVG(SALARY) from employees28oct GROUP BY job\_role ;<br />+-----------+-------------+<br />\| job\_role  \| AVG(SALARY) \|<br />+-----------+-------------+<br />\| Manager   \| 6500.000000 \|<br />\| Developer \| 5250.000000 \|<br />\| Recruiter \| 4100.000000 \|<br />\| Tester    \| 4650.000000 \|<br />\| Analyst   \| 5250.000000 \|<br />+-----------+-------------+|
|-|



Find the highest salary in the IT department.

|select MAX(SALARY) from employees28oct WHERE DEPARTMENT="IT" ;<br />+-------------+<br />\| MAX(SALARY) \|<br />+-------------+<br />\|     5500.00 \|<br />+-------------+|
|-|



Find the lowest salary among all employees

.

|select MIN(SALARY) from employees28oct  ;<br />+-------------+<br />\| MIN(SALARY) \|<br />+-------------+<br />\|     4000.00 \|<br />+-------------+|
|-|



Count the number of employees who joined after January 1, 2023.

|select  count(\*) from employees28oct WHERE hire\_date >"2023-01-01" ;<br />+----------+<br />\| count(\*) \|<br />+----------+<br />\|        4 \|<br />+----------+|
|-|



Find the total salary paid in each department.

|select department, SUM(SALARY) from employees28oct GROUP BY DEPARTMENT ;<br />+------------+-------------+<br />\| department \| SUM(SALARY) \|<br />+------------+-------------+<br />\| HR         \|    14200.00 \|<br />\| IT         \|    19800.00 \|<br />\| Finance    \|    17500.00 \|<br />+------------+-------------+|
|-|



Find the job role that has the highest total salary payout.

|select job\_role, SUM(SALARY) AS total\_salary from employees28oct GROUP BY job\_role ORDER BY total\_salary DESC LIMIT 1;<br />+----------+--------------+<br />\| job\_role \| total\_salary \|<br />+----------+--------------+<br />\| Manager  \|     13000.00 \|<br />+----------+--------------+|
|-|



Find the average salary of employees who joined after 2022.

|select AVG(SALARY) from employees28oct WHERE hire\_date >"2022-12-31"  ;<br />+-------------+<br />\| AVG(SALARY) \|<br />+-------------+<br />\| 5075.000000 \|<br />+-------------+|
|-|



Find departments where the total salary exceeds 10,000.

|select department, SUM(SALARY) AS SAL from employees28oct  GROUP BY DEPARTMENT HAVING SAL>10000 ;<br />+------------+----------+<br />\| department \| SAL      \|<br />+------------+----------+<br />\| HR         \| 14200.00 \|<br />\| IT         \| 19800.00 \|<br />\| Finance    \| 17500.00 \|<br />+------------+----------+|
|-|



Find the department with the highest number of employees.



|select department, COUNT(\*) from employees28oct GROUP BY DEPARTMENT ORDER BY COUNT(\*) DESC LIMIT 1;<br />+------------+----------+<br />\| department \| COUNT(\*) \|<br />+------------+----------+<br />\| IT         \|        4 \|<br />+------------+----------+|
|-|







2\.

Student Performance Analysis

Use the following students table for the queries.



NOTE: use your friends names in the given table.

Table: students

student\_id name class subject marks exam\_date

1 John 10 Math 85 2023-02-10

2 Alice 10 Science 78 2023-03-15

3 Bob 9 Math 92 2023-04-20

4 David 9 Science 80 2023-05-25

5 Eve 10 Math 88 2023-06-30

6 Frank 9 Science 75 2023-07-10

7 Grace 10 Math 90 2023-08-20

8 Hank 9 Math 85 2023-09-15

9 Ivy 10 Science 82 2023-10-10

10 Jack 9 Science 79 2023-11-05

Questions

Find the total number of students in each class.

|SELECT class,COUNT(\*) FROM students28oct GROUP BY CLASS;<br />+-------+----------+<br />\| class \| COUNT(\*) \|<br />+-------+----------+<br />\|    10 \|        5 \|<br />\|     9 \|        5 \|<br />+-------+----------+|
|-|



Find the highest marks scored in Math.

|select MAX(MARKS) from students28oct WHERE SUBJECT="MATH" ;<br />+------------+<br />\| MAX(MARKS) \|<br />+------------+<br />\|         92 \|<br />+------------+|
|-|



Find the average marks in each subject.

|SELECT subject, AVG(marks) FROM students28oct GROUP BY SUBJECT;<br />+---------+------------+<br />\| subject \| AVG(marks) \|<br />+---------+------------+<br />\| Math    \|    88.0000 \|<br />\| Science \|    78.8000 \|<br />+---------+------------+|
|-|



Find the total number of students who scored above 80.

|SELECT COUNT(\*) FROM students28oct WHERE MARKS>80;<br />+----------+<br />\| COUNT(\*) \|<br />+----------+<br />\|        6 \|<br />+----------+|
|-|



Find the number of students who took the exam in each month.

|SELECT exam\_date, COUNT(\*) FROM students28oct  GROUP BY exam\_date;<br />+------------+----------+<br />\| exam\_date  \| COUNT(\*) \|<br />+------------+----------+<br />\| 2023-02-10 \|        1 \|<br />\| 2023-03-15 \|        1 \|<br />\| 2023-04-20 \|        1 \|<br />\| 2023-05-25 \|        1 \|<br />\| 2023-06-30 \|        1 \|<br />\| 2023-07-10 \|        1 \|<br />\| 2023-08-20 \|        1 \|<br />\| 2023-09-15 \|        1 \|<br />\| 2023-10-10 \|        1 \|<br />\| 2023-11-05 \|        1 \|<br />+------------+----------+<br />|
|-|

|SELECT MONTH(exam\_date), COUNT(\*) FROM students28oct  GROUP BY MONTH(exam\_date);<br />+------------------+----------+<br />\| MONTH(exam\_date) \| COUNT(\*) \|<br />+------------------+----------+<br />\|                2 \|        1 \|<br />\|                3 \|        1 \|<br />\|                4 \|        1 \|<br />\|                5 \|        1 \|<br />\|                6 \|        1 \|<br />\|                7 \|        1 \|<br />\|                8 \|        1 \|<br />\|                9 \|        1 \|<br />\|               10 \|        1 \|<br />\|               11 \|        1 \|<br />+------------------+----------+<br />10 rows in set (0.00 sec)<br /><br />mysql> SELECT MONTHNAME(exam\_date), COUNT(\*) FROM students28oct  GROUP BY MONTHNAME(exam\_date);<br />+----------------------+----------+<br />\| MONTHNAME(exam\_date) \| COUNT(\*) \|<br />+----------------------+----------+<br />\| February             \|        1 \|<br />\| March                \|        1 \|<br />\| April                \|        1 \|<br />\| May                  \|        1 \|<br />\| June                 \|        1 \|<br />\| July                 \|        1 \|<br />\| August               \|        1 \|<br />\| September            \|        1 \|<br />\| October              \|        1 \|<br />\| November             \|        1 \|<br />+----------------------+----------+<br />10 rows in set (0.00 sec)<br />|
|-|



Find the subject where students scored the highest average marks.

|SELECT SUBJECT, AVG(MARKS) FROM students28oct  GROUP BY SUBJECT ORDER BY AVG(MARKS) DESC LIMIT 1;<br />+---------+------------+<br />\| SUBJECT \| AVG(MARKS) \|<br />+---------+------------+<br />\| Math    \|    88.0000 \|<br />+---------+------------+|
|-|



Find the student who scored the lowest marks in Science.

|SELECT  MIN(MARKS) FROM students28oct  WHERE SUBJECT ="Science" ;<br />+------------+<br />\| MIN(MARKS) \|<br />+------------+<br />\|         75 \|<br />+------------+<br /><br />SELECT name, marks FROM students28oct WHERE subject = 'Science' ORDER BY marks LIMIT 1;<br />+---------+-------+<br />\| name    \| marks \|<br />+---------+-------+<br />\| Vinayak \|    75 \|<br />+---------+-------+|
|-|



Find the number of students in each class who scored more than 85.

|SELECT CLASS, COUNT(\*) FROM students28oct  WHERE MARKS >85 GROUP BY CLASS ;<br />+-------+----------+<br />\| CLASS \| COUNT(\*) \|<br />+-------+----------+<br />\|     9 \|        1 \|<br />\|    10 \|        2 \|<br />+-------+----------+|
|-|



Find the average marks for each subject where the average is above 80.

|SELECT SUBJECT, AVG(MARKS) AS AV FROM students28oct  GROUP BY SUBJECT HAVING AV> 80 ;<br />+---------+---------+<br />\| SUBJECT \| AV      \|<br />+---------+---------+<br />\| Math    \| 88.0000 \|<br />+---------+---------+|
|-|



Find the student who scored the highest marks overall.

|SELECT NAME,MAX(MARKS)  FROM students28oct  GROUP BY NAME ORDER BY MAX(MARKS) DESC LIMIT 1;<br />+-------+------------+<br />\| NAME  \| MAX(MARKS) \|<br />+-------+------------+<br />\| Rohit \|         92 \|<br />+-------+------------+<br /><br /><br /> SELECT NAME,MARKS FROM students28oct  ORDER BY MARKS DESC LIMIT 1;<br />+-------+-------+<br />\| NAME  \| MARKS \|<br />+-------+-------+<br />\| Rohit \|    92 \|<br />+-------+-------+|
|-|



