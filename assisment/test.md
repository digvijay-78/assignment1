Employee Management System(3.5)



Write SQL queries for all the following questions using the `employees` table and sample data provided below.



Table: `employees`



Columns: `employee\\\_id`, `employee\\\_name`, `department`, `city`, `salary`, `joining\\\_date`, `experience`, `age`, `gender`,

&#x20;`employment\\\_type`, `skills`, `email`, `manager\\\_id`



Sample Data



| employee\_id | employee\_name | department | city | salary | joining\_date | experience | age | gender | employment\_type | skills | email | manager\_id |

|---:|---|---|---|---:|---|---:|---:|---|---|---|---|---:|

| 101 | Amit Sharma | IT | Indore | 75000 | 2023-05-10 | 5 | 30 | MALE | FULL\_TIME | JAVA,SQL,SPRING | amit@company.com | 501 |

| 102 | Sneha Patel | Finance | Pune | 65000 | 2024-02-15 | 4 | 28 | FEMALE | FULL\_TIME | SQL,PYTHON | sneha@company.com | 502 |

| 103 | Rahul Verma | Development | Delhi | 85000 | 2022-08-20 | 7 | 32 | MALE | FULL\_TIME | JAVA,SQL,REACT | rahul@company.com | 501 |

| 104 | Anjali Gupta | HR | Mumbai | 35000 | 2023-11-01 | 3 | 27 | FEMALE | CONTRACT | SQL | NULL | 503 |

| 105 | Suresh Kumar | IT | Bhopal | 28000 | 2021-06-12 | 6 | 35 | MALE | FULL\_TIME | JAVA,SPRING | NULL | NULL |

| 106 | Priya Singh | Development | Indore | 95000 | 2025-01-10 | 4 | 29 | FEMALE | FULL\_TIME | PYTHON,REACT,SQL | priya@company.com | 501 |

| 107 | Arjun Mehta | Finance | Delhi | 45000 | 2022-03-25 | 3 | 26 | MALE | PART\_TIME | SQL,PYTHON | arjun@company.com | NULL |

| 108 | Simran Kaur | IT | Pune | 55000 | 2024-07-18 | 5 | 31 | FEMALE | FULL\_TIME | JAVA,SQL,REACT | simran@company.com | 504 |



Note: The `skills` column is a MySQL `SET` column. Use appropriate conditions to check individual skills.



Questions



Q1. (0.5 Marks)



Display employees belonging to IT, Finance, or Development whose salary is between ₹40,000 and ₹90,000, experience is greater than 3 years, email and manager ID are both NOT NULL, and city is neither Mumbai nor Bhopal.

|SELECT \* FROM employees WHERE DEPARTMENT IN("IT","Finance","Development") AND SALARY BETWEEN 40000 AND 90000 AND experience >3  AND CITY NOT IN ("MUMBAI","BHOPAL");<br />+-------------+---------------+-------------+--------+----------+--------------+------------+------+--------+-----------------+-----------------+--------------------+------------+<br />\| employee\_id \| employee\_name \| department  \| city   \| salary   \| joining\_date \| experience \| age  \| gender \| employment\_type \| skills          \| email              \| manager\_id \|<br />+-------------+---------------+-------------+--------+----------+--------------+------------+------+--------+-----------------+-----------------+--------------------+------------+<br />\|         101 \| Amit Sharma   \| IT          \| Indore \| 75000.00 \| 2023-05-10   \|          5 \|   30 \| male   \| FULL\_TIME       \| JAVA,SQL,SPRING \| amit@company.com   \|        501 \|<br />\|         102 \| Sneha Patel   \| Finance     \| Pune   \| 65000.00 \| 2024-02-15   \|          4 \|   28 \| female \| FULL\_TIME       \| SQL,python      \| sneha@company.com  \|        502 \|<br />\|         103 \| Rahul Verma   \| Development \| Delhi  \| 85000.00 \| 2022-08-20   \|          7 \|   32 \| male   \| FULL\_TIME       \| JAVA,SQL,react  \| rahul@company.com  \|        501 \|<br />\|         108 \| Simran Kaur   \| IT          \| Pune   \| 55000.00 \| 2024-07-18   \|          5 \|   31 \| female \| FULL\_TIME       \| JAVA,SQL,react  \| simran@company.com \|        504 \|<br />+-------------+---------------+-------------+--------+----------+--------------+------------+------+--------+-----------------+-----------------+--------------------+------------+<br />4 rows in set (0.00 sec)|
|-|



