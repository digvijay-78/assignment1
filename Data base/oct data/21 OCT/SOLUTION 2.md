QNO 2:

Table Name: staff\_update



| Column         | Data Type                      |

| -------------- | ------------------------------ |

| staff\_id     | INT PRIMARY KEY AUTO\_INCREMENT |

| staff\_name   | VARCHAR(50)                    |

| department   | VARCHAR(30)                    |

| city         | VARCHAR(30)                    |

| salary       | DECIMAL(10,2)                  |

| experience   | INT                            |

| age          | INT                            |

| joining\_date | DATE                           |

| status       | VARCHAR(20)                    |

===================================================



|**mysql> create table staff\_update(<br />    ->     staff\_id int primary key auto\_increment,<br />    ->     staff\_name varchar(50),<br />    ->     department varchar(30),<br />    ->     city varchar(30),<br />    ->     salary decimal(10,2),<br />    ->     experience int,<br />    ->     age int,<br />    ->     joining\_date date,<br />    ->     status varchar(20)<br />    -> );**|
|-|



DATA:--

('Aarav', 'IT', 'Indore', 48000, 3, 26, '2022-04-15', 'Active'),

('Bhavna', 'HR', 'Bhopal', 56000, 5, 31, '2020-08-20', 'Active'),

('Chetan', 'Finance', 'Delhi', 62000, 7, 35, '2018-03-10', 'Active'),

('Divya', 'IT', 'Pune', 78000, 9, 38, '2016-11-05', 'Active'),

('Eshan', 'Sales', 'Indore', 51000, 4, 29, '2021-06-18', 'Inactive'),

('Farah', 'HR', NULL, 68000, 6, 34, '2019-01-25', 'Active');



|**mysql> insert into staff\_update<br />    -> (staff\_name, department, city, salary, experience, age, joining\_date, status)<br />    -> values<br />    -> ('Aarav', 'IT', 'Indore', 48000, 3, 26, '2022-04-15', 'Active'),<br />    -> ('Bhavna', 'HR', 'Bhopal', 56000, 5, 31, '2020-08-20', 'Active'),<br />    -> ('Chetan', 'Finance', 'Delhi', 62000, 7, 35, '2018-03-10', 'Active'),<br />    -> ('Divya', 'IT', 'Pune', 78000, 9, 38, '2016-11-05', 'Active'),<br />    -> ('Eshan', 'Sales', 'Indore', 51000, 4, 29, '2021-06-18', 'Inactive'),<br />    -> ('Farah', 'HR', NULL, 68000, 6, 34, '2019-01-25', 'Active');<br />Query OK, 6 rows affected (0.02 sec)**|
|-|





Questions



Q1. Aarav's salary needs to be revised to ₹52,000. Update his salary using his employee ID.

|**update staff\_update set salary=52000 where staff\_id=1;<br /><br /> select \* from staff\_update ;<br />+----------+------------+------------+--------+----------+------------+------+--------------+----------+<br />\| staff\_id \| staff\_name \| department \| city   \| salary   \| experience \| age  \| joining\_date \| status   \|<br />+----------+------------+------------+--------+----------+------------+------+--------------+----------+<br />\|        1 \| Aarav      \| IT         \| Indore \| 52000.00 \|          3 \|   26 \| 2022-04-15   \| Active   \|<br />\|        2 \| Bhavna     \| HR         \| Bhopal \| 56000.00 \|          5 \|   31 \| 2020-08-20   \| Active   \|<br />\|        3 \| Chetan     \| Finance    \| Delhi  \| 62000.00 \|          7 \|   35 \| 2018-03-10   \| Active   \|<br />\|        4 \| Divya      \| IT         \| Pune   \| 78000.00 \|          9 \|   38 \| 2016-11-05   \| Active   \|<br />\|        5 \| Eshan      \| Sales      \| Indore \| 51000.00 \|          4 \|   29 \| 2021-06-18   \| Inactive \|<br />\|        6 \| Farah      \| HR         \| NULL   \| 68000.00 \|          6 \|   34 \| 2019-01-25   \| Active   \|<br />+----------+------------+------------+--------+----------+------------+------+--------------+----------+**|
|-|





