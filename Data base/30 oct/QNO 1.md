QNO 1:

table salses

=========================================================

| Column         | Data Type                               |

| -------------- | --------------------------------------- |

| sale\_id        | INT                                     |

| customer\_name  | VARCHAR(50)                             |

| city           | VARCHAR(30)                             |

| category       | VARCHAR(30)                             |

| product        | VARCHAR(50)                             |

| quantity       | INT                                     |

| price          | DECIMAL(10,2)                           |

| discount       | DECIMAL(10,2)                           |

| sale\_date      | DATE                                    |

| payment\_method | ENUM('UPI','Card','Cash','Net Banking') |

| status         | ENUM('Completed','Pending','Cancelled') |

| customer\_type  | ENUM('New','Regular','Premium')         |

=========================================================

|mysql> create table salses(sale\_id INT,customer\_name VARCHAR(50),city VARCHAR(30),category VARCHAR(30),product VARCHAR(50),quantity INT,price DECIMAL(10,2),discount DECIMAL(10,2),sale\_date  DATE, payment\_method ENUM('UPI','Card','Cash','Net Banking'),status ENUM('Completed','Pending','Cancelled'),customer\_type ENUM('New','Regular','Premium'));|
|-|



|DESC salses;<br />+----------------+-----------------------------------------+------+-----+---------+-------+<br />\| Field          \| Type                                    \| Null \| Key \| Default \| Extra \|<br />+----------------+-----------------------------------------+------+-----+---------+-------+<br />\| sale\_id        \| int                                     \| YES  \|     \| NULL    \|       \|<br />\| customer\_name  \| varchar(50)                             \| YES  \|     \| NULL    \|       \|<br />\| city           \| varchar(30)                             \| YES  \|     \| NULL    \|       \|<br />\| category       \| varchar(30)                             \| YES  \|     \| NULL    \|       \|<br />\| product        \| varchar(50)                             \| YES  \|     \| NULL    \|       \|<br />\| quantity       \| int                                     \| YES  \|     \| NULL    \|       \|<br />\| price          \| decimal(10,2)                           \| YES  \|     \| NULL    \|       \|<br />\| discount       \| decimal(10,2)                           \| YES  \|     \| NULL    \|       \|<br />\| sale\_date      \| date                                    \| YES  \|     \| NULL    \|       \|<br />\| payment\_method \| enum('UPI','Card','Cash','Net Banking') \| YES  \|     \| NULL    \|       \|<br />\| status         \| enum('Completed','Pending','Cancelled') \| YES  \|     \| NULL    \|       \|<br />\| customer\_type  \| enum('New','Regular','Premium')         \| YES  \|     \| NULL    \|       \|<br />+----------------+-----------------------------------------+------+-----+---------+-------+|
|-|



INSERT INTO salses

(customer\_name, city, category, product, quantity, price, discount, sale\_date, payment\_method, status, customer\_type)

VALUES

('Rahul','Indore','Electronics','Laptop',2,60000,5000,'2026-01-05','Card','Completed','Premium'),

('Priya','Bhopal','Electronics','Mobile',3,25000,3000,'2026-01-07','UPI','Completed','Regular'),

('Amit','Indore','Clothing','Jeans',5,2000,500,'2026-01-10','Cash','Completed','New'),

('Sneha','Mumbai','Beauty','Cream',8,800,400,'2026-01-12','UPI','Completed','Premium'),

('Rohit','Pune','Electronics','Laptop',1,55000,4000,'2026-01-15','Card','Completed','Regular'),

('Neha','Delhi','Clothing','Kurti',6,1800,600,'2026-01-17','UPI','Completed','Premium'),

('Karan','Indore','Sports','Bat',4,3500,700,'2026-01-20','Cash','Completed','Regular'),

('Pooja','Bhopal','Beauty','Lipstick',10,600,300,'2026-01-22','UPI','Completed','New'),

('Vikas','Delhi','Books','SQL Book',7,900,200,'2026-01-25','Net Banking','Completed','Regular'),

('Anjali','Mumbai','Electronics','Watch',3,7000,800,'2026-01-27','Card','Completed','Premium'),

