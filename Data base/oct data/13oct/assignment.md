QNO  1: Create and Populate students Table

Columns:



id INT



name VARCHAR(100)



age INT



gender VARCHAR(10)



address VARCHAR(150)



phone VARCHAR(15)



email VARCHAR(100)

|CREATE TABLE students (<br />    id INT,<br />    name VARCHAR(100),<br />    age INT,<br />    gender VARCHAR(10),<br />    address VARCHAR(150),<br />    phone VARCHAR(15),<br />    email VARCHAR(100)<br />);<br /><br />INSERT INTO students<br />VALUES<br />(1, 'Aman Sharma', 20, 'Male', 'Indore', '9876543210', 'aman@gmail.com'),<br />(2, 'Priya Verma', 21, 'Female', 'Bhopal', '9876543211', 'priya@gmail.com'),<br />(3, 'Rahul Patel', 22, 'Male', 'Ujjain', '9876543212', 'rahul@gmail.com'),<br />(4, 'Neha Singh', 20, 'Female', 'Indore', '9876543213', 'neha@gmail.com'),<br />(5, 'Rohit Jain', 23, 'Male', 'Dewas', '9876543214', 'rohit@gmail.com');<br /><br /><br />SELECT \* FROM students;<br />mysql> SELECT \* FROM students;<br />+------+-------------+------+--------+---------+------------+-----------------+<br />\| id   \| name        \| age  \| gender \| address \| phone      \| email           \|<br />+------+-------------+------+--------+---------+------------+-----------------+<br />\|    1 \| Aman Sharma \|   20 \| Male   \| Indore  \| 9876543210 \| aman@gmail.com  \|<br />\|    2 \| Priya Verma \|   21 \| Female \| Bhopal  \| 9876543211 \| priya@gmail.com \|<br />\|    3 \| Rahul Patel \|   22 \| Male   \| Ujjain  \| 9876543212 \| rahul@gmail.com \|<br />\|    4 \| Neha Singh  \|   20 \| Female \| Indore  \| 9876543213 \| neha@gmail.com  \|<br />\|    5 \| Rohit Jain  \|   23 \| Male   \| Dewas   \| 9876543214 \| rohit@gmail.com \|<br />+------+-------------+------+--------+---------+------------+-----------------+<br />5 rows in set (0.00 sec)|
|-|



Task:



Insert 5 different student records with dummy data.







QNO  2: Create and Populate books Table

Columns:



book\_id INT



title VARCHAR(150)



author VARCHAR(100)



genre VARCHAR(50)



publication\_year INT



price DECIMAL(6,2)



publisher VARCHAR(100)



Task:



Insert 4 book records.



QNO  3: ALTER students Table

Task:



Add a column dob DATE



Rename column phone to mobile\_number



Modify column age to SMALLINT



Drop column email



QNO  4: RENAME Table

Task:



Rename books table to library\_books



QNO  5: TRUNCATE Table

Task:



Truncate all data from students table



QNO  6: DROP Table

Task:



Drop the library\_books table



QNO  7: Create and Insert into products Table

Columns:



product\_id INT



product\_name VARCHAR(100)



category VARCHAR(50)



price DECIMAL(7,2)



stock\_quantity INT



supplier\_name VARCHAR(100)



manufacture\_date DATE



expiry\_date DATE



Task:



Insert 6 products (some with expiry dates, some without)



QNO  8: Create and Insert into employees Table

Columns:



emp\_id INT



emp\_name VARCHAR(100)



gender VARCHAR(10)



dob DATE



department VARCHAR(100)



position VARCHAR(100)



salary DECIMAL(8,2)



joining\_date DATE



phone VARCHAR(15)



Task:



Insert 5 employee records









QNO 9:





You are designing a system to store movie reviews. Start with basic details and then evolve the table structure using ALTER, RENAME, TRUNCATE, and DROP, and perform INSERT operations at each stage.



&#x20;Initial Table Creation:

Create a table movie\_reviews with the following columns:



review\_id INT



movie\_title VARCHAR(150)



reviewer\_name VARCHAR(100)



rating DECIMAL(2,1)



review\_text TEXT



&#x20;Insert 3 sample movie reviews



Step 1: Add More Columns (ALTER)

Add the following columns using ALTER:



review\_date DATE



platform VARCHAR(50) — (e.g., IMDb, Rotten Tomatoes)



likes INT



&#x20;Insert 2 more rows with new columns



&#x20;Step 2: Rename a Column

Rename the column reviewer\_name to critic\_name



&#x20;Step 3: Modify Column Types

Modify:



rating to DECIMAL(3,1)



movie\_title to VARCHAR(200)



&#x20;Step 4: Drop an Unnecessary Column

Drop the likes column



&#x20;Step 5: Truncate the Table

Truncate the table so all data is removed



&#x20;Step 6: Rename the Table

Rename movie\_reviews to archived\_reviews



&#x20;Step 7: Drop the Table

Finally, drop the archived\_reviews table