Q2. Bhavna has been transferred to the Finance department in Indore. Update both her department and city.

|**update staff\_update set department="Finance" , city= "indore" where staff\_name="bhavna";<br /><br /> 2 \| Bhavna     \| Finance    \| indore  \| 56000.00 \|          5 \|   31 \| 2020-08-20   \| Active   \|**|
|-|





Q3. Give a ₹4,000 increment to employees whose salary is below ₹60,000, who have at least 3 years of experience, and who do not belong to Sales.

|**update staff\_update set salary=salary +4000 where SALARY<60000 AND experience>=3 AND DEPARTMENT !="SALES";**|
|-|





Q4. Give a ₹3,000 increment to employees who either belong to IT with at least 3 years of experience or belong to HR with at least 5 years of experience.

|**update staff\_update set SALARY = SALARY+3000 where (DEPARTMENT="IT" AND experience>=3 ) OR (DEPARTMENT="HR" AND experience>=5);**|
|-|





Q5. Give a 10% increment to employees from IT or Finance whose current salary is below ₹70,000.



|**update staff\_update set salary=salary \* 1.1 where SALARY<70000 AND  DEPARTMENT IN ("IT","Finance");**|
|-|



Q6. Give a ₹2,500 increment to employees who are neither from HR nor Sales and have between 5 and 8 years of experience.

|**update staff\_update set SALARY =SALARY+2500 where DEPARTMENT NOT IN ("HR","SALES") AND experience BETWEEN 5 AND 8 ;**|
|-|





Q7. Give a ₹5,000 increment to employees whose salary is between ₹50,000 and ₹70,000, excluding Finance employees.

|**update staff\_update set salary=salary +5000 where SALARY BETWEEN 50000 AND 70000 AND  DEPARTMENT !="Finance";**|
|-|





Q8. Give a 7% increment to employees whose names start with either A or D.

|**update staff\_update set salary=salary \* 1.07 where staff\_name LIKE ("A%") OR  staff\_name LIKE ("D%");**|
|-|





Q9. Farah's city is missing. Update her city to Mumbai without modifying employees whose city is already available.

|**update staff\_update set CITY="MUMBAI" where staff\_name="Farah";**|
|-|





Q10. Give a 10% increment to employees who joined before January 1, 2020 and whose salary is below ₹70,000.

|**update staff\_update set SALARY =SALARY \*1.1 where joining\_date< "2020-01-01" AND SALARY <70000;**|
|-|





Q11. For IT employees having at least 5 years of experience, increase salary by 8%, increase experience by 1 year, and change their status to Promoted.

|**update staff\_update set SALARY =SALARY \* 1.08,experience=experience+1,STATUS ="Promoted" where DEPARTMENT ="IT" AND experience>=5;**|
|-|





Q12. Give a ₹6,000 increment to employees having at least 5 years of experience, salary below ₹75,000, and belonging to either HR or Finance.

|**update staff\_update set SALARY =SALARY +6000 where  SALARY <75000 AND  experience>=5 AND DEPARTMENT IN ("HR","Finance") ;**|
|-|





Q13. Apply the following salary revisions in a single statement:



IT → 12%

HR → 9%

Finance → 8%

Sales → 5%

|**update staff\_update set  SALARY =CASE WHEN DEPARTMENT ="IT" THEN SALARY\*1.12 WHEN DEPARTMENT ="HR" THEN SALARY\*1.09 WHEN DEPARTMENT ="Finance" THEN SALARY\*1.08  WHEN DEPARTMENT ="SALES" THEN SALARY\*1.05 ELSE SALARY END;<br />Query OK, 6 rows affected (0.01 sec)<br />Rows matched: 6  Changed: 6  Warnings: 0<br /><br />mysql> select \* from staff\_update ;<br />+----------+------------+------------+---------+----------+------------+------+--------------+----------+<br />\| staff\_id \| staff\_name \| department \| city    \| salary   \| experience \| age  \| joining\_date \| status   \|<br />+----------+------------+------------+---------+----------+------------+------+--------------+----------+<br />\|        1 \| Aarav      \| IT         \| Indore  \| 53760.00 \|          3 \|   26 \| 2022-04-15   \| Active   \|<br />\|        2 \| Bhavna     \| Finance    \| indore  \| 60480.00 \|          5 \|   31 \| 2020-08-20   \| Active   \|<br />\|        3 \| Chetan     \| Finance    \| Delhi   \| 66960.00 \|          7 \|   35 \| 2018-03-10   \| Active   \|<br />\|        4 \| Divya      \| IT         \| Pune    \| 87360.00 \|         10 \|   38 \| 2016-11-05   \| Promoted \|<br />\|        5 \| Eshan      \| Sales      \| Indore  \| 53550.00 \|          4 \|   29 \| 2021-06-18   \| Inactive \|<br />\|        6 \| Farah      \| HR         \| MUMBAI  \| 74120.00 \|          6 \|   34 \| 2019-01-25   \| Active   \|<br />+----------+------------+------------+---------+----------+------------+------+--------------+----------+<br />6 rows in set (0.00 sec)**|
|-|