('Saurabh','Pune','Grocery','Rice',12,900,500,'2026-02-01','UPI','Completed','Regular'),

('Riya','Delhi','Electronics','AC',2,45000,5000,'2026-02-03','Card','Completed','Premium'),

('Manish','Indore','Clothing','Shirt',6,1500,300,'2026-02-05','UPI','Completed','New'),

('Komal','Bhopal','Furniture','Chair',3,8000,1000,'2026-02-07','Cash','Completed','Premium'),

('Deepak','Mumbai','Electronics','Speaker',5,3000,500,'2026-02-12','Card','Cancelled','Regular');









Questions===>

Find the total number of completed sales for each city where quantity is greater than 2. Display cities in descending order of sales count.

|<br />mysql> select city,count(\*) as a from salses where quantity>2 and status="Completed" group by city order by a desc;<br />+--------+---+<br />\| city   \| a \|<br />+--------+---+<br />\| Bhopal \| 3 \|<br />\| Indore \| 3 \|<br />\| Mumbai \| 2 \|<br />\| Delhi  \| 2 \|<br />\| Pune   \| 1 \|<br />+--------+---+<br />5 rows in set (0.00 sec)|
|-|



Find the total quantity sold for each category where discount is greater than 300. Display highest quantity first.

|select category,sum(quantity) as a from salses where discount>300 group by category order by a desc;<br />+-------------+------+<br />\| category    \| a    \|<br />+-------------+------+<br />\| Electronics \|   16 \|<br />\| Grocery     \|   12 \|<br />\| Clothing    \|   11 \|<br />\| Beauty      \|    8 \|<br />\| Sports      \|    4 \|<br />\| Furniture   \|    3 \|<br />+-------------+------+<br />6 rows in set (0.00 sec)<br />|
|-|



Find the total sales amount for each city for completed sales only. Display highest-selling city first.

|select city,sum(price\*quantity) as a from salses where status="Completed" group by city order by a desc;<br />+--------+-----------+<br />\| city   \| a         \|<br />+--------+-----------+<br />\| Indore \| 153000.00 \|<br />\| Delhi  \| 107100.00 \|<br />\| Bhopal \| 105000.00 \|<br />\| Pune   \|  65800.00 \|<br />\| Mumbai \|  27400.00 \|<br />+--------+-----------+<br />5 rows in set (0.00 sec)|
|-|



Find the average product price for each category where quantity is at least 3. Display categories by average price descending.

|select category,avg(price) as a from salses where quantity>=3 group by category order by a desc;<br />+-------------+--------------+<br />\| category    \| a            \|<br />+-------------+--------------+<br />\| Electronics \| 11666.666667 \|<br />\| Furniture   \|  8000.000000 \|<br />\| Sports      \|  3500.000000 \|<br />\| Clothing    \|  1766.666667 \|<br />\| Books       \|   900.000000 \|<br />\| Grocery     \|   900.000000 \|<br />\| Beauty      \|   700.000000 \|<br />+-------------+--------------+<br />7 rows in set (0.00 sec)|
|-|



Find the number of sales for each customer type where the order amount (quantity \* price) is greater than 5000. Sort by number of sales descending.

|select  customer\_type,count(\*) as a from salses where (quantity\* price) >5000 group by customer\_type order by a desc;<br />+---------------+---+<br />\| customer\_type \| a \|<br />+---------------+---+<br />\| Premium       \| 6 \|<br />\| Regular       \| 6 \|<br />\| New           \| 3 \|<br />+---------------+---+|
|-|



Find the total discount given for each city for UPI transactions. Display highest discount first.

|select city,sum(discount) as a from salses where payment\_method="upi" group by city order by a desc;<br />+--------+---------+<br />\| city   \| a       \|<br />+--------+---------+<br />\| Bhopal \| 3300.00 \|<br />\| Delhi  \|  600.00 \|<br />\| Pune   \|  500.00 \|<br />\| Mumbai \|  400.00 \|<br />\| Indore \|  300.00 \|<br />+--------+---------+|
|-|



Find the total quantity sold through each payment method for completed transactions. Sort by total quantity descending.