Q2. (0.5 Marks)



Display employees whose names start with 'A' or contain the letter 'a', who joined after '2023-01-01', and whose salary is greater than ₹50,000 OR experience is greater than 6 years. Exclude employees from HR and Mumbai.

|SELECT \* FROM employees WHERE employee\_name LIKE("%A%") AND joining\_date>"2023-01-01" AND (SALARY>50000 OR experience>6 )  AND CITY !="MUMBAI" AND DEPARTMENT != "HR";<br />+-------------+---------------+-------------+--------+----------+--------------+------------+------+--------+-----------------+------------------+--------------------+------------+<br />\| employee\_id \| employee\_name \| department  \| city   \| salary   \| joining\_date \| experience \| age  \| gender \| employment\_type \| skills           \| email              \| manager\_id \|<br />+-------------+---------------+-------------+--------+----------+--------------+------------+------+--------+-----------------+------------------+--------------------+------------+<br />\|         101 \| Amit Sharma   \| IT          \| Indore \| 75000.00 \| 2023-05-10   \|          5 \|   30 \| male   \| FULL\_TIME       \| JAVA,SQL,SPRING  \| amit@company.com   \|        501 \|<br />\|         102 \| Sneha Patel   \| Finance     \| Pune   \| 65000.00 \| 2024-02-15   \|          4 \|   28 \| female \| FULL\_TIME       \| SQL,python       \| sneha@company.com  \|        502 \|<br />\|         106 \| Priya Singh   \| Development \| Indore \| 95000.00 \| 2025-01-10   \|          4 \|   29 \| female \| FULL\_TIME       \| SQL,python,react \| priya@company.com  \|        501 \|<br />\|         108 \| Simran Kaur   \| IT          \| Pune   \| 55000.00 \| 2024-07-18   \|          5 \|   31 \| female \| FULL\_TIME       \| JAVA,SQL,react   \| simran@company.com \|        504 \|<br />+-------------+---------------+-------------+--------+----------+--------------+------------+------+--------+-----------------+------------------+--------------------+------------+<br />4 rows in set (0.01 sec)|
|-|







Q3. (0.5 Marks)



Display FULL\_TIME employees from IT or Development who have \*\*both JAVA and SQL skills or both PYTHON and REACT skills\*\*, earn more than ₹60,000, and have a non-NULL email.

|SELECT \* FROM employees WHERE employment\_type ="FULL\_TIME" AND DEPARTMENT IN("IT","Development") AND (FIND\_IN\_SET ("JAVA",SKILLS)>0 AND FIND\_IN\_SET ("SQL",SKILLS)>0) OR (FIND\_IN\_SET ("PYTHON",SKILLS)>0 AND FIND\_IN\_SET ("REACT",SKILLS)>0) AND SALARY > 60000 AND EMAIL !=NULL;<br />+-------------+---------------+-------------+--------+----------+--------------+------------+------+--------+-----------------+-----------------+--------------------+------------+<br />\| employee\_id \| employee\_name \| department  \| city   \| salary   \| joining\_date \| experience \| age  \| gender \| employment\_type \| skills          \| email              \| manager\_id \|<br />+-------------+---------------+-------------+--------+----------+--------------+------------+------+--------+-----------------+-----------------+--------------------+------------+<br />\|         101 \| Amit Sharma   \| IT          \| Indore \| 75000.00 \| 2023-05-10   \|          5 \|   30 \| male   \| FULL\_TIME       \| JAVA,SQL,SPRING \| amit@company.com   \|        501 \|<br />\|         103 \| Rahul Verma   \| Development \| Delhi  \| 85000.00 \| 2022-08-20   \|          7 \|   32 \| male   \| FULL\_TIME       \| JAVA,SQL,react  \| rahul@company.com  \|        501 \|<br />\|         108 \| Simran Kaur   \| IT          \| Pune   \| 55000.00 \| 2024-07-18   \|          5 \|   31 \| female \| FULL\_TIME       \| JAVA,SQL,react  \| simran@company.com \|        504 \|<br />+-------------+---------------+-------------+--------+----------+--------------+------------+------+--------+-----------------+-----------------+--------------------+------------+<br />3 rows in set (0.00 sec)|
|-|





