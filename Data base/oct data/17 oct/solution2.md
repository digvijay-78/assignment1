Assignment 2 — Product Management System

Table: products



Create a products table with:



Product ID

Product Name

Category

Brand

City

Price

Stock

Rating

Manufacturing Date

Data Requirements

|**CREATE TABLE products (<br />    ->     product\_id INT PRIMARY KEY AUTO\_INCREMENT,<br />    ->     product\_name VARCHAR(50),<br />    ->     category VARCHAR(30),<br />    ->     brand VARCHAR(30),<br />    ->     city VARCHAR(30),<br />    ->     price INT,<br />    ->     stock INT,<br />    ->     rating DECIMAL(2,1),<br />    ->     manufacturing\_date DATE<br />    -> );<br />Query OK, 0 rows affected (0.04 sec)**|
|-|





Insert at least 8 products.



Your data should include:



Categories: Electronics, Furniture, Clothing, Grocery

At least 5 different brands

Cities: Indore, Bhopal, Pune, Mumbai, Delhi

Price: ₹500 to ₹1,00,000

Stock: 0 to 100

Rating: 1 to 5

Manufacturing dates from 2021 to 2026

Some products with the same category

Some products with the same brand

Some similar prices

Some products with zero stock

|**INSERT INTO products<br />    -> (product\_name, category, brand, city, price, stock, rating, manufacturing\_date)<br />    -> VALUES<br />    -> ('Laptop', 'Electronics', 'Dell', 'Indore', 65000, 25, 4.5, '2023-05-15'),<br />    -> ('Smartphone', 'Electronics', 'Samsung', 'Bhopal', 45000, 40, 4.2, '2024-02-10'),<br />    -> ('Office Chair', 'Furniture', 'Godrej', 'Pune', 12000, 15, 4.0, '2022-08-20'),<br />    -> ('Sofa', 'Furniture', 'Godrej', 'Mumbai', 45000, 10, 4.3, '2021-11-12'),<br />    -> ('T-Shirt', 'Clothing', 'Puma', 'Delhi', 1500, 100, 4.1, '2025-01-25'),<br />    -> ('Jeans', 'Clothing', 'Puma', 'Indore', 2500, 60, 3.8, '2024-07-18'),<br />    -> ('Rice Pack', 'Grocery', 'India Gate', 'Bhopal', 500, 0, 4.4, '2026-02-05'),<br />    -> ('Television', 'Electronics', 'Samsung', 'Pune', 65000, 0, 4.6, '2025-09-10');<br />Query OK, 8 rows affected (0.01 sec)<br />Records: 8  Duplicates: 0  Warnings: 0**|
|-|





SQL Queries

1\. Find products whose price is greater than ₹30,000 AND rating is at least 4, but exclude products from Mumbai.

|**select \* from products where price>30000 and rating >=4 and city!="mumbai";<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\| product\_id \| product\_name \| category    \| brand   \| city   \| price \| stock \| rating \| manufacturing\_date \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\|          1 \| Laptop       \| Electronics \| Dell    \| Indore \| 65000 \|    25 \|    4.5 \| 2023-05-15         \|<br />\|          2 \| Smartphone   \| Electronics \| Samsung \| Bhopal \| 45000 \|    40 \|    4.2 \| 2024-02-10         \|<br />\|          8 \| Television   \| Electronics \| Samsung \| Pune   \| 65000 \|     0 \|    4.6 \| 2025-09-10         \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />3 rows in set (0.00 sec)**|
|-|





2\. Find products whose stock is less than 20 OR price is greater than ₹75,000, and whose category is not Grocery.

|**select \* from products where (stock<20 or price >75000 )and category != "Grocery";<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\| product\_id \| product\_name \| category    \| brand   \| city   \| price \| stock \| rating \| manufacturing\_date \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\|          3 \| Office Chair \| Furniture   \| Godrej  \| Pune   \| 12000 \|    15 \|    4.0 \| 2022-08-20         \|<br />\|          4 \| Sofa         \| Furniture   \| Godrej  \| Mumbai \| 45000 \|    10 \|    4.3 \| 2021-11-12         \|<br />\|          8 \| Television   \| Electronics \| Samsung \| Pune   \| 65000 \|     0 \|    4.6 \| 2025-09-10         \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />3 rows in set (0.00 sec)**|
|-|



