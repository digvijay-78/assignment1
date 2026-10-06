"""
5. Main Application
Create main.py file.
Create a menu-driven program.
Menu:
========== Hospital Management System ==========
1. Add Patient
2. Display Patients
3. Search Patient
4. Add Doctor
5. Display Doctors
6. Book Appointment
7. Show Appointments
8. Generate Bill
9. Exit
According to user choice call the required functions from packages."""

patient=[]
doctor=[]
appoint=[]
import appointment_management_package
import billing_management_package
import doctor_management_package
import patient_management_package
while True:
    print("""Menu:
========== Hospital Management System ==========
1. Add Patient
2. Display Patients
3. Search Patient
4. Add Doctor
5. Display Doctors
6. Book Appointment
7. Show Appointments
8. Generate Bill
9. Exit""")
    choice=(input("enter the choice"))
    match choice:
        case 1:
            print(" Add Patient")
            patient=patient_management_package.add()
        
        case 2:
            print("Display Patients")
            patient_management_package.display_patients(patient)

        case 3:
            print("Search Patient")
            patient_management_package.search_patient(patient)
        case 4:
            print("Add Doctor") 
            doctor=doctor_management_package.dadd()
        case 5:
            print("Display Doctors")
            doctor_management_package.display_doctors(doctor)
        case 6:
            print("Book Appointment")
            appointment_management_package.book_appointment()
        case 7:
            print("Show Appointments")
            appointment_management_package.show_appointments(appoint)
        case 8:
            print("Generate Bill")
            billing_management_package.billing.generate_bill() 

        case 9:
            print("Exiting.......")
            break
        case _:
            print("invalid choice")
