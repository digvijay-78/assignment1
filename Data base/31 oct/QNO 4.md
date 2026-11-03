QNO 4:

A university wants to track students' exam results. If a student is deleted, their results should also be deleted.

Tasks:

Create a Students table:

StudentID (PRIMARY KEY, AUTO\_INCREMENT)

StudentName (NOT NULL)

|CREATE TABLE Students\_31OCT (StudentID INT PRIMARY KEY AUTO\_INCREMENT,StudentName VARCHAR (50) NOT NULL);<br />Query OK, 0 rows affected (0.03 sec)|
|-|



Create an Exams table:

ExamID (PRIMARY KEY, AUTO\_INCREMENT)

SubjectName (NOT NULL, UNIQUE)

| CREATE TABLE Exams\_31OCT (ExamID INT PRIMARY KEY AUTO\_INCREMENT,SubjectName VARCHAR(50) NOT NULL UNIQUE);<br />Query OK, 0 rows affected (0.06 sec)|
|-|



Create a Results table:

ResultID (PRIMARY KEY, AUTO\_INCREMENT)

StudentID (FOREIGN key)

ExamID (FOREIGN KEY)

Score (NOT NULL, CHECK Score BETWEEN 0 AND 100)

|CREATE TABLE Results\_31OCT (ResultID INT PRIMARY KEY AUTO\_INCREMENT,StudentID INT ,ExamID INT , Score INT NOT NULL CHECK (Score BETWEEN 0 AND 100),FOREIGN key (StudentID) REFERENCES Students\_31OCT(StudentID) ON DELETE CASCADE ,FOREIGN key (ExamID) REFERENCES Exams\_31OCT (ExamID));<br />Query OK, 0 rows affected (0.06 sec)|
|-|



Insert sample data (at least 3 students, 3 exams, and 5 results).

|SELECT \* FROM Students\_31OCT;<br />+-----------+-------------+<br />\| StudentID \| StudentName \|<br />+-----------+-------------+<br />\|         1 \| Aman        \|<br />\|         2 \| ARY         \|<br />\|         3 \| NIT         \|<br />+-----------+-------------+<br />3 rows in set (0.00 sec)<br /><br />mysql><br />mysql> SELECT \* FROM Exams\_31OCT;<br />+--------+-----------------+<br />\| ExamID \| SubjectName     \|<br />+--------+-----------------+<br />\|      3 \| Data Structures \|<br />\|      2 \| DBMS            \|<br />\|      1 \| Python          \|<br />+--------+-----------------+<br />3 rows in set (0.00 sec)<br /><br />mysql><br />mysql> SELECT \* FROM Results\_31OCT;<br />+----------+-----------+--------+-------+<br />\| ResultID \| StudentID \| ExamID \| Score \|<br />+----------+-----------+--------+-------+<br />\|        1 \|         1 \|      1 \|    85 \|<br />\|        2 \|         1 \|      2 \|    90 \|<br />\|        3 \|         2 \|      1 \|    78 \|<br />\|        4 \|         2 \|      3 \|    88 \|<br />\|        5 \|         3 \|      2 \|    95 \|<br />+----------+-----------+--------+-------+<br />5 rows in set (0.00 sec)|
|-|



Delete a student and check if their results are removed automatically.

| **DELETE FROM Students\_31OCT WHERE StudentID =2;<br />Query OK, 1 row affected (0.01 sec)<br /><br />mysql> SELECT \* FROM Students\_31OCT;<br />+-----------+-------------+<br />\| StudentID \| StudentName \|<br />+-----------+-------------+<br />\|         1 \| Aman        \|<br />\|         3 \| NIT         \|<br />+-----------+-------------+<br />2 rows in set (0.00 sec)<br /><br />mysql> SELECT \* FROM Results\_31OCT;<br />+----------+-----------+--------+-------+<br />\| ResultID \| StudentID \| ExamID \| Score \|<br />+----------+-----------+--------+-------+<br />\|        1 \|         1 \|      1 \|    85 \|<br />\|        2 \|         1 \|      2 \|    90 \|<br />\|        5 \|         3 \|      2 \|    95 \|<br />+----------+-----------+--------+-------+<br />3 rows in set (0.00 sec)**|
|-|



Update an exam’s subject name and observe the effect.

|<br />mysql> SELECT \* FROM Exams\_31OCT;<br />+--------+-----------------+<br />\| ExamID \| SubjectName     \|<br />+--------+-----------------+<br />\|      1 \| Advanced Python \|<br />\|      3 \| Data Structures \|<br />\|      2 \| DBMS            \|<br />+--------+-----------------+<br />3 rows in set (0.00 sec)<br /><br />mysql> SELECT \* FROM Results\_31OCT;<br />+----------+-----------+--------+-------+<br />\| ResultID \| StudentID \| ExamID \| Score \|<br />+----------+-----------+--------+-------+<br />\|        1 \|         1 \|      1 \|    85 \|<br />\|        2 \|         1 \|      2 \|    90 \|<br />\|        5 \|         3 \|      2 \|    95 \|<br />+----------+-----------+--------+-------+<br />3 rows in set (0.00 sec)|
|-|



