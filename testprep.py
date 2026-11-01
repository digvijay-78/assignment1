'''# print("a"==97)
# print(None or "deep")


#WAP to add 2 matrix
a=[[2,3],[4,5]]
b=[[8,10],[9,11]]
c=[]
for i in range(len(a)):
    row=[]
    for j in range(len(a[i])):
        row.append(a[i][j]+b[i][j])
    c.append(row)
print("display")
print(*c)'''

# nums = [2, 7, 11, 15]
# target = 9
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         ch=nums[i]+nums[j]
#         if ch==target:
#             print(i,j)


# s = "aabbcdeef"
# for st in s:
#     if s.count(st)==1:
#         print(st)
#         break


# nums = [0, 1, 0, 3, 12]
# z=0
# for i in range(len(nums)):
#     if nums[i]!=0:
#         nums[z]=nums[i]
#         z+=1
# for i in range(z, len(nums)):
#     nums[i] = 0

# print(nums)

# nums = [3, 0, 1]
# nums.sort()
# for i in range(len(nums)-1):
#     if  nums[i+1]-nums[i]!=1:
#         print(nums[i+1]-nums[i])
#         break
# else:
#     print(nums[-1]+1)
'''
QNO 1:Student Result Processing System(3 Marks)

You are working as a Python developer for a training institute. The institute maintains student marks 
in a file named students.txt.
Your task is to develop a Student Result Processing System that reads student records from the file,
validates the data, calculates the result, and generates separate files for valid results and errors.
Input File: students.txt
The file contains student records in the following format:
Student_ID,Student_Name,Subject,Marks

The actual file contains:

101,Ajay,Python,85
102,Rahul,Python,78
103,Priya,Python,92
104,Amit,Python,abc
105,Neha,Python,88
106,Rohit,Python
107,Simran,Python,95
108,Karan,Python,105
109,Anita,Python,35
110,Vikas,Python,65

NOTE:
Some records intentionally contain invalid data:

104,Amit,Python,abc → Marks are not numeric.
106,Rohit,Python → Marks are missing.
108,Karan,Python,105 → Marks are outside the valid range of 0–100.

Your program must not terminate when it encounters an invalid record.

It should skip the invalid record, store the error in an error file, and continue processing the remaining records.

Requirements
1. Read the Input File

Read student records from students.txt using Python file handling.

Process the file line by line.

2. Validate Student Records

For every record, validate:

Student ID must be present.
Student Name must be present.
Subject must be present.
Marks must be present.
Marks must be numeric.
Marks must be between 0 and 100.
3. Calculate Result

Based on marks, assign the following result:

Marks Result
90–100 Excellent
75–89 Very Good
60–74 Good
40–59 Pass
0–39 Fail
4. Generate result.txt

For every valid student record, write:

Student ID - Name - Subject - Marks - Result

Expected output:

101 - Ajay - Python - 85 - Very Good
102 - Rahul - Python - 78 - Very Good
103 - Priya - Python - 92 - Excellent
105 - Neha - Python - 88 - Very Good
107 - Simran - Python - 95 - Excellent
109 - Anita - Python - 35 - Fail
110 - Vikas - Python - 65 - Good

5. Generate error_log.txt

For every invalid record, write the original record along with the reason for the error.

Expected output:

Error: 104,Amit,Python,abc -> Marks must be numeric
Error: 106,Rohit,Python -> Marks are missing
Error: 108,Karan,Python,105 -> Marks must be between 0 and 100

6. Error Handling

Your program should handle different types of invalid situations appropriately.

Important: If one student's record is invalid, the program must continue processing the remaining records instead of terminating.

For example:

104 → Invalid → Continue
105 → Valid → Process
106 → Invalid → Continue
107 → Valid → Process
7. Additional Requirement

If the input file is not available, display an appropriate error message instead of terminating the program.

Expected Final Output

After successful execution, display:

Student result processing completed successfully.

Valid records have been written to result.txt
Invalid records have been written to error_log.txt

The following files should be generated:

project/
│
├── student_result.py
├── students.txt
├── result.txt
└── error_log.txt
'''

try:
    f = open("students.txt", "r")
    result_file = open("result.txt", "w")
    error_file = open("error_log.txt", "w")

    for line in f:
        line = line.strip()
        data = line.split(",")

        # Check missing fields
        if len(data) < 4:
            error_file.write("Error: " + line + " -> Marks are missing\n")
            continue

        student_id = data[0].strip()
        name = data[1].strip()
        subject = data[2].strip()
        marks = data[3].strip()

        # Check required fields
        if student_id == "":
            error_file.write("Error: " + line + " -> Student ID is missing\n")
            continue

        if name == "":
            error_file.write("Error: " + line + " -> Student Name is missing\n")
            continue

        if subject == "":
            error_file.write("Error: " + line + " -> Subject is missing\n")
            continue

        if marks == "":
            error_file.write("Error: " + line + " -> Marks are missing\n")
            continue

        # Check numeric marks
        try:
            marks = int(marks)
        except ValueError:
            error_file.write("Error: " + line + " -> Marks must be numeric\n")
            continue

        # Check range
        if marks < 0 or marks > 100:
            error_file.write(
                "Error: " + line + " -> Marks must be between 0 and 100\n"
            )
            continue

        # Calculate result
        if marks >= 90:
            result = "Excellent"
        elif marks >= 75:
            result = "Very Good"
        elif marks >= 60:
            result = "Good"
        elif marks >= 40:
            result = "Pass"
        else:
            result = "Fail"

        result_file.write(
            student_id + " - " + name + " - " + subject +
            " - " + str(marks) + " - " + result + "\n"
        )

    f.close()
    result_file.close()
    error_file.close()

    print("Student result processing completed successfully.")
    print("Valid records have been written to result.txt")
    print("Invalid records have been written to error_log.txt")

except FileNotFoundError:
    print("Error: students.txt file not found.")