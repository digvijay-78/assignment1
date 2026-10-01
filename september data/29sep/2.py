"""
============================================================
QUESTION 2: HOSPITAL PATIENT BILLING SYSTEM
============================================================
Develop a MENU-DRIVEN Hospital Patient Billing System.
The hospital treats different categories of patients:
1. General Patient
2. Emergency Patient
3. Insurance Patient
4. Corporate Patient
Every patient must perform common operations such as:
calculate_bill()
calculate_discount()
calculate_final_amount()
generate_bill()
However, the calculation rules are different for each type
of patient.
Therefore, use ABSTRACTION to design the system.
------------------------------------------------------------
ABSTRACT CLASS:
------------------------------------------------------------
Create an abstract class:
Patient
It should contain appropriate abstract methods required for
billing.
Create the following child classes:
1. GeneralPatient
2. EmergencyPatient
3. InsurancePatient
4. CorporatePatient
------------------------------------------------------------
MAIN MENU:
-----------------------------------------------------------
========================================
       HOSPITAL MANAGEMENT SYSTEM
========================================
1. Register Patient
2. Generate Patient Bill
3. View Patient Bill
4. Exit
Enter your choice:
------------------------------------------------------------
OPTION 1: REGISTER PATIENT
------------------------------------------------------------
Input:
Patient ID
Patient Name
Patient Age
Then display:
1. General Patient
2. Emergency Patient
3. Insurance Patient
4. Corporate Patient
Enter patient type:
------------------------------------------------------------
GENERAL PATIENT:
------------------------------------------------------------
Consultation Fee : Rs.500
Room Charge       : Rs.1000 per day
Medicine Charge   : Actual amount
Discount          : No discount
Input:
Number of Days
Medicine Charge
------------------------------------------------------------
EMERGENCY PATIENT:
------------------------------------------------------------
Consultation Fee : Rs.1000
Emergency Charge : Rs.500
Room Charge       : Rs.2000 per day
Medicine Charge   : Actual amount
Discount          : No discount
Input:
Number of Days
Medicine Charge
------------------------------------------------------------
INSURANCE PATIENT:
------------------------------------------------------------
Consultation Fee : Rs.800
Room Charge       : Rs.1500 per day
Medicine Charge   : Actual amount
Insurance covers 70% of the total hospital bill.
Patient pays remaining 30%.
Input:
Number of Days
Medicine Charge
------------------------------------------------------------
CORPORATE PATIENT:
------------------------------------------------------------
Consultation Fee : Rs.700
Room Charge       : Rs.1200 per day
Medicine Charge   : Actual amount
Corporate Discount = 20%
Input:
Number of Days
Medicine Charge
------------------------------------------------------------
SAMPLE INPUT:
------------------------------------------------------------
Enter Patient ID: P1025
Enter Patient Name: Rajesh
Enter Patient Age: 42
Select Patient Type:
1. General
2. Emergency
3. Insurance
4. Corporate
Enter choice: 3
Enter Number of Days: 4
Enter Medicine Charge: 3500
------------------------------------------------------------
EXPECTED OUTPUT:
------------------------------------------------------------
========================================
            PATIENT BILL
========================================
Patient ID       : P1025
Patient Name     : Rajesh
Patient Age      : 42
Patient Type     : Insurance
Consultation Fee : Rs.800.00
Room Charges     : Rs.6000.00
Medicine Charges : Rs.3500.00
----------------------------------------
Total Hospital Bill : Rs.10300.00
Insurance Coverage  : 70%
Insurance Amount    : Rs.7210.00
Patient Payable     : Rs.3090.00
Bill Status         : GENERATED
========================================
------------------------------------------------------------
OPTION 2: GENERATE PATIENT BILL
------------------------------------------------------------
Ask:
Enter Patient ID:
If patient exists, generate and display the bill according
to the patient's type.
The calculation must be performed by the appropriate child
class.
------------------------------------------------------------
OPTION 3: VIEW PATIENT BILL
------------------------------------------------------------
Ask:
Enter Patient ID:
Display the complete patient bill.
If patient does not exist:
Patient record not found.
------------------------------------------------------------
OPTION 4:
------------------------------------------------------------
Display:
Thank you for using Hospital Management System."""


from abc import ABC,abstractmethod
class Patient(ABC):
    def __init__(self,id,name,age) :
        self.id=id
        self.name=name
        self.age=age
    @abstractmethod
    def calculate_bill(self):
        pass
    @abstractmethod
    def calculate_discount(self):
        pass
    @abstractmethod
    def calculate_final_amount(self):
        pass
    @abstractmethod
    def generate_bill(self):
        pass

class GeneralPatient(Patient):
    def __init__(self, id, name, age,medical,days,charge):
        super().__init__(id, name, age)
        self.Consultation=500
        self.room=10000
        self.medical=medical
        self.discount=0
        self.days=days
        self.charge=charge
    def calculate_bill(self):
        pass
    def calculate_discount(self):
        pass
    def calculate_final_amount(self):
        pass
    def generate_bill(self):
        pass
class EmergencyPatient(Patient):
    def calculate_bill(self):
        pass
    def calculate_discount(self):
        pass
    def calculate_final_amount(self):
        pass
    def generate_bill(self):
        pass
class InsurancePatient(Patient):
    def calculate_bill(self):
        pass
    def calculate_discount(self):
        pass
    def calculate_final_amount(self):
        pass
    def generate_bill(self):
        pass
class CorporatePatient(Patient):
    def calculate_bill(self):
        pass
    def calculate_discount(self):
        pass
    def calculate_final_amount(self):
        pass
    def generate_bill(self):
        pass

while True:
    print("""------------------------------------------------------------
MAIN MENU:
-----------------------------------------------------------
========================================
       HOSPITAL MANAGEMENT SYSTEM
========================================
1. Register Patient
2. Generate Patient Bill
3. View Patient Bill
4. Exit
Enter your choice:""")
    menu=int(input("enter the choice:"))
    match menu:
        case 1:
            print("""------------------------------------------------------------
OPTION 1: REGISTER PATIENT
------------------------------------------------------------""")
            pid=input("enter the id: ")
            pname=input("enter the name:")
            page=int(input("enter the age:"))
            print("""1. General Patient
2. Emergency Patient
3. Insurance Patient
4. Corporate Patient
Enter patient type:""")
            amenu=int(input("enter the choice"))
            match amenu:
                case 1:
                    print("""------------------------------------------------------------
GENERAL PATIENT:
------------------------------------------------------------""")
                case 2:
                    print("""------------------------------------------------------------
EMERGENCY PATIENT:
------------------------------------------------------------""")
                case 3:
                    print("""------------------------------------------------------------
INSURANCE PATIENT:
------------------------------------------------------------""")
                case 4:
                    print("""------------------------------------------------------------
CORPORATE PATIENT:
------------------------------------------------------------""")
                case _ :
                    print("invalid choice")
        case 2:
            print("Generate Patient Bill")    
        case 3:
            print(" View Patient Bill")
        case 4:
            print("thankyou for visisting ")
            break
        case _ :
            print("invalid choice")