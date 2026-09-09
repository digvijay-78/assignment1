"""2.
Hospital Management System – Oldest Patient
A hospital wants to give priority to the oldest patient during a free health check-up camp. The patient details are 
stored as tuples containing the patient's name and age.
As a Python developer, write a program to identify the oldest patient using the reduce() 
function with a lambda expression.
Input
patients = [
    ("Rahul", 45),
    ("Sneha", 62),
    ("Amit", 38),
    ("Kiran", 71),
    ("Pooja", 55)
]
Expected Output
Oldest Patient: Kiran
"""

from functools import reduce
n = int(input("enter number of patient: "))
main = []
for i in range(n):
    name = input(f"enter the name {i+1}: ")
    age = int(input(f"enter the age {i+1}: "))
    main.append((name, age))
result=reduce(lambda x,y: x if x[1]>y[1] else y, main)
print("Oldest Patient : ", result[0])