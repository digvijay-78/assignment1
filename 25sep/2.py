"""
Assignment 2 – Vehicle Rental System
Create a parent class Vehicle with:
vehicle_no
brand
rent_per_day
Create two child classes:
Car
Bike
Requirements
Take vehicle details and number of rental days from the user.
Use super() to initialize common attributes.
Create a method calculate_rent(days) in the parent class.
Override the method in both child classes.
For a Car, add ₹500 service charge to the rental amount.
For a Bike, add ₹200 service charge.
Display the final rental amount.
Sample Input
Enter Vehicle Number: MP09AB1234
Enter Brand: Honda
Enter Rent Per Day: 800
Enter Number of Days: 3
Enter Vehicle Type: Car
Expected Output
----- Rental Details -----
Vehicle Number : MP09AB1234
Brand          : Honda
Rent Per Day   : 800
Number of Days : 3
Vehicle Type   : Car
Rental Amount  : 2400
Service Charge : 500
Final Amount   : 2900"""

class Vehicle:
    def __int__(self,vehicle_no,brand,rent_per_day):
        self.vehicle_no=vehicle_no
        self.brand=brand
        self.rent_per_day=rent_per_day
        self.days=int(input("enter the no of days :"))
    def calculate_rent(self,days):
        self.days=days
        self.v= self.days*self.rent_per_day
        return self.v
    def display(self):
        print(f"""----- Rental Details -----
Vehicle Number : {self.vehicle_no}
Brand          : {self.brand}
Rent Per Day   : {self.rent_per_day}
Number of Days : {self.days}""")
class Car(Vehicle):
    def __int__(self, vehicle_no, brand, rent_per_day):
        return super().__int__(vehicle_no, brand, rent_per_day)
    
    def calculate_rent(self):
        super().calaculate_rent()
        self.m=self.v+500
        return self.m
    def display(self):
        super().display()
        print(f"""Vehicle Type   : Car
Rental Amount  : {self.v}
Service Charge : 500
Final Amount   : {self.m}""")

class Bike(Vehicle):
    def __int__(self, vehicle_no, brand, rent_per_day):
        return super().__int__(vehicle_no, brand, rent_per_day)
    def calculate_rent(self):
        super().calaculate_rent()
        self.m=self.v+200
    
    def display(self):
        super().display()
        print(f"""Vehicle Type   : Bike
Rental Amount  : {self.v}
Service Charge : 200
Final Amount   : {self.m}""")

no=input("Enter Vehicle Number:  ")
b=input("Enter Brand:")
rent=int(input("Enter Rent Per Day:"))
day=int(input("Enter Number of Days:"))
type=input("Enter Vehicle Type: ").lower()

if type=="car":
    c=Car()
    c.display()
elif type =="bike":
    b=Bike()
else:
    print("invalid vehicle type ")