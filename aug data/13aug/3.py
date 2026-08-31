'''QUESTION 3: HOSPITAL PATIENT TRACKER
====================================

A hospital stores patient records for daily monitoring.

Fields:
patient_id, patient_name, age, disease

Requirements:
1. Read N patient records from the user and store them in a list of NamedTuples.

2. Display all patient details

3. Display patients whose age is above 60 years.

4. Search for a patient using Patient ID.

5. Count the number of patients suffering from a particular disease.

Test Case:

Input:
Enter number of patients: 4

P101 Rajesh 65 Diabetes
P102 Suman 45 Fever
P103 Mohan 70 Diabetes
P104 Rita 35 Cold

Enter Patient ID: P103
Enter Disease: Diabetes

Expected Output:
Patient Found:
P103 Mohan 70 Diabetes

Patients Above 60:
P101 Rajesh 65 Diabetes
P103 Mohan 70 Diabetes

Patients with Diabetes:
2'''
from collections import namedtuple
hospital=namedtuple("hospital",["patient_id", "patient_name", "age", "disease"])
n=int(input("Enter number of patients:"))
a=[]
for i in range(n):
    print("enter details")
    id=int(input("enter patient_id>"))
    name=input("enter name")
    age=int(input("enter age"))
    di=input("enter the disease").lower()
    z=hospital(id,name,age,di)
    a.append(z)
print("details")
for j in a:
    print(j.patient_id,j.patient_name,j.age,j.disease)



print("Patients Above 60:")
for k in a:
    if k.age>60:
        print(k.patient_id,k.patient_name,k.age,k.disease) 
    else:
        print("no patient is above 60")


n=int(input("Enter Patient ID:"))
d=input("Enter Disease:").lower()
m=0
for z in a:
    if z.patient_id==n:
        print("patient found\n",z.patient_id)
    if z.disease==d:
        m+=1
print("Patients with Diabetes:\n",m) 