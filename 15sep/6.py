"""Assignment 6: Electricity Bill Calculator

An electricity board wants to calculate a customer's electricity bill based on units consumed.

Create a class ElectricityBill with the following attributes:

Consumer number

Consumer name

Units consumed

Rate per unit

Fixed charge

Create the following methods:

calculate_energy_charge() – Calculate units × rate per unit.

calculate_total_bill() – Add energy charge and fixed charge.

display_bill() – Display consumer details and bill amount.

Sample data:

Consumer Number: 501
Consumer Name: Amit
Units Consumed: 250
Rate Per Unit: 6
Fixed Charge: 100

Expected result:

Energy Charge: 1500
Total Bill: 1600"""

class bill:
    def accept(self,no,name,unit,rate,charge):
        self.name=name
        self.no=no
        self.unit=unit
        self.rate=rate
        self.charge=charge
    def energy(self):
        self.cal=self.unit*self.rate
    def total(self):
        self.bill=(self.unit*self.rate)+self.charge
    def display(self):
        print(f"""Energy Charge:{self.cal}
Total Bill:{self.bill}""")
b=bill()
a=input("enter the no")
c=input("enter the name")
d=int(input("unit consumed"))
r=int(input("enter the rate per unit"))
f=float(input("enter the fixed charge"))
b.accept(a,c,d,r,f)
b.energy()
b.total()
b.display()