Q14. Apply salary increments according to experience:



8 or more years → 15%

5–7 years → 10%

3–4 years → 7%

Less than 3 years → 5%

|**update staff\_update set  SALARY =CASE WHEN experience>=8 THEN SALARY\*1.15  WHEN experience BETWEEN 5 AND 7 THEN SALARY\*1.1  WHEN experience BETWEEN 3 AND 4 THEN SALARY\*1.07  ELSE SALARY \* 1.05 END;**|
|-|





Q15. Apply these salary revisions in a single statement:



IT employees with at least 8 years → 18%

Other IT employees → 10%

HR employees with at least 6 years → 12%

Other HR employees → 7%

**Finance** employees → 8%

Sales employees → 5%





|**update staff\_update set  SALARY =CASE WHEN experience>=8 AND DEPARTMENT ="IT" THEN SALARY\*1.18 WHEN DEPARTMENT="IT" THEN SALARY \*1.1 WHEN experience >=6 AND DEPARTMENT ="HR" THEN SALARY\*1.12  WHEN DEPARTMENT="HR" THEN SALARY\*1.07   WHEN  DEPARTMENT ="Finance" THEN SALARY\*1.08  WHEN DEPARTMENT="SALES" THEN SALARY\* 1.05 ELSE SALARY  END;**|
|-|



Q16. Update the status of every employee according to salary:



₹75,000 or more → Senior

₹60,000–₹74,999 → Experienced

₹50,000–₹59,999 → Regular

Below ₹50,000 → Junior

|**update staff\_update set  STATUS =CASE WHEN SALARY >=75000 THEN "Senior"  WHEN SALARY BETWEEN 60000 AND 74999 THEN "Experienced" WHEN SALARY BETWEEN 50000 AND 59999 THEN "REGULAR" ELSE "JUNIOR"END;**|
|-|





Q17. Display all employees with departments arranged in this business priority:



Finance → IT → HR → Sales



Do not change the actual department values.

|**SELECT \* FROM staff\_update ORDER BY CASE WHEN DEPARTMENT = "FINANCE" THEN 1 WHEN DEPARTMENT = "IT" THEN 2 WHEN DEPARTMENT="HR" THEN 3 ELSE 4 END ;<br />+----------+------------+------------+---------+-----------+------------+------+--------------+-------------+<br />\| staff\_id \| staff\_name \| department \| city    \| salary    \| experience \| age  \| joining\_date \| status      \|<br />+----------+------------+------------+---------+-----------+------------+------+--------------+-------------+<br />\|        2 \| Bhavna     \| Finance    \| indore  \|  71850.24 \|          5 \|   31 \| 2020-08-20   \| Experienced \|<br />\|        3 \| Chetan     \| Finance    \| Delhi   \|  79548.48 \|          7 \|   35 \| 2018-03-10   \| Senior      \|<br />\|        1 \| Aarav      \| IT         \| Indore  \|  63275.52 \|          3 \|   26 \| 2022-04-15   \| Experienced \|<br />\|        4 \| Divya      \| IT         \| Pune    \| 118547.52 \|         10 \|   38 \| 2016-11-05   \| Senior      \|<br />\|        6 \| Farah      \| HR         \| MUMBAI  \|  91315.84 \|          6 \|   34 \| 2019-01-25   \| Senior      \|<br />\|        5 \| Eshan      \| Sales      \| Indore  \|  60163.43 \|          4 \|   29 \| 2021-06-18   \| Experienced \|<br />+----------+------------+------------+---------+-----------+------------+------+--------------+-------------+<br />6 rows in set (0.00 sec)**|
|-|