3\. Find products whose price is between ₹15,000 and ₹60,000 AND rating is between 3 and 5, and which were manufactured after 2022.

|**select \* from products where price between 15000 and 60000 and rating between 3 and 5 and manufacturing\_date > "2022-12-31";<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\| product\_id \| product\_name \| category    \| brand   \| city   \| price \| stock \| rating \| manufacturing\_date \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\|          2 \| Smartphone   \| Electronics \| Samsung \| Bhopal \| 45000 \|    40 \|    4.2 \| 2024-02-10         \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />1 row in set (0.00 sec)**|
|-|





4\. Find products from Indore, Pune, or Delhi whose price is greater than ₹20,000 AND stock is not 0.

|**select \* from products where city in ('Indore', "Pune", "Delhi")and price >20000 and stock !=0;<br />+------------+--------------+-------------+-------+--------+-------+-------+--------+--------------------+<br />\| product\_id \| product\_name \| category    \| brand \| city   \| price \| stock \| rating \| manufacturing\_date \|<br />+------------+--------------+-------------+-------+--------+-------+-------+--------+--------------------+<br />\|          1 \| Laptop       \| Electronics \| Dell  \| Indore \| 65000 \|    25 \|    4.5 \| 2023-05-15         \|<br />+------------+--------------+-------------+-------+--------+-------+-------+--------+--------------------+<br />1 row in set (0.00 sec)**|
|-|





5\. Find products belonging to Electronics or Furniture using IN.

|**select \* from products where category in ("Electronics","Furniture");<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\| product\_id \| product\_name \| category    \| brand   \| city   \| price \| stock \| rating \| manufacturing\_date \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\|          1 \| Laptop       \| Electronics \| Dell    \| Indore \| 65000 \|    25 \|    4.5 \| 2023-05-15         \|<br />\|          2 \| Smartphone   \| Electronics \| Samsung \| Bhopal \| 45000 \|    40 \|    4.2 \| 2024-02-10         \|<br />\|          3 \| Office Chair \| Furniture   \| Godrej  \| Pune   \| 12000 \|    15 \|    4.0 \| 2022-08-20         \|<br />\|          4 \| Sofa         \| Furniture   \| Godrej  \| Mumbai \| 45000 \|    10 \|    4.3 \| 2021-11-12         \|<br />\|          8 \| Television   \| Electronics \| Samsung \| Pune   \| 65000 \|     0 \|    4.6 \| 2025-09-10         \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />5 rows in set (0.00 sec)**|
|-|





6\. Find products belonging to Electronics, Clothing, or Grocery using IN.

|**select \* from products where category in ("electronics", "clothing", "grocery");<br />+------------+--------------+-------------+------------+--------+-------+-------+--------+--------------------+<br />\| product\_id \| product\_name \| category    \| brand      \| city   \| price \| stock \| rating \| manufacturing\_date \|<br />+------------+--------------+-------------+------------+--------+-------+-------+--------+--------------------+<br />\|          1 \| Laptop       \| Electronics \| Dell       \| Indore \| 65000 \|    25 \|    4.5 \| 2023-05-15         \|<br />\|          2 \| Smartphone   \| Electronics \| Samsung    \| Bhopal \| 45000 \|    40 \|    4.2 \| 2024-02-10         \|<br />\|          5 \| T-Shirt      \| Clothing    \| Puma       \| Delhi  \|  1500 \|   100 \|    4.1 \| 2025-01-25         \|<br />\|          6 \| Jeans        \| Clothing    \| Puma       \| Indore \|  2500 \|    60 \|    3.8 \| 2024-07-18         \|<br />\|          7 \| Rice Pack    \| Grocery     \| India Gate \| Bhopal \|   500 \|     0 \|    4.4 \| 2026-02-05         \|<br />\|          8 \| Television   \| Electronics \| Samsung    \| Pune   \| 65000 \|     0 \|    4.6 \| 2025-09-10         \|<br />+------------+--------------+-------------+------------+--------+-------+-------+--------+--------------------+<br />6 rows in set (0.00 sec)**|
|-|