|select payment\_method,sum(quantity) as a from salses where status="Completed" group by payment\_method order by a desc;<br />+----------------+------+<br />\| payment\_method \| a    \|<br />+----------------+------+<br />\| UPI            \|   45 \|<br />\| Cash           \|   12 \|<br />\| Card           \|    8 \|<br />\| Net Banking    \|    7 \|<br />+----------------+------+<br />4 rows in set (0.00 sec)|
|-|



Find the average discount for each category where quantity is greater than 4. Display highest average discount first.

|select category,avg(discount) as a from salses where quantity>4 group by category order by a desc;<br />+-------------+------------+<br />\| category    \| a          \|<br />+-------------+------------+<br />\| Grocery     \| 500.000000 \|<br />\| Electronics \| 500.000000 \|<br />\| Clothing    \| 466.666667 \|<br />\| Beauty      \| 350.000000 \|<br />\| Books       \| 200.000000 \|<br />+-------------+------------+<br />5 rows in set (0.00 sec)<br /><br />mysql>|
|-|



Find the maximum product price for each city where the status is Completed. Sort by maximum price descending.

|select city,max(price) as a from salses where status="Completed" group by city order by a desc;<br />+--------+----------+<br />\| city   \| a        \|<br />+--------+----------+<br />\| Indore \| 60000.00 \|<br />\| Pune   \| 55000.00 \|<br />\| Delhi  \| 45000.00 \|<br />\| Bhopal \| 25000.00 \|<br />\| Mumbai \|  7000.00 \|<br />+--------+----------+|
|-|



Find the minimum product price for each category where discount is greater than 300. Sort by minimum price ascending.

|select category,min(price) as a from salses where discount>300 group by category order by a;<br />+-------------+---------+<br />\| category    \| a       \|<br />+-------------+---------+<br />\| Beauty      \|  800.00 \|<br />\| Grocery     \|  900.00 \|<br />\| Clothing    \| 1800.00 \|<br />\| Electronics \| 3000.00 \|<br />\| Sports      \| 3500.00 \|<br />\| Furniture   \| 8000.00 \|<br />+-------------+---------+<br />6 rows in set (0.00 sec)<br />|
|-|



Find cities having more than 2 completed sales. Sort cities by completed sales count descending.

|select city,count(\*) as a from salses where status="Completed" group by city having a>2 order by a desc;<br />+--------+---+<br />\| city   \| a \|<br />+--------+---+<br />\| Indore \| 4 \|<br />\| Bhopal \| 3 \|<br />\| Delhi  \| 3 \|<br />+--------+---+<br />3 rows in set (0.00 sec)<br /><br />mysql>|
|-|



Find categories having total quantity greater than 10. Sort by total quantity descending.

|select category,sum(quantity) as a from salses group by category having a>10 order by a desc;<br />+-------------+------+<br />\| category    \| a    \|<br />+-------------+------+<br />\| Beauty      \|   18 \|<br />\| Clothing    \|   17 \|<br />\| Electronics \|   16 \|<br />\| Grocery     \|   12 \|<br />+-------------+------+<br />4 rows in set (0.00 sec)|
|-|



Find cities having total sales greater than 50,000. Sort by total sales descending.

|select city,sum(price\*quantity) as a from salses  group by city having a>50000 order by a desc;<br />+--------+-----------+<br />\| city   \| a         \|<br />+--------+-----------+<br />\| Indore \| 153000.00 \|<br />\| Delhi  \| 107100.00 \|<br />\| Bhopal \| 105000.00 \|<br />\| Pune   \|  65800.00 \|<br />+--------+-----------+<br />4 rows in set (0.00 sec)<br /><br />mysql>|
|-|



Find customer types having average product price greater than 10,000. Sort by average price descending.

|select  customer\_type,avg(price) as a from salses  group by customer\_type having a>10000 order by a desc;<br />+---------------+--------------+<br />\| customer\_type \| a            \|<br />+---------------+--------------+<br />\| Premium       \| 20433.333333 \|<br />\| Regular       \| 14716.666667 \|<br />+---------------+--------------+<br />2 rows in set (0.00 sec)<br /><br />mysql>|
|-|



