QNO 1:

A company wants to manage its employees and their respective departments. Each employee must belong to a department. If a department is deleted, all employees in that department should also be removed automatically.

Tasks:

1\. Create the Departments Table

Each department has a unique ID (DepartmentID).

The department name must be unique.

The department name cannot be NULL.

| create table Departments(DepartmentID int PRIMARY KEy,dname varchar(50) not null unique);<br />Query OK, 0 rows affected (0.08 sec)<br />|
|-|



2\. Create the Employees Table

Each employee has a unique ID (EmployeeID).

Each employee has a name and salary, both cannot be NULL.

Each employee must be assigned to a department (DepartmentID), which is a FOREIGN KEY referencing Departments(DepartmentID).

If a department is deleted, all employees in that department should also be deleted.

| create table Employees\_31oct(EmployeeID int PRIMARY KEy ,ename varchar (30) not null , esalary decimal (10,2) not null , Departmentno int  not null ,foreign key (Departmentno) references Departments(DepartmentID) on delete cascade );<br />Query OK, 0 rows affected (0.08 sec)|
|-|



3\. Insert Sample Data

Insert at least 3 departments.

|<br />mysql> INSERT INTO Departments (DepartmentID, dname)<br />    -> VALUES<br />    -> (101, 'IT'),<br />    -> (102, 'HR'),<br />    -> (103, 'Finance');<br />Query OK, 3 rows affected (0.01 sec)<br />Records: 3  Duplicates: 0  Warnings: 0|
|-|



Insert at least 5 employees (make sure at least two employees belong to the same department).

| INSERT INTO Employees\_31oct<br />    -> (EmployeeID, ename, esalary, Departmentno)<br />    -> VALUES<br />    -> (1, 'aman', 45000, 101),<br />    -> (2, 'ajay', 50000, 101),<br />    -> (3, "nit", 35000, 102),<br />    -> (4, 'aryan', 40000, 102),<br />    -> (5, 'Kp', 55000, 103);<br />Query OK, 5 rows affected (0.01 sec)<br />Records: 5  Duplicates: 0  Warnings: 0|
|-|



4\. Implement Query Constraints (Without Using JOIN)

Write a query to list all employees and their department names (without using JOIN).

|SELECT e.ename, d.dname<br />FROM Employees\_31oct e, Departments d<br />WHERE e.Departmentno = d.DepartmentID;|
|-|



Write a query to update an employee's department.

|UPDATE Employees\_31oct set Departmentno = 103 WHERE EmployeeID = 1;|
|-|



Try deleting a department and observe what happens to the employees under that department.

| select \* from Departments ;<br />+--------------+---------+<br />\| DepartmentID \| dname   \|<br />+--------------+---------+<br />\|          103 \| Finance \|<br />\|          102 \| HR      \|<br />+--------------+---------+<br />2 rows in set (0.00 sec)<br /><br />mysql> select \* from Employees\_31oct ;<br />+------------+-------+----------+--------------+<br />\| EmployeeID \| ename \| esalary  \| Departmentno \|<br />+------------+-------+----------+--------------+<br />\|          3 \| nit   \| 35000.00 \|          102 \|<br />\|          4 \| aryan \| 40000.00 \|          102 \|<br />\|          5 \| Kp    \| 55000.00 \|          103 \|<br />+------------+-------+----------+--------------+<br />3 rows in set (0.00 sec)|
|-|





