# from abc import ABC,abstractmethod
# class Bank(ABC):
#     @abstractmethod
#     def intrest(self):
#         pass 
# o=Bank()#TypeError: Can't instantiate abstract class Bank without an implementation for abstract method 'intrest'

# from abc import ABC,abstractmethod
# class Bank(ABC):
#     @abstractmethod
#     def intrest(self):
#         pass
#     @abstractmethod
#     def adhar(self):
#         pass 
# class SBI(Bank):
#     def intrest(self):
#         print("abc")
#         return super().intrest()
# class HDFC(Bank):
#     def intrest(self):
#         print("HDFC intrest rate 8.0")
# o=SBI()#TypeError: Can't instantiate abstract class SBI without an implementation for abstract method 'adhar'
# o.intrest()
# o2=HDFC()
# o2.intrest()

# from abc import ABC,abstractmethod
# class Shape(ABC):
#     def __init__(self) :
#         print("this is constructor of shape class")
#     @abstractmethod
#     def area(self):
#         pass
#     def hello(self):
#         print("hello guys")
# class Circle(Shape):
#     def __init__(self,r) :
#         self.r=r
#         super().__init__()
#     def area(self):
#         return 3.14 *self.r*self.r
# c=Circle(5)
# print(c.area())#78.5
# c.hello()
# #this is constructor of shape class
# # 78.5
# # hello guys

# from abc import ABC,abstractmethod
# class Emp(ABC):
#     def __init__(self,name,salary) :
#         self.name=name
#         self.salary=salary
#     @abstractmethod
#     def cal(self):
#         pass
#     def display(self):
#         print("name is ",self.name,"and salary is ",self.salary)

# class Manager(Emp):
#     def cal(self):
#         bonus=self.salary*0.20
#         print("manager bonus ",bonus)

# class Devloper(Emp):
#     def cal(self):
#         bonus=self.salary*0.10
#         print("developer bonus is",bonus)

# obj1=Manager("deep",90000)
# obj1.display()
# obj1.cal()
# obj2=Devloper("rash",80000)
# obj2.display()
# obj2.cal()
# """name is  deep and salary is  90000
# manager bonus  18000.0
# name is  rash and salary is  80000
# developer bonus is 8000.0"""



'''
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
------------------------------------------------------------

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

Thank you for using Hospital Management System.
'''

from abc import ABC,abstractmethod

class Patient(ABC):
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
    def _init_(self,patient_id,patient_age,patient_name,med_charges,no_days):
        self.patient_id = patient_id
        self.patient_age = patient_age
        self.patient_name = patient_name
        self.med_charges = med_charges
        self.no_days = no_days
        self.patient_type = "General"
        
    def calculate_bill(self):
        self.room_charges = self.no_days * 1000
        self.bill = self.room_charges + self.med_charges + 500
        return self.bill
     
    def calculate_discount(self):
        self.discount = 0*self.bill
     
    def calculate_final_amount(self):
        self.final_bill = self.bill - self.discount
    
    def generate_bill(self):
        print(f"""

========================================
            PATIENT BILL
========================================

Patient ID       : {self.patient_id}
Patient Name     : {self.patient_name}
Patient Age      : {self.patient_age}
Patient Type     : {self.patient_type}

Consultation Fee : Rs.500.00
Room Charges     : Rs.{self.room_charges}
Medicine Charges : Rs.{self.med_charges}

----------------------------------------

Total Hospital Bill : Rs.{self.bill}

Discount Percentage : 0%
Discount Amount     : Rs.0

Patient Payable     : Rs.{self.final_bill}

Bill Status         : GENERATED

========================================""")

    

class EmergencyPatient(Patient):
    def _init_(self,patient_id,patient_age,patient_name,med_charges,no_days):
        self.patient_id = patient_id
        self.patient_age = patient_age
        self.patient_name = patient_name
        self.med_charges = med_charges
        self.no_days = no_days
        self.patient_type = "Emergency"
        
    def calculate_bill(self):
        self.room_charges = self.no_days * 2000
        self.bill = self.room_charges + self.med_charges + 1000 + 500
        return self.bill
     
    def calculate_discount(self):
        self.discount = 0*self.bill
     
    def calculate_final_amount(self):
        self.final_bill = self.bill - self.discount
    
    def generate_bill(self):
        print(f"""

========================================
            PATIENT BILL
========================================

Patient ID       : {self.patient_id}
Patient Name     : {self.patient_name}
Patient Age      : {self.patient_age}
Patient Type     : {self.patient_type}

Consultation Fee : Rs.1000.00
Room Charges     : Rs.{self.room_charges}
Medicine Charges : Rs.{self.med_charges}

----------------------------------------

Total Hospital Bill : Rs.{self.bill}

Discount Percentage : 0%
Discount Amount     : Rs.0

Patient Payable     : Rs.{self.final_bill}

Bill Status         : GENERATED

========================================""")
    