Q4. (0.5 Marks)



Display employees from IT, Finance, or HR whose age is between 25 and 40, salary is NOT between ₹30,000 and ₹60,000, experience is greater than 2 years, and city is neither Mumbai nor Bhopal.]

|SELECT \* FROM employees WHERE DEPARTMENT IN ("IT","FINANCE","HR") AND AGE BETWEEN 25 AND 40 AND SALARY NOT BETWEEN 30000 AND 60000 AND experience >2 AND CITY NOT IN ("BHOPAL","MUMBAI");<br />+-------------+---------------+------------+--------+----------+--------------+------------+------+--------+-----------------+-----------------+-------------------+------------+<br />\| employee\_id \| employee\_name \| department \| city   \| salary   \| joining\_date \| experience \| age  \| gender \| employment\_type \| skills          \| email             \| manager\_id \|<br />+-------------+---------------+------------+--------+----------+--------------+------------+------+--------+-----------------+-----------------+-------------------+------------+<br />\|         101 \| Amit Sharma   \| IT         \| Indore \| 75000.00 \| 2023-05-10   \|          5 \|   30 \| male   \| FULL\_TIME       \| JAVA,SQL,SPRING \| amit@company.com  \|        501 \|<br />\|         102 \| Sneha Patel   \| Finance    \| Pune   \| 65000.00 \| 2024-02-15   \|          4 \|   28 \| female \| FULL\_TIME       \| SQL,python      \| sneha@company.com \|        502 \|<br />+-------------+---------------+------------+--------+----------+--------------+------------+------+--------+-----------------+-----------------+-------------------+------------+<br />2 rows in set (0.00 sec)|
|-|





Q5. (0.5 Marks)



Display employees who joined between '2022-01-01' and '2025-12-31', have JAVA or PYTHON skills, earn more than ₹45,000, and have either email or manager ID as NULL. Their experience must be greater than 3 years.

|SELECT \* FROM employees WHERE joining\_date BETWEEN '2022-01-01' AND '2025-12-31' AND SALARY > 45000 AND manager\_id!= NULL AND experience>3 AND FIND\_IN\_SET ("JAVA",SKILLS)>0  OR FIND\_IN\_SET ("PYTHON",SKILLS)>0;<br />+-------------+---------------+-------------+--------+----------+--------------+------------+------+--------+-----------------+------------------+-------------------+------------+<br />\| employee\_id \| employee\_name \| department  \| city   \| salary   \| joining\_date \| experience \| age  \| gender \| employment\_type \| skills           \| email             \| manager\_id \|<br />+-------------+---------------+-------------+--------+----------+--------------+------------+------+--------+-----------------+------------------+-------------------+------------+<br />\|         102 \| Sneha Patel   \| Finance     \| Pune   \| 65000.00 \| 2024-02-15   \|          4 \|   28 \| female \| FULL\_TIME       \| SQL,python       \| sneha@company.com \|        502 \|<br />\|         106 \| Priya Singh   \| Development \| Indore \| 95000.00 \| 2025-01-10   \|          4 \|   29 \| female \| FULL\_TIME       \| SQL,python,react \| priya@company.com \|        501 \|<br />\|         107 \| Arjun Mehta   \| Finance     \| Delhi  \| 45000.00 \| 2022-03-25   \|          3 \|   26 \| male   \| PART\_TIME       \| SQL,python       \| arjun@company.com \|       NULL \|<br />+-------------+---------------+-------------+--------+----------+--------------+------------+------+--------+-----------------+------------------+-------------------+------------+<br />3 rows in set (0.00 sec)|
|-|





