1\.

Create a table named Students with the following columns:



StudentID (INT, Primary Key)

Name (VARCHAR(50), NOT NULL)

Age (INT, should be between 18 and 25)

Marks (DECIMAL(5,2), should be between 0 and 100)

Insert the following records and observe what happens:



(101, 'Alice', 20, 85.5)

(102, 'Bob', 17, 90.0) (This should fail due to Age constraint)

(103, 'Charlie', 22, 105.0) (This should fail due to Marks constraint)

(104, 'David', 24, 75.0)



|create table Students (StudentID INT Primary Key,Name VARCHAR(50) NOT NULL, age int check (age between 18 and 25), marks decimal (5,2) check (marks between 0 and 100 ));<br />Query OK, 0 rows affected (0.06 sec)<br /><br />mysql> insert into Students values (101, 'Alice', 20, 85.5);<br />Query OK, 1 row affected (0.03 sec)<br /><br />mysql> select \* from students;<br />+-----------+-------+------+-------+<br />\| StudentID \| Name  \| age  \| marks \|<br />+-----------+-------+------+-------+<br />\|       101 \| Alice \|   20 \| 85.50 \|<br />+-----------+-------+------+-------+<br />1 row in set (0.00 sec)<br /><br />mysql> insert into Students values (102, 'Bob', 17, 90.0);<br />ERROR 3819 (HY000): Check constraint 'students\_chk\_1' is violated.<br />mysql> insert into Students values (103, 'Charlie', 22, 105.0);<br />ERROR 3819 (HY000): Check constraint 'students\_chk\_2' is violated.<br />mysql> insert into Students values (104, 'David', 24, 75.0);<br />Query OK, 1 row affected (0.01 sec)<br /><br />mysql> select \* from students;<br />+-----------+-------+------+-------+<br />\| StudentID \| Name  \| age  \| marks \|<br />+-----------+-------+------+-------+<br />\|       101 \| Alice \|   20 \| 85.50 \|<br />\|       104 \| David \|   24 \| 75.00 \|<br />+-----------+-------+------+-------+<br />2 rows in set (0.00 sec)|
|-|