class InsurancePatient(Patient):
    def _init_(self,patient_id,patient_age,patient_name,med_charges,no_days):
        self.patient_id = patient_id
        self.patient_age = patient_age
        self.patient_name = patient_name
        self.med_charges = med_charges
        self.no_days = no_days
        self.patient_type = "Insurance"
        
    def calculate_bill(self):
        self.room_charges = self.no_days * 1500
        self.bill = self.room_charges + self.med_charges + 800
        return self.bill
     
    def calculate_discount(self):
        self.discount = 0.7*self.bill
     
    def calculate_final_amount(self):
        self.final_bill = self.bill - self.discount
    
    def generate_bill(self):
        print(f"""

========================================
            PATIENT BILL
========================================

Patient ID       : {self.patient_id}
Patient Name     : {self.patient_name}
Patient Age      : {self.patient_age}
Patient Type     : {self.patient_type}

Consultation Fee : Rs.800.00
Room Charges     : Rs.{self.room_charges}
Medicine Charges : Rs.{self.med_charges}

----------------------------------------

Total Hospital Bill : Rs.{self.bill}

Insurance Coverage  : 70%
Insurance Amount    : Rs.{self.discount}

Patient Payable     : Rs.{self.final_bill}

Bill Status         : GENERATED

========================================""")

class CorporatePatient(Patient):
    def _init_(self,patient_id,patient_age,patient_name,med_charges,no_days):
        self.patient_id = patient_id
        self.patient_age = patient_age
        self.patient_name = patient_name
        self.med_charges = med_charges
        self.no_days = no_days
        self.patient_type = "Corporate"
        
    def calculate_bill(self):
        self.room_charges = self.no_days * 1200
        self.bill = self.room_charges + self.med_charges + 700
     
    def calculate_discount(self):
        self.discount = 0.2*self.bill
     
    def calculate_final_amount(self):
        self.final_bill = self.bill - self.discount
    
    def generate_bill(self):
        print(f"""

========================================
            PATIENT BILL
========================================

Patient ID       : {self.patient_id}
Patient Name     : {self.patient_name}
Patient Age      : {self.patient_age}
Patient Type     : {self.patient_type}

Consultation Fee : Rs.700.00
Room Charges     : Rs.{self.room_charges}
Medicine Charges : Rs.{self.med_charges}

----------------------------------------

Total Hospital Bill : Rs.{self.bill}

Discount Percentage : 20%
Discount Amount     : Rs.{self.discount}

Patient Payable     : Rs.{self.final_bill}

Bill Status         : GENERATED

========================================""")

patient_id = False
while True:
    print("""
========================================
       HOSPITAL MANAGEMENT SYSTEM
========================================

1. Register Patient
2. Generate Patient Bill
3. View Patient Bill
4. Exit""")

    ch = int(input("Enter your choice: "))
    match ch:
        case 1:
            patient_id = input("Enter Patient ID: ")
            patient_name = input("Enter Patient Name: ")
            patient_age = int(input("Enter Patient Age: "))

            print("""
1. General Patient
2. Emergency Patient
3. Insurance Patient
4. Corporate Patient
""")        
            choice=int(input("Enter patient type: "))
            match choice:
                case 1:
                    
                    print("""
Consultation Fee : Rs.500
Room Charge       : Rs.1000 per day
Medicine Charge   : Actual amount
Discount          : No discount""")
                    no_days = int(input("Number of Days: "))
                    med_charges = int(input("Medicine Charges: "))
                    obj = GeneralPatient(patient_id,patient_age,patient_name,med_charges,no_days)


                case 2:
                    print("""
Consultation Fee : Rs.1000
Emergency Charge : Rs.500
Room Charge       : Rs.2000 per day
Medicine Charge   : Actual amount
Discount          : No discount""")
                    no_days = int(input("Number of Days: "))
                    med_charges = int(input("Medicine Charges: "))
                    obj = EmergencyPatient(patient_id,patient_age,patient_name,med_charges,no_days)


                case 3:
                    print("""
Consultation Fee : Rs.800
Room Charge       : Rs.1500 per day
Medicine Charge   : Actual amount

Insurance covers 70% of the total hospital bill.

Patient pays remaining 30%.""")
                    no_days = int(input("Number of Days: "))
                    med_charges = int(input("Medicine Charges: "))
                    obj = InsurancePatient(patient_id,patient_age,patient_name,med_charges,no_days)
                    

                case 4:
                    print("""
Consultation Fee : Rs.700
Room Charge       : Rs.1200 per day
Medicine Charge   : Actual amount

Corporate Discount = 20%""")
                    no_days = int(input("Number of Days: "))
                    med_charges = int(input("Medicine Charges: "))
                    obj = CorporatePatient(patient_id,patient_age,patient_name,med_charges,no_days)
        
        case 2:
            pat_id = input("Enter Patient ID: ")
            if pat_id != patient_id:
                print("Not Available")
            else:
                obj.calculate_bill()
                obj.calculate_discount()
                obj.calculate_final_amount()
                obj.generate_bill()

        case 3:
            pat_id = input("Enter Patient ID: ")
            if pat_id == patient_id:
                obj.calculate_bill()
                obj.calculate_discount()
                obj.calculate_final_amount()
                obj.generate_bill()
            else:
                print("Patient record not found.")
            
        
        case 4:
            print("Thank you for using Hospital Management System.")
            break