Q6. (0.5 Marks)



Display employees whose names start with 'S' or contain the letter 'a', belong to IT or Finance, earn between ₹40,000 and ₹1,00,000, have more than 2 years of experience, and have both email and manager ID NOT NULL. They must have JAVA or PYTHON skills. Display the results ordered by department in ascending order and salary in descending order.

|SELECT \* FROM employees WHERE employee\_name LIKE ("S%") OR employee\_name LIKE ("%A%") AND DEPARTMENT IN ("IT","Finance") AND SALARY BETWEEN 40000 AND 100000 AND  experience > 2  AND FIND\_IN\_SET ("JAVA",SKILLS)>0  OR FIND\_IN\_SET ("PYTHON",SKILLS)>0 AND manager\_id !=NULL ORDER BY SALARY;<br />+-------------+---------------+------------+--------+----------+--------------+------------+------+--------+-----------------+-----------------+--------------------+------------+<br />\| employee\_id \| employee\_name \| department \| city   \| salary   \| joining\_date \| experience \| age  \| gender \| employment\_type \| skills          \| email              \| manager\_id \|<br />+-------------+---------------+------------+--------+----------+--------------+------------+------+--------+-----------------+-----------------+--------------------+------------+<br />\|         108 \| Simran Kaur   \| IT         \| Pune   \| 55000.00 \| 2024-07-18   \|          5 \|   31 \| female \| FULL\_TIME       \| JAVA,SQL,react  \| simran@company.com \|        504 \|<br />\|         102 \| Sneha Patel   \| Finance    \| Pune   \| 65000.00 \| 2024-02-15   \|          4 \|   28 \| female \| FULL\_TIME       \| SQL,python      \| sneha@company.com  \|        502 \|<br />\|         101 \| Amit Sharma   \| IT         \| Indore \| 75000.00 \| 2023-05-10   \|          5 \|   30 \| male   \| FULL\_TIME       \| JAVA,SQL,SPRING \| amit@company.com   \|        501 \|<br />+-------------+---------------+------------+--------+----------+--------------+------------+------+--------+-----------------+-----------------+--------------------+------------+<br />3 rows in set (0.00 sec)<br />|
|-|





NOTE: Table creation and insertion will be .5 marks



=====================================







(101, 'Amit Sharma', 'IT', 'Indore', 75000, '2023-05-10', 5, 30, 'MALE', 'FULL\_TIME', 'JAVA,SQL,SPRING', 'amit@company.com', 501),



(102, 'Sneha Patel', 'Finance', 'Pune', 65000, '2024-02-15', 4, 28, 'FEMALE', 'FULL\_TIME', 'SQL,PYTHON', 'sneha@company.com', 502),



(103, 'Rahul Verma', 'Development', 'Delhi', 85000, '2022-08-20', 7, 32, 'MALE', 'FULL\_TIME', 'JAVA,SQL,REACT', 'rahul@company.com', 501),



(104, 'Anjali Gupta', 'HR', 'Mumbai', 35000, '2023-11-01', 3, 27, 'FEMALE', 'CONTRACT', 'SQL', NULL, 503),



(105, 'Suresh Kumar', 'IT', 'Bhopal', 28000, '2021-06-12', 6, 35, 'MALE', 'FULL\_TIME', 'JAVA,SPRING', NULL, NULL),



(106, 'Priya Singh', 'Development', 'Indore', 95000, '2025-01-10', 4, 29, 'FEMALE', 'FULL\_TIME', 'PYTHON,REACT,SQL', 'priya@company.com', 501),



(107, 'Arjun Mehta', 'Finance', 'Delhi', 45000, '2022-03-25', 3, 26, 'MALE', 'PART\_TIME', 'SQL,PYTHON', 'arjun@company.com', NULL),



(108, 'Simran Kaur', 'IT', 'Pune', 55000, '2024-07-18', 5, 31, 'FEMALE', 'FULL\_TIME', 'JAVA,SQL,REACT', 'simran@company.com', 504);