7\. Find products that are not from Indore or Bhopal using NOT IN.

|**select \* from products where city not  in ("indore","bhopal");<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\| product\_id \| product\_name \| category    \| brand   \| city   \| price \| stock \| rating \| manufacturing\_date \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\|          3 \| Office Chair \| Furniture   \| Godrej  \| Pune   \| 12000 \|    15 \|    4.0 \| 2022-08-20         \|<br />\|          4 \| Sofa         \| Furniture   \| Godrej  \| Mumbai \| 45000 \|    10 \|    4.3 \| 2021-11-12         \|<br />\|          5 \| T-Shirt      \| Clothing    \| Puma    \| Delhi  \|  1500 \|   100 \|    4.1 \| 2025-01-25         \|<br />\|          8 \| Television   \| Electronics \| Samsung \| Pune   \| 65000 \|     0 \|    4.6 \| 2025-09-10         \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />4 rows in set (0.00 sec)**|
|-|





8\. Find products whose brand is not Samsung, LG, or Sony.

|**select \* from products where brand not in ("samsung","lg","sony");<br />+------------+--------------+-------------+------------+--------+-------+-------+--------+--------------------+<br />\| product\_id \| product\_name \| category    \| brand      \| city   \| price \| stock \| rating \| manufacturing\_date \|<br />+------------+--------------+-------------+------------+--------+-------+-------+--------+--------------------+<br />\|          1 \| Laptop       \| Electronics \| Dell       \| Indore \| 65000 \|    25 \|    4.5 \| 2023-05-15         \|<br />\|          3 \| Office Chair \| Furniture   \| Godrej     \| Pune   \| 12000 \|    15 \|    4.0 \| 2022-08-20         \|<br />\|          4 \| Sofa         \| Furniture   \| Godrej     \| Mumbai \| 45000 \|    10 \|    4.3 \| 2021-11-12         \|<br />\|          5 \| T-Shirt      \| Clothing    \| Puma       \| Delhi  \|  1500 \|   100 \|    4.1 \| 2025-01-25         \|<br />\|          6 \| Jeans        \| Clothing    \| Puma       \| Indore \|  2500 \|    60 \|    3.8 \| 2024-07-18         \|<br />\|          7 \| Rice Pack    \| Grocery     \| India Gate \| Bhopal \|   500 \|     0 \|    4.4 \| 2026-02-05         \|<br />+------------+--------------+-------------+------------+--------+-------+-------+--------+--------------------+<br />6 rows in set (0.00 sec)**|
|-|



9\. Find products whose price is between ₹10,000 and ₹50,000.

| **select \* from products where price between 10000 and 50000;<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\| product\_id \| product\_name \| category    \| brand   \| city   \| price \| stock \| rating \| manufacturing\_date \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\|          2 \| Smartphone   \| Electronics \| Samsung \| Bhopal \| 45000 \|    40 \|    4.2 \| 2024-02-10         \|<br />\|          3 \| Office Chair \| Furniture   \| Godrej  \| Pune   \| 12000 \|    15 \|    4.0 \| 2022-08-20         \|<br />\|          4 \| Sofa         \| Furniture   \| Godrej  \| Mumbai \| 45000 \|    10 \|    4.3 \| 2021-11-12         \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />3 rows in set (0.00 sec)**|
|-|





10\. Find products whose stock is between 20 and 60.

| **select \* from products where stock between 20 and 60;<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\| product\_id \| product\_name \| category    \| brand   \| city   \| price \| stock \| rating \| manufacturing\_date \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\|          1 \| Laptop       \| Electronics \| Dell    \| Indore \| 65000 \|    25 \|    4.5 \| 2023-05-15         \|<br />\|          2 \| Smartphone   \| Electronics \| Samsung \| Bhopal \| 45000 \|    40 \|    4.2 \| 2024-02-10         \|<br />\|          6 \| Jeans        \| Clothing    \| Puma    \| Indore \|  2500 \|    60 \|    3.8 \| 2024-07-18         \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />3 rows in set (0.00 sec)**|
|-|