Find categories having average discount greater than 400. Sort by average discount descending.

|select category,avg(discount) as a from salses group by category having a>400 order by a desc;<br />+-------------+-------------+<br />\| category    \| a           \|<br />+-------------+-------------+<br />\| Electronics \| 3050.000000 \|<br />\| Furniture   \| 1000.000000 \|<br />\| Sports      \|  700.000000 \|<br />\| Grocery     \|  500.000000 \|<br />\| Clothing    \|  466.666667 \|<br />+-------------+-------------+<br />5 rows in set (0.00 sec)<br /><br />mysql>|
|-|



Find payment methods having more than 2 completed transactions. Sort by transaction count descending.

|select payment\_method,count(\*) as a from salses WHERE status = 'Completed' group by payment\_method having a > 2 order by a desc;<br />+----------------+---+<br />\| payment\_method \| a \|<br />+----------------+---+<br />\| UPI            \| 6 \|<br />\| Card           \| 4 \|<br />\| Cash           \| 3 \|<br />+----------------+---+<br />3 rows in set (0.00 sec|
|-|



Find cities where the maximum product price is greater than 20,000. Sort by maximum price descending.

|select city,max(price) as a from salses  group by city having a>20000 order by a desc;<br />+--------+----------+<br />\| city   \| a        \|<br />+--------+----------+<br />\| Indore \| 60000.00 \|<br />\| Pune   \| 55000.00 \|<br />\| Delhi  \| 45000.00 \|<br />\| Bhopal \| 25000.00 \|<br />+--------+----------+|
|-|



Find categories where the minimum product price is less than 2,000. Sort by minimum price ascending.

|select category,min(price) as a from salses group by category having a<2000 order by a;<br />+----------+---------+<br />\| category \| a       \|<br />+----------+---------+<br />\| Beauty   \|  600.00 \|<br />\| Books    \|  900.00 \|<br />\| Grocery  \|  900.00 \|<br />\| Clothing \| 1500.00 \|<br />+----------+---------+<br />4 rows in set (0.00 sec)<br /><br />mysql>|
|-|



Find customer types where total discount is greater than 2,000. Sort by total discount descending.

|select  customer\_type,sum(discount) as a from salses  group by customer\_type having a>2000 order by a desc;<br />+---------------+----------+<br />\| customer\_type \| a        \|<br />+---------------+----------+<br />\| Premium       \| 12800.00 \|<br />\| Regular       \|  8900.00 \|<br />+---------------+----------+<br />2 rows in set (0.00 sec)<br /><br />mysql>|
|-|



Find cities where average quantity per transaction is greater than 4. Sort by average quantity descending.

|select city,avg(quantity) as a from salses  group by city having a>4 order by a desc;<br />+--------+--------+<br />\| city   \| a      \|<br />+--------+--------+<br />\| Pune   \| 6.5000 \|<br />\| Bhopal \| 5.3333 \|<br />\| Mumbai \| 5.3333 \|<br />\| Delhi  \| 5.0000 \|<br />\| Indore \| 4.2500 \|<br />+--------+--------+<br />5 rows in set (0.00 sec)<br />|
|-|



Find each city’s total sales for completed UPI transactions where quantity is greater than 2. Display only cities having total sales greater than 10,000.

|select city,sum(price\*quantity) as a from salses where status ="Completed" and payment\_method="upi" and quantity> 2  group by city having a>10000 ;<br />+--------+----------+<br />\| city   \| a        \|<br />+--------+----------+<br />\| Bhopal \| 81000.00 \|<br />\| Delhi  \| 10800.00 \|<br />\| Pune   \| 10800.00 \|<br />+--------+----------+<br />3 rows in set (0.00 sec)|
|-|



Find each category’s total quantity for completed transactions where discount is greater than 300. Display only categories having total quantity greater than 5.

|select category,sum(quantity) as a from salses where status ="Completed" and discount>300 group by category having a>5 ;<br />+-------------+------+<br />\| category    \| a    \|<br />+-------------+------+<br />\| Electronics \|   11 \|<br />\| Clothing    \|   11 \|<br />\| Beauty      \|    8 \|<br />\| Grocery     \|   12 \|<br />+-------------+------+<br />4 rows in set (0.00 sec)<br /><br />mysql>|
|-|



Find each customer type’s average price for completed transactions where quantity >= 2. Display only customer types whose average price exceeds 10,000.

|select  customer\_type,avg(price) as a from salses  where status ="Completed" and quantity>=2  group by customer\_type having a>10000 ;<br />+---------------+--------------+<br />\| customer\_type \| a            \|<br />+---------------+--------------+<br />\| Premium       \| 20433.333333 \|<br />+---------------+--------------+<br />1 row in set (0.00 sec)<br /><br />mysql>|
|-|



Find each city’s total discount for UPI transactions where quantity > 3. Display cities having total discount greater than 500.

|select city,sum(discount) as a from salses where  quantity>3 and payment\_method="upi"   group by city having a>500 ;<br />+-------+--------+<br />\| city  \| a      \|<br />+-------+--------+<br />\| Delhi \| 600.00 \|<br />+-------+--------+<br />1 row in set (0.00 sec)<br />|
|-|



Find each category’s total sales where payment method is UPI or Card and status is Completed. Display categories having total sales greater than 10,000.

|select category,sum(quantity\*price) as a from salses where payment\_method in ("upi","card") and status ="Completed"  group by category having a>10000 ;<br />+-------------+-----------+<br />\| category    \| a         \|<br />+-------------+-----------+<br />\| Electronics \| 361000.00 \|<br />\| Beauty      \|  12400.00 \|<br />\| Clothing    \|  19800.00 \|<br />\| Grocery     \|  10800.00 \|<br />+-------------+-----------+<br />4 rows in set (0.00 sec)<br /><br />mysql>|
|-|



Find each city’s transaction count for January 2026 completed transactions. Display cities having at least 2 transactions.

|select city,count(\*) as a from salses where status="Completed"  and sale\_date between "2026-01-01" and "2026-01-31" group by city having a>=2 ;<br />+--------+---+<br />\| city   \| a \|<br />+--------+---+<br />\| Indore \| 3 \|<br />\| Bhopal \| 2 \|<br />\| Mumbai \| 2 \|<br />\| Delhi  \| 2 \|<br />+--------+---+<br />4 rows in set (0.00 sec)<br />|
|-|



Find each category’s average sales amount where quantity >= 3 and status = Completed. Display categories whose average sales amount is greater than 5,000.

|select category,avg(quantity\*price) as a from salses where quantity>=3 and status ="Completed"  group by category having a>5000 ;<br />+-------------+--------------+<br />\| category    \| a            \|<br />+-------------+--------------+<br />\| Electronics \| 48000.000000 \|<br />\| Clothing    \|  9933.333333 \|<br />\| Beauty      \|  6200.000000 \|<br />\| Sports      \| 14000.000000 \|<br />\| Books       \|  6300.000000 \|<br />\| Grocery     \| 10800.000000 \|<br />\| Furniture   \| 24000.000000 \|<br />+-------------+--------------+<br />7 rows in set (0.00 sec)<br />|
|-|



Find each customer type’s maximum price where payment method is Card and status is Completed. Display only customer types whose maximum price exceeds 20,000.

|select  customer\_type,max(price) as a from salses  where status ="Completed" and payment\_method="card"  group by customer\_type having a>20000 ;<br />+---------------+----------+<br />\| customer\_type \| a        \|<br />+---------------+----------+<br />\| Premium       \| 60000.00 \|<br />\| Regular       \| 55000.00 \|<br />+---------------+----------+<br />2 rows in set (0.00 sec)<br /><br />mysql>|
|-|



Find each city’s total quantity for Electronics and Clothing products where status is Completed. Display cities having total quantity greater than 5.

|> select city,sum(quantity) as a from salses where  status ="Completed" and category in ("Electronics","Clothing")   group by city having a>5 ;<br />+--------+------+<br />\| city   \| a    \|<br />+--------+------+<br />\| Indore \|   13 \|<br />\| Delhi  \|    8 \|<br />+--------+------+<br />2 rows in set (0.00 sec)|
|-|



Find each payment method’s total sales where status is Completed and discount is greater than 400. Display payment methods having total sales greater than 20,000.

| select payment\_method,sum(price\*quantity) as a from salses where status="Completed" and discount >400 group by payment\_method having a>20000;<br />+----------------+-----------+<br />\| payment\_method \| a         \|<br />+----------------+-----------+<br />\| Card           \| 286000.00 \|<br />\| UPI            \|  96600.00 \|<br />\| Cash           \|  48000.00 \|<br />+----------------+-----------+<br />3 rows in set (0.00 sec)|
|-|



Find cities having more than 2 completed transactions and total sales greater than 50,000. Sort by total sales descending.

| select city,sum(price\*quantity) as a,count(\*) as c from salses where status="Completed"  group by city having a>50000 and c>2 order by a desc;<br />+--------+-----------+---+<br />\| city   \| a         \| c \|<br />+--------+-----------+---+<br />\| Indore \| 153000.00 \| 4 \|<br />\| Delhi  \| 107100.00 \| 3 \|<br />\| Bhopal \| 105000.00 \| 3 \|<br />+--------+-----------+---+<br />3 rows in set (0.00 sec)<br />|
|-|



Find categories having total quantity greater than 8 and average price greater than 2,000. Sort by total quantity descending.

| select category,sum(quantity) as a,avg(price) as c from salses  group by category having a>8 and c>2000 order by a desc;<br />+-------------+------+--------------+<br />\| category    \| a    \| c            \|<br />+-------------+------+--------------+<br />\| Electronics \|   16 \| 32500.000000 \|<br />+-------------+------+--------------+<br />1 row in set (0.00 sec)|
|-|



Find customer types having more than 2 transactions and total discount greater than 2,000. Sort by total discount descending.

| select customer\_type,sum(discount) as a,count(\*) as c from salses  group by customer\_type having a>2000 and c>2 order by a desc;<br />+---------------+----------+---+<br />\| customer\_type \| a        \| c \|<br />+---------------+----------+---+<br />\| Premium       \| 12800.00 \| 6 \|<br />\| Regular       \|  8900.00 \| 6 \|<br />+---------------+----------+---+<br />2 rows in set (0.00 sec)<br /><br />mysql>|
|-|



Find cities having average quantity greater than 3 and maximum product price greater than 20,000. Sort by average quantity descending.

| select city,avg(quantity) as a,max(price) as c from salses  group by city having a>3 and c>20000 order by a desc;<br />+--------+--------+----------+<br />\| city   \| a      \| c        \|<br />+--------+--------+----------+<br />\| Pune   \| 6.5000 \| 55000.00 \|<br />\| Bhopal \| 5.3333 \| 25000.00 \|<br />\| Delhi  \| 5.0000 \| 45000.00 \|<br />\| Indore \| 4.2500 \| 60000.00 \|<br />+--------+--------+----------+<br />4 rows in set (0.00 sec)<br /><br />mysql>|
|-|



Find categories having more than 2 completed transactions and total sales greater than 20,000. Sort by total sales descending.

| select category,sum(price\*quantity) as a,count(\*) as c from salses where status="Completed" group by category having a>20000 and c>2 order by a desc;<br />+-------------+-----------+---+<br />\| category    \| a         \| c \|<br />+-------------+-----------+---+<br />\| Electronics \| 361000.00 \| 5 \|<br />\| Clothing    \|  29800.00 \| 3 \|<br />+-------------+-----------+---+<br />2 rows in set (0.00 sec)|
|-|



Find payment methods having more than 2 completed transactions and average price greater than 10,000. Sort by average price descending.

| select payment\_method,avg(price) as a,count(\*) as c from salses where status="Completed" group by payment\_method having a>10000 and c>2 order by a desc;<br />+----------------+--------------+---+<br />\| payment\_method \| a            \| c \|<br />+----------------+--------------+---+<br />\| Card           \| 41750.000000 \| 4 \|<br />+----------------+--------------+---+<br />1 row in set (0.00 sec)|
|-|



Find cities having total quantity greater than 8 and average discount greater than 300. Sort by total quantity descending.

|select city,sum(quantity) as a,avg(discount) as c from salses  group by city having a>8 and c>300 order by a desc;<br />+--------+------+-------------+<br />\| city   \| a    \| c           \|<br />+--------+------+-------------+<br />\| Indore \|   17 \| 1625.000000 \|<br />\| Bhopal \|   16 \| 1433.333333 \|<br />\| Mumbai \|   16 \|  566.666667 \|<br />\| Delhi  \|   15 \| 1933.333333 \|<br />\| Pune   \|   13 \| 2250.000000 \|<br />+--------+------+-------------+<br />5 rows in set (0.00 sec)<br /><br />mysql>|
|-|



Find customer types having average price greater than 5,000 and total quantity greater than 8. Sort by total quantity descending.

| select customer\_type,avg(price) as a,sum(quantity) as c from salses  group by customer\_type having a>5000 and c>8 order by c desc;<br />+---------------+--------------+------+<br />\| customer\_type \| a            \| c    \|<br />+---------------+--------------+------+<br />\| Regular       \| 14716.666667 \|   32 \|<br />\| Premium       \| 20433.333333 \|   24 \|<br />+---------------+--------------+------+|
|-|



Find categories having minimum price below 2,000 and maximum price above 20,000. Sort by maximum price descending.

| select category,min(price) as a,max(price) as c from salses  group by category having a<2000 and c>20000 order by c desc;|
|-|



Find cities having total discount greater than 1,000 and total sales greater than 30,000. Sort by total sales descending.

| select city,sum(quantity\*price) as a,sum(discount) as c from salses  group by city having a>30000 and c>1000 order by a desc;<br />+--------+-----------+---------+<br />\| city   \| a         \| c       \|<br />+--------+-----------+---------+<br />\| Indore \| 153000.00 \| 6500.00 \|<br />\| Delhi  \| 107100.00 \| 5800.00 \|<br />\| Bhopal \| 105000.00 \| 4300.00 \|<br />\| Pune   \|  65800.00 \| 4500.00 \|<br />\| Mumbai \|  42400.00 \| 1700.00 \|<br />+--------+-----------+---------+<br />5 rows in set (0.00 sec)|
|-|



Find the top 3 cities based on total sales, considering only completed transactions with quantity greater than 1 and displaying only cities having more than 1 transaction.

| select city,sum(quantity\*price) as a,count(\*) as c from salses where  status="Completed" and quantity>1 group by city having c>1 order by a desc limit 3;<br />+--------+-----------+---+<br />\| city   \| a         \| c \|<br />+--------+-----------+---+<br />\| Indore \| 153000.00 \| 4 \|<br />\| Delhi  \| 107100.00 \| 3 \|<br />\| Bhopal \| 105000.00 \| 3 \|<br />+--------+-----------+---+<br />3 rows in set (0.00 sec)|
|-|



Find the top 3 categories based on total quantity where discount is greater than 300 and total quantity is greater than 5.

| select category,sum(quantity) as a from salses where discount>300  group by category having a>5 order by a desc limit 3;<br />+-------------+------+<br />\| category    \| a    \|<br />+-------------+------+<br />\| Electronics \|   16 \|<br />\| Grocery     \|   12 \|<br />\| Clothing    \|   11 \|<br />+-------------+------+<br />3 rows in set (0.00 sec)|
|-|



Find the top 3 customer types based on average sales amount where status is Completed and transaction count is greater than 1.

| select customer\_type,avg(quantity \*price) as a, count(\*) as c from salses where status ="Completed" group by customer\_type having  c>1 order by a desc limit 3;<br />+---------------+--------------+---+<br />\| customer\_type \| a            \| c \|<br />+---------------+--------------+---+<br />\| Premium       \| 45366.666667 \| 6 \|<br />\| Regular       \| 32220.000000 \| 5 \|<br />\| New           \|  8333.333333 \| 3  |
|-|



Find the top 3 cities based on total discount for UPI transactions where status is Completed and total discount is greater than 500.

| select city,sum(discount) as a from salses where  status="Completed" and payment\_method="upi" group by city having a>500 order by a desc limit 3;<br />+--------+---------+<br />\| city   \| a       \|<br />+--------+---------+<br />\| Bhopal \| 3300.00 \|<br />\| Delhi  \|  600.00 \|<br />+--------+---------+<br />2 rows in set (0.00 sec)<br /><br />mysql>|
|-|



Find the top 3 categories based on total sales where quantity is greater than 2, average price is greater than 1,000, and total sales exceeds 10,000.

| select category,sum(quantity\*price) as a,avg(price) as c from salses where quantity>2  group by category having a>10000 and c>1000 order by a desc limit 3;<br />+-------------+-----------+--------------+<br />\| category    \| a         \| c            \|<br />+-------------+-----------+--------------+<br />\| Electronics \| 111000.00 \| 11666.666667 \|<br />\| Clothing    \|  29800.00 \|  1766.666667 \|<br />\| Furniture   \|  24000.00 \|  8000.000000 \|<br />+-------------+-----------+--------------+<br />3 rows in set (0.00 sec)<br /><br />mysql>|
|-|



Find the top 3 cities based on average order value where status is Completed, total quantity is greater than 5, and transaction count is greater than 1.

| select city,avg(price\*quantity) as a,sum(quantity) as c,count(\*) from salses where  status="Completed"  group by city having c>5 and count(\*) > 1 order by a desc limit 3;<br />+--------+--------------+------+----------+<br />\| city   \| a            \| c    \| count(\*) \|<br />+--------+--------------+------+----------+<br />\| Indore \| 38250.000000 \|   17 \|        4 \|<br />\| Delhi  \| 35700.000000 \|   15 \|        3 \|<br />\| Bhopal \| 35000.000000 \|   16 \|        3 \|<br />+--------+--------------+------+----------+<br />3 rows in set (0.00 sec)<br />|
|-|



Find the second-highest city based on total sales after considering only completed transactions and cities having at least 2 transactions.

| select city,sum(price\*quantity) as a,count(\*) as c from salses where  status="Completed"  group by city having c>=2  order by a desc limit 1,1;<br />+-------+-----------+---+<br />\| city  \| a         \| c \|<br />+-------+-----------+---+<br />\| Delhi \| 107100.00 \| 3 \|<br />+-------+-----------+---+<br />1 row in set (0.00 sec)|
|-|



Find the third-highest category based on total quantity where quantity is greater than 2 and total discount exceeds 500.

| select category,sum(quantity) as a,sum(discount) as c from salses where quantity>2  group by category HAVING c > 500 order by a desc limit 2,1;<br />+-------------+------+---------+<br />\| category    \| a    \| c       \|<br />+-------------+------+---------+<br />\| Electronics \|   11 \| 4300.00 \|<br />+-------------+------+---------+<br />1 row in set (0.00 sec)<br />|
|-|



Find the 2nd and 3rd highest customer types based on total sales where status is Completed and average price is greater than 5,000.

| select customer\_type,sum(quantity \*price) as a, avg(price) as c from salses where status ="Completed" group by customer\_type having  c>5000 order by a desc limit 1,2;<br />+---------------+-----------+--------------+<br />\| customer\_type \| a         \| c            \|<br />+---------------+-----------+--------------+<br />\| Regular       \| 161100.00 \| 17060.000000 \|<br />+---------------+-----------+--------------+<br />1 row in set (0.00 sec)<br />|
|-|



Find the top 3 cities where:

status is Completed

payment method is UPI or Card

quantity is greater than 1

number of transactions is greater than 1

total quantity is greater than 5

total sales is greater than 20,000



| select city,sum(price\*quantity) as a,count(\*) as c,sum(quantity) as q from salses where  status="Completed" and payment\_method in ("upi","card") and quantity >1 group by city having c>1 and q>5 and a >20000 order by a desc limit 3;<br />+--------+-----------+---+------+<br />\| city   \| a         \| c \| q    \|<br />+--------+-----------+---+------+<br />\| Indore \| 129000.00 \| 2 \|    8 \|<br />\| Delhi  \| 100800.00 \| 2 \|    8 \|<br />\| Bhopal \|  81000.00 \| 2 \|   13 \|<br />+--------+-----------+---+------+<br />3 rows in set (0.00 sec)<br /><br />mysql>|
|-|



