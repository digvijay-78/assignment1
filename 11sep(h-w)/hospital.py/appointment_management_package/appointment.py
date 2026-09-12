"""3. Appointment Management Package
Create a package named "appointment".
Create module:
appointment_module.py
Implement:
a) book_appointment()
Take appointment details:
- Appointment ID
- Patient ID
- Doctor ID
- Appointment Date
- Appointment Time
Store appointment information.
b) show_appointments()
Display all booked appointments."""
def  book_appointment():
    appoint=[]
    napp=input("enter appointment")
    pid=input("enter PATIENT  ID")
    did=input("enter Doctor  ID")
    adate=(input("enter the date"))
    atime=input("enter the time")
    dic={"Appointment ID":napp,
         "Patient ID":pid,
         "Doctor ID":did,
         "Appointment Date":adate,
         "Appointment Time":atime
         }
    appoint.append(dic)
    print("doctor added successfully")
    return appoint
def show_appointments(appoint):
    for i in appoint:
        for k,v in i.items():
            print(k,":",v)