11\. Find products whose rating is between 3 and 5, and whose price is greater than ₹20,000.

|**select \* from products where rating between 3 and 5 and price >20000;<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\| product\_id \| product\_name \| category    \| brand   \| city   \| price \| stock \| rating \| manufacturing\_date \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\|          1 \| Laptop       \| Electronics \| Dell    \| Indore \| 65000 \|    25 \|    4.5 \| 2023-05-15         \|<br />\|          2 \| Smartphone   \| Electronics \| Samsung \| Bhopal \| 45000 \|    40 \|    4.2 \| 2024-02-10         \|<br />\|          4 \| Sofa         \| Furniture   \| Godrej  \| Mumbai \| 45000 \|    10 \|    4.3 \| 2021-11-12         \|<br />\|          8 \| Television   \| Electronics \| Samsung \| Pune   \| 65000 \|     0 \|    4.6 \| 2025-09-10         \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />4 rows in set (0.00 sec)**|
|-|





12\. Find products manufactured between 2023 and 2025, whose category is Electronics or Furniture.

|**select \* from products where manufacturing\_date between "2023-01-01"and "2025-12-31" and category in("Electronics","Furniture");<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\| product\_id \| product\_name \| category    \| brand   \| city   \| price \| stock \| rating \| manufacturing\_date \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\|          1 \| Laptop       \| Electronics \| Dell    \| Indore \| 65000 \|    25 \|    4.5 \| 2023-05-15         \|<br />\|          2 \| Smartphone   \| Electronics \| Samsung \| Bhopal \| 45000 \|    40 \|    4.2 \| 2024-02-10         \|<br />\|          8 \| Television   \| Electronics \| Samsung \| Pune   \| 65000 \|     0 \|    4.6 \| 2025-09-10         \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />3 rows in set (0.00 sec)<br />**|
|-|





13\. Find products whose name starts with S.

|**select \* from products where product\_name like ("s%");<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\| product\_id \| product\_name \| category    \| brand   \| city   \| price \| stock \| rating \| manufacturing\_date \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\|          2 \| Smartphone   \| Electronics \| Samsung \| Bhopal \| 45000 \|    40 \|    4.2 \| 2024-02-10         \|<br />\|          4 \| Sofa         \| Furniture   \| Godrej  \| Mumbai \| 45000 \|    10 \|    4.3 \| 2021-11-12         \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />2 rows in set (0.00 sec)**|
|-|



14\. Find products whose name contains phone anywhere.

|**select \* from products where product\_name like ("%phone%");<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\| product\_id \| product\_name \| category    \| brand   \| city   \| price \| stock \| rating \| manufacturing\_date \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\|          2 \| Smartphone   \| Electronics \| Samsung \| Bhopal \| 45000 \|    40 \|    4.2 \| 2024-02-10         \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />1 row in set (0.00 sec)**|
|-|





15\. Find products whose brand ends with a.

|**select \* from products where brand like ("%a");<br />+------------+--------------+----------+-------+--------+-------+-------+--------+--------------------+<br />\| product\_id \| product\_name \| category \| brand \| city   \| price \| stock \| rating \| manufacturing\_date \|<br />+------------+--------------+----------+-------+--------+-------+-------+--------+--------------------+<br />\|          5 \| T-Shirt      \| Clothing \| Puma  \| Delhi  \|  1500 \|   100 \|    4.1 \| 2025-01-25         \|<br />\|          6 \| Jeans        \| Clothing \| Puma  \| Indore \|  2500 \|    60 \|    3.8 \| 2024-07-18         \|<br />+------------+--------------+----------+-------+--------+-------+-------+--------+--------------------+<br />2 rows in set (0.00 sec)**|
|-|



16\. Find products from Indore or Pune, whose price is between ₹20,000 and ₹70,000, and whose rating is at least 4.

| **select \* from products where city in ("indore","pune") and price between 20000 and 70000 and rating >=4;<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\| product\_id \| product\_name \| category    \| brand   \| city   \| price \| stock \| rating \| manufacturing\_date \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\|          1 \| Laptop       \| Electronics \| Dell    \| Indore \| 65000 \|    25 \|    4.5 \| 2023-05-15         \|<br />\|          8 \| Television   \| Electronics \| Samsung \| Pune   \| 65000 \|     0 \|    4.6 \| 2025-09-10         \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />2 rows in set (0.00 sec)**|
|-|



