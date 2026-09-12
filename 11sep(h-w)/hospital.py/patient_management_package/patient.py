"""1. Patient Management Package
Create a package named "patient".
Create module:
patient_module.py
Implement the following functions:
a) add_patient()
Take patient details from user:
- Patient ID
- Patient Name
- Age
- Gender
- Disease
- Mobile Number
Store patient information using list and dictionary.
b) display_patients()
Display all registered patients.
c) search_patient()
Search patient details using Patient ID."""
def add():
    patient=[]
    a=int(input("enter the no of patient"))
    for i in range(a):
        id=input("enter Patient ID")
        name=input("enter Patient Name")
        age=int(input("enter the age"))
        gender=input("enter the gender")
        d=input("enter the disease")
        no=int(input("enter the mobile no"))
        dic={"id":id,
             "name":name,
             "age":age,
             "gender":gender,
             "disease":d,
             "mobile no":no}
        patient.append(dic)
    print("patient added successfully")
    return patient
def display_patients(patient):
    for i in patient:
        for k,v in i.items():
            print(k,":",v)


def search_patient(patient):
    a=input("enter the patient id")
    f=0
    for i in patient: 
        if a==i["id"]:
            for k,v in i.items():
                print(k,":",v)
            f=1
    if f==0:
        print("patient not found")
