3\.

NOTE:USE TABLE from QNO 1:Table: employees



Find the total number of employees in each department and display only those departments having more than 2 employees. (GROUP BY + HAVING)

|select department,count(\*) as c from employees28oct group by department having c>2;<br />+------------+---+<br />\| department \| c \|<br />+------------+---+<br />\| HR         \| 3 \|<br />\| IT         \| 4 \|<br />\| Finance    \| 3 \|<br />+------------+---+;|
|-|



Find the total salary paid in each department and display the results in descending order of total salary. (GROUP BY + ORDER BY)

|select department,sum(salary) as c from employees28oct group by department order by c desc;<br />+------------+----------+<br />\| department \| c        \|<br />+------------+----------+<br />\| IT         \| 19800.00 \|<br />\| Finance    \| 17500.00 \|<br />\| HR         \| 14200.00 \|<br />+------------+----------+|
|-|



Find the job role that has the highest total salary payout, displaying only roles where total salary is above 10,000. (GROUP BY + HAVING + ORDER BY)

|select job\_role,sum(salary) as c from employees28oct group by job\_role having c>10000 order by c desc limit 1;<br />+----------+----------+<br />\| job\_role \| c        \|<br />+----------+----------+<br />\| Manager  \| 13000.00 \|<br />+----------+----------+|
|-|



Find the average salary of employees who joined after 2022, displaying only job roles where the average salary is above 4500. (WHERE + GROUP BY + HAVING)

|select job\_role,avg(salary) as c from employees28oct where hire\_date >"2022-12-31" group by job\_role having c>4500 ;<br />+----------+-------------+<br />\| job\_role \| c           \|<br />+----------+-------------+<br />\| Tester   \| 4650.000000 \|<br />\| Manager  \| 7000.000000 \|<br />+----------+-------------+|
|-|



Find departments where the total salary exceeds 10,000 and order the results in ascending order of department name. (GROUP BY + HAVING + ORDER BY)

|select department,sum(salary) as c from employees28oct group by department having c> 10000 order by department ;<br />+------------+----------+<br />\| department \| c        \|<br />+------------+----------+<br />\| Finance    \| 17500.00 \|<br />\| HR         \| 14200.00 \|<br />\| IT         \| 19800.00 \|<br />+------------+----------+|
|-|









4\.



Find the average marks in each subject and display only subjects where the average is above 80. (GROUP BY + HAVING)

| select subject,avg(marks) as a from students28oct group by subject having a>80;<br />+---------+---------+<br />\| subject \| a       \|<br />+---------+---------+<br />\| Math    \| 88.0000 \|<br />+---------+---------+<br />1 row in set (0.01 sec)|
|-|



Find the total number of students in each class and order them by class in descending order. (GROUP BY + ORDER BY)

| select class,count(\*) as a from students28oct group by class order by class desc;<br />+-------+---+<br />\| class \| a \|<br />+-------+---+<br />\|    10 \| 5 \|<br />\|     9 \| 5 \|<br />+-------+---+|
|-|



Find the subject where students scored the highest average marks, displaying only subjects where the average is above 85. (GROUP BY + HAVING + ORDER BY)

|<br /> select subject,avg(marks) as a from students28oct group by subject having a>85 order by a desc limit 1;<br />+---------+---------+<br />\| subject \| a       \|<br />+---------+---------+<br />\| Math    \| 88.0000 \|<br />+---------+---------+<br />1 row in set (0.00 sec)|
|-|



Find the student who scored the highest marks overall. (ORDER BY + LIMIT 1)

|  select \* from students28oct order by marks desc limit 1 ;<br />+------------+-------+-------+---------+-------+------------+<br />\| student\_id \| name  \| class \| subject \| marks \| exam\_date  \|<br />+------------+-------+-------+---------+-------+------------+<br />\|          3 \| Rohit \|     9 \| Math    \|    92 \| 2023-04-20 \|<br />+------------+-------+-------+---------+-------+------------+<br />1 row in set (0.00 sec)|
|-|



Find the number of students in each class who scored more than 85, displaying only classes with more than 2 such students. (GROUP BY + HAVING)

| select class,count(\*) as a from students28oct where marks>85 group by class having a>2 ;|
|-|