17\. Find products belonging to Electronics or Furniture, whose stock is greater than 10, whose price is less than ₹60,000, and whose manufacturing date is after 2022.

|**select \* from products where category in ("Electronics","Furniture") and stock >10 and price <60000 and manufacturing\_date>"2022-12-31";<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\| product\_id \| product\_name \| category    \| brand   \| city   \| price \| stock \| rating \| manufacturing\_date \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\|          2 \| Smartphone   \| Electronics \| Samsung \| Bhopal \| 45000 \|    40 \|    4.2 \| 2024-02-10         \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />1 row in set (0.00 sec)**|
|-|



18\. Find products whose name contains the letter a, whose price is NOT between ₹10,000 and ₹50,000, and whose stock is greater than 5.

| **select \* from products where product\_name like ("%a%") and price not between 10000 and 50000 and stock >5;<br />+------------+--------------+-------------+-------+--------+-------+-------+--------+--------------------+<br />\| product\_id \| product\_name \| category    \| brand \| city   \| price \| stock \| rating \| manufacturing\_date \|<br />+------------+--------------+-------------+-------+--------+-------+-------+--------+--------------------+<br />\|          1 \| Laptop       \| Electronics \| Dell  \| Indore \| 65000 \|    25 \|    4.5 \| 2023-05-15         \|<br />\|          6 \| Jeans        \| Clothing    \| Puma  \| Indore \|  2500 \|    60 \|    3.8 \| 2024-07-18         \|<br />+------------+--------------+-------------+-------+--------+-------+-------+--------+--------------------+<br />2 rows in set (0.00 sec)<br />**|
|-|





19\. Find products manufactured between 2022 and 2025, belonging to Electronics, Clothing, or Furniture, having a rating greater than 3, and whose city is not Mumbai.

| **select \* from products where category in ("Electronics","Furniture","Clothing") and rating>3 and city != "mumbai" and manufacturing\_date between "2022-01-01" and "2025-12-31";<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\| product\_id \| product\_name \| category    \| brand   \| city   \| price \| stock \| rating \| manufacturing\_date \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\|          1 \| Laptop       \| Electronics \| Dell    \| Indore \| 65000 \|    25 \|    4.5 \| 2023-05-15         \|<br />\|          2 \| Smartphone   \| Electronics \| Samsung \| Bhopal \| 45000 \|    40 \|    4.2 \| 2024-02-10         \|<br />\|          3 \| Office Chair \| Furniture   \| Godrej  \| Pune   \| 12000 \|    15 \|    4.0 \| 2022-08-20         \|<br />\|          5 \| T-Shirt      \| Clothing    \| Puma    \| Delhi  \|  1500 \|   100 \|    4.1 \| 2025-01-25         \|<br />\|          6 \| Jeans        \| Clothing    \| Puma    \| Indore \|  2500 \|    60 \|    3.8 \| 2024-07-18         \|<br />\|          8 \| Television   \| Electronics \| Samsung \| Pune   \| 65000 \|     0 \|    4.6 \| 2025-09-10         \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />6 rows in set (0.00 sec)**|
|-|



20\. Find products whose name starts with S or M, whose city is not Indore or Mumbai, whose price is between ₹15,000 and ₹80,000, whose rating is at least 4, and whose manufacturing date is after 2023.

| **select \* from products where (product\_name like "s%" or product\_name like "m%") and city not in ("indore","mumbai") and price between 15000 and 80000 and rating >=4 and manufacturing\_date >"2023-12-31";<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\| product\_id \| product\_name \| category    \| brand   \| city   \| price \| stock \| rating \| manufacturing\_date \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />\|          2 \| Smartphone   \| Electronics \| Samsung \| Bhopal \| 45000 \|    40 \|    4.2 \| 2024-02-10         \|<br />+------------+--------------+-------------+---------+--------+-------+-------+--------+--------------------+<br />1 row in set (0.00 sec)<br />**|
|-|



