'''QNO 2: Automated Student Result Processing System(3.5)

A college stores student marks in a file named students.txt. Each line contains a student's ID, name, and marks in three subjects, separated by commas.

Write a Python program that reads the file, validates the records, calculates total marks and percentage, and writes the results of valid students into results.txt.

Requirements:
1. Read student records from students.txt.
2. Handle missing files and file access errors using exception handling.
3. Validate that each record contains exactly five fields and that marks are numeric and between 0 and 100.
4. Handle invalid records without terminating the program; record their line numbers and reasons in errors.txt.
5. If a student ID is duplicated, reject the duplicate record.
6. Calculate total marks and percentage for valid records.
7. Write valid results to results.txt, assigning grades:
   - 90% and above: A
   - 75% to below 90%: B
   - 60% to below 75%: C
   - Below 60%: D
8. Use appropriate exception handling for file operations, invalid data, and unexpected errors. Ensure files are closed properly.
Sample input file (students.txt):
101,Amit,85,90,78
102,Priya,95,92,98
103,Rahul,75,abc,80
104,Neha,60,65,70
102,Karan,80,85,90
105,Simran,110,85,90
106,Rohit,70,80
107,Anjali,88,91,84


Expected output file (results.txt):
ID: 101, Name: Amit, Total: 253, Percentage: 84.33%, Grade: B
ID: 102, Name: Priya, Total: 285, Percentage: 95.00%, Grade: A
ID: 104, Name: Neha, Total: 195, Percentage: 65.00%, Grade: C
ID: 107, Name: Anjali, Total: 263, Percentage: 87.67%, Grade: B


Expected error log (errors.txt):
Line 3: Invalid marks - marks must be numeric.
Line 5: Duplicate student ID - 102.
Line 6: Invalid marks - marks must be between 0 and 100.
Line 7: Invalid record - expected 5 fields.


Challenge: The program must continue processing all remaining records even when individual records are invalid. If students.txt does not exist, display a meaningful error message instead of crashing.
'''