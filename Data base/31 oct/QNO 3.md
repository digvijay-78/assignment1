QNO 3:

A library maintains a record of books and their authors. If an author is removed, their books should not be deleted, but their author information should be set to NULL.



Tasks:

Create an Authors table:



AuthorID (PRIMARY KEY, AUTO\_INCREMENT)

AuthorName (NOT NULL, UNIQUE)

| create table Authors\_31oct (AuthorID int PRIMARY KEY AUTO\_INCREMENT,AuthorName varchar (50) NOT NULL UNIQUE);<br />Query OK, 0 rows affected (0.10 sec)|
|-|





Create a Books table:

BookID int PRIMARY KEY AUTO\_INCREMENT

BookTitle (NOT NULL, UNIQUE)

AuthorID (FOREIGN KEY )

|create table Books\_31oct (BookID int PRIMARY KEY AUTO\_INCREMENT,BookTitle VARCHAR(50) NOT NULL UNIQUE,AuthorID INT ,FOREIGN KEY (AuthorID) REFERENCES Authors\_31oct (AuthorID) ON DELETE SET NULL);<br />Query OK, 0 rows affected (0.08 sec)|
|-|



Insert sample data (at least 3 authors and 5 books).

|<br />mysql> INSERT INTO Authors\_31oct (AuthorName)<br />    -> VALUES<br />    -> ('Chetan Bhagat'),<br />    -> ('Ravinder Singh'),<br />    -> ('WILLAM CHETAN');<br />Query OK, 3 rows affected (0.02 sec)<br />Records: 3  Duplicates: 0  Warnings: 0<br /><br />mysql> INSERT INTO Books\_31oct (BookTitle, AuthorID)<br />    -> VALUES<br />    -> ('Five Point Someone', 1),<br />    -> ('GOOD BYE SAM', 1),<br />    -> ('HARRY POTTER', 2),<br />    -> ('The Immortals of Meluha', 3),<br />    -> ('The Secret of the Nagas', 3);<br />Query OK, 5 rows affected (0.01 sec)<br />Records: 5  Duplicates: 0  Warnings: 0<br />|
|-|



Delete an author and check if books remain, but the AuthorID is set to NULL.

|DELETE FROM Authors\_31oct WHERE AuthorID=1;<br />Query OK, 1 row affected (0.01 sec)<br /><br />mysql> SELECT \* FROM Authors\_31oct;<br />+----------+----------------+<br />\| AuthorID \| AuthorName     \|<br />+----------+----------------+<br />\|        2 \| Ravinder Singh \|<br />\|        3 \| WILLAM CHETAN  \|<br />+----------+----------------+<br />2 rows in set (0.00 sec)<br /><br />mysql> SELECT \* FROM Books\_31oct;<br />+--------+-------------------------+----------+<br />\| BookID \| BookTitle               \| AuthorID \|<br />+--------+-------------------------+----------+<br />\|      1 \| Five Point Someone      \|     NULL \|<br />\|      2 \| GOOD BYE SAM            \|     NULL \|<br />\|      3 \| HARRY POTTER            \|        2 \|<br />\|      4 \| The Immortals of Meluha \|        3 \|<br />\|      5 \| The Secret of the Nagas \|        3 \|<br />+--------+-------------------------+----------+<br />5 rows in set (0.00 sec)<br />|
|-|



Update the author of a book to a new author.



| SELECT \* FROM Books\_31oct;<br />+--------+-------------------------+----------+<br />\| BookID \| BookTitle               \| AuthorID \|<br />+--------+-------------------------+----------+<br />\|      1 \| Five Point Someone      \|        3 \|<br />\|      2 \| GOOD BYE SAM            \|        3 \|<br />\|      3 \| HARRY POTTER            \|        3 \|<br />\|      4 \| The Immortals of Meluha \|        3 \|<br />\|      5 \| The Secret of the Nagas \|        3 \|<br />+--------+-------------------------+----------+<br />5 rows in set (0.00 sec)<br />|
|-|