Q18. Display all employees with departments arranged in this order:



IT → HR → Finance → Sales



Within each department, display the employee with the highest salary first.

|**SELECT \* FROM staff\_update ORDER BY CASE WHEN DEPARTMENT = "IT" THEN 1 WHEN DEPARTMENT = "HR" THEN 2 WHEN DEPARTMENT="FINANCE" THEN 3 ELSE 4 END, SALARY DESC ;**|
|-|





Q19. Display employees according to experience priority:



8+ years → 5–7 years → 3–4 years → below 3 years

|**SELECT \* FROM staff\_update ORDER BY CASE WHEN experience>=8 THEN 1 WHEN experience BETWEEN 5 AND 7  THEN 2 WHEN experience BETWEEN 3 AND 4  THEN 3 ELSE 4 END ;**|
|-|





Q20. Give a ₹5,000 increment to only one employee. The employee must belong to IT or HR, have at least 3 years of experience, and earn less than ₹70,000. If multiple employees qualify, update only the lowest-paid employee.

|**update staff\_update set  SALARY =SALARY +5000 WHERE DEPARTMENT IN ("IT","HR") AND experience>=3 AND SALARY <70000 ORDER BY SALARY ASC LIMIT 1;**|
|-|



Q21. Give a 10% increment to only one employee. The employee must be Active and have at least 5 years of experience. If multiple employees qualify, update only the highest-paid employee.

| **update staff\_update set  SALARY =SALARY \*1.1 where status= "active" and experience>=5 order by salary desc limit 1;**|
|-|





Q22. Give a ₹3,000 increment to only one employee who is neither from HR nor Sales and has at least 3 years of experience. If multiple employees qualify, update the lowest-paid employee.

| **update staff\_update set  SALARY =SALARY +3000 where department not in ("hr","sales") and experience>=3 order by salary limit 1;**|
|-|



Q23. Change the status to Promoted for only the highest-paid IT employee.

| update staff\_update set  StaTUS = "Promoted" where DEPARTMENT="IT"  ORDER BY SALARY DESC LIMIT 1;|
|-|





Q24. Give a 12% increment to employees who are either IT employees with at least 5 years of experience or Finance employees earning below ₹65,000. In addition, only Active employees earning below ₹80,000 should receive the increment.

| update staff\_update set  SALARY=SALARY \*1.12 WHERE ((DEPARTMENT="IT" AND EXPERIENCE >=5) OR<br />    -> (DEPARTMENT="FINANCE" AND SALARY <65000)) AND STATUS ="ACTIVE" AND SALARY <80000;|
|-|





Q25. Apply the following salary revision in one statement:



IT + 8 or more years → 18%

IT + 5–7 years → 12%

HR + at least 6 years → 10%

HR + less than 6 years → 7%

Finance + salary below ₹65,000 → 10%

Finance + salary ₹65,000 or above → 7%

Sales + at least 4 years → 6%

All remaining employees → 3%

|update staff\_update set  SALARY = CASE WHEN DEPARTMENT ="IT" AND EXPERIENCE >=8 THEN SALARY\*1.18 WHEN DEPARTMENT ="IT" AND EXPERIENCE BETWEEN 5 AND 7 THEN SALARY \*1.12 WHEN DEPARTMENT ="HR" AND EXPERIENCE >=6 THEN SALARY \*1.1 WHEN DEPARTMENT ="HR" AND EXPERIENCE <6 THEN SALARY \*1.07 WHEN DEPARTMENT ="Finance" AND SALARY <65000 THEN SALARY \*1.1 WHEN DEPARTMENT ="Finance" AND SALARY >=65000 THEN SALARY \*1.07 WHEN DEPARTMENT ="SALES" AND EXPERIENCE >=4 THEN SALARY \*1.06 ELSE SALARY\*1.03 END ;|
|-|





Q26. Update both salary and status according to experience:



