"""2. Doctor Management Package
Create a package named "doctor".
Create module:
doctor_module.py
Implement the following functions:
a) add_doctor()
Take doctor details:
- Doctor ID
- Doctor Name
- Specialization
- Experience
- Consultation Fees
Store doctor information using list and dictionary.
b) display_doctors()
Display all doctor details."""

def dadd():
    doctor=[]
    a=int(input("enter the no of doctor"))
    for i in range(a):
        id=input("enter Doctor  ID")
        name=input("enter doctor Name")
        sp=(input("enter the Specialization"))
        ex=int(input("enter the Experience"))
        con=int(input("enter the Consultation Fees"))
        dic={"id":id,
             "name":name,
             "specialization":sp,
             "experince":ex,
             "consulation free":con
             }
        doctor.append(dic)
    print("doctor added successfully")
    return doctor
def display_doctors(doctor):
    for i in doctor:
        for k,v in i.items():
            print(k,":",v)
