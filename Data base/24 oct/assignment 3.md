3\.

Create a table GymMembers with:



MemberID (INT, Primary Key)

MemberName (VARCHAR(50), NOT NULL)

MembershipType (VARCHAR(15), should be 'Basic', 'Premium', or 'VIP', DEFAULT 'Basic')

MonthlyFee (DECIMAL(6,2), should be at least 500)

Insert records and check constraints:



(501, 'John', 'Premium', 1200)

(502, 'Emma', 'Gold', 800) (Should fail due to MembershipType constraint)

(503, 'Daniel', DEFAULT, 700) (Should insert 'Basic' as default)

(504, 'Sophia', 'VIP', 300) (Should fail due to MonthlyFee constraint)

| CREATE TABLE GymMembers (MemberID INT Primary Key,MemberName VARCHAR(50) NOT NULL, MembershipType VARCHAR(15) DEFAULT 'Basic',MonthlyFee DECIMAL(6,2),CHECK (MonthlyFee >=500 AND MembershipType IN ('Basic', 'Premium', 'VIP')));<br />Query OK, 0 rows affected (0.04 sec)<br /><br />mysql> INSERT INTO GymMembers VALUES (501, 'John', 'Premium', 1200);<br />Query OK, 1 row affected (0.01 sec)<br /><br />mysql> INSERT INTO GymMembers VALUES (502, 'Emma', 'Gold', 800);<br />ERROR 3819 (HY000): Check constraint 'gymmembers\_chk\_1' is violated.<br />mysql> INSERT INTO GymMembers VALUES (503, 'Daniel', DEFAULT, 700);<br />Query OK, 1 row affected (0.01 sec)<br /><br />mysql> INSERT INTO GymMembers VALUES (504, 'Sophia', 'VIP', 300);<br />ERROR 3819 (HY000): Check constraint 'gymmembers\_chk\_1' is violated.<br />mysql>|
|-|