8+ years → salary +15%, status Promoted

5–7 years → salary +10%, status Eligible

3–4 years → salary +7%, status Regular

Below 3 years → salary +5%, status Junior

|   **update staff\_update set  SALARY=CASE WHEN EXPERIENCE>=8 THEN SALARY\*1.15  WHEN EXPERIENCE BETWEEN 5 AND 7 THEN SALARY\*1.1  WHEN EXPERIENCE BETWEEN 3 AND 4 THEN SALARY\*1.07  WHEN EXPERIENCE<3 THEN SALARY\*1.05 END ,STATUS=CASE WHEN EXPERIENCE>=8 THEN "Promoted"  WHEN EXPERIENCE BETWEEN 5 AND 7 THEN "Eligible"  WHEN EXPERIENCE BETWEEN 3 AND 4 THEN "Regular"  WHEN EXPERIENCE<3 THEN "Junior" END ;**|
|-|





Q27. Change the status to Promoted for employees who have at least 6 years of experience, salary of at least ₹60,000, are Active, and belong to IT, HR, or Finance.

| UPDATE  staff\_update set STATUS = "Promoted" WHERE EXPERIENCE>=6 AND SALARY >=60000 AND STATUS ="ACTIVE" AND DEPARTMENT IN ("IT","HR","Finance");|
|-|





Q28. Employees belonging to IT, having at least 5 years of experience, and currently living in Pune or Delhi should receive a 10% salary increment, have their city changed to Bangalore, and their status changed to Transferred.

| UPDATE  staff\_update set STATUS = "Transferred" ,CITY = "Bangalore" ,SALARY=SALARY \*1.1 WHERE DEPARTMENT="IT" AND EXPERIENCE>=5 AND CITY IN ("PUNE","DELHI") ;<br />|
|-|





Q29. Give a ₹7,000 special increment to only one eligible employee. The employee must belong to IT, HR, or Finance, have at least 4 years of experience, be Active, and earn less than ₹75,000. If multiple employees qualify, update only the lowest-paid employee.

| UPDATE  staff\_update set SALARY=SALARY +7000 WHERE DEPARTMENT IN ("IT","HR","Finance") AND EXPERIENCE>=4 AND STATUS="ACTIVE" AND SALARY<75000 ORDER BY SALARY LIMIT 1 ;|
|-|



Q30. The company wants to perform an annual salary revision using one statement:



IT + experience >= 8 + salary >= ₹70,000 → 18%

IT + experience >= 5 → 12%

HR + experience >= 6 → 10%

HR + experience < 6 → 7%

Finance + salary < ₹65,000 → 10%

Finance + salary >= ₹65,000 → 7%

Sales + experience >= 4 → 6%

All remaining employees → 3%



Employees whose status is Inactive must not receive any increment.



Additionally, update the status based on the applicable increment:



15% or more → Promoted

10%–14.99% → Eligible

Below 10% → Under Review



| UPDATE  staff\_update set SALARY= CASE when status = "Inactive" then salary WHEN DEPARTMENT ="IT" AND EXPERIENCE>=8 AND SALARY>=70000 THEN SALARY\*1.18 WHEN DEPARTMENT ="IT" AND EXPERIENCE>=5 THEN SALARY\*1.12 WHEN DEPARTMENT ="HR" AND EXPERIENCE>=6  THEN SALARY\*1.1 WHEN DEPARTMENT ="HR" AND EXPERIENCE<6 THEN SALARY\*1.07 WHEN DEPARTMENT ="Finance" AND SALARY<65000 THEN SALARY\*1.1 WHEN DEPARTMENT ="Finance" AND SALARY>=65000 THEN SALARY\*1.07 WHEN DEPARTMENT ="SALES" AND EXPERIENCE>=4  THEN SALARY\*1.06  ELSE SALARY \*1.03 END , STATUS = CASE when status = "Inactive" then STATUS when department = "IT" and experience >= 8 and salary >= 70000 then "Promoted" when department = "IT" and experience >= 5 then "Eligible" when department = "HR" and experience >= 6 then "Eligible" when department = "Finance" and salary < 65000 then "Eligible" else "Under Review" END ;|
|-|



