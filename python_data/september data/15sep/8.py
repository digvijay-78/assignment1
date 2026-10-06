"""Assignment 8: Car Mileage Calculator
 A car owner wants to calculate the mileage and fuel cost of a journey.
Create a class Car with the following attributes:
Car brand
Car model
Distance travelled in km
Fuel consumed in litres
Petrol price per litre
Create the following methods:
calculate_mileage() – Calculate kilometres per litre.
calculate_fuel_cost() – Calculate total fuel cost.
display_trip_details() – Display car and journey details.
Formulas:
Mileage = Distance / Fuel Consumed
Fuel Cost = Fuel Consumed × Petrol Price
Sample data:
Car Brand: Maruti
Car Model: Swift
Distance: 320 km
Fuel Consumed: 20 litres
Petrol Price: 105"""

class car:
    def accept(self,brand,model,km,fuel,petrol):
        self.brand=brand
        self.model=model
        self.km=km
        self.fuel=fuel
        self.petrol=petrol
    def milage(self):
        self.mil=self.km/self.fuel
    def cost(self):
        self.fuelcost=self.fuel*self.petrol
    def display(self):
        print(f"""Car Brand: {self.brand}
Car Model: {self.model}
Distance: {self.km}km
Fuel Consumed: {self.fuel} litres
Petrol Price: {self.petrol}
milage : {self.mil}
petrol price : {self.fuelcost}""")

c=car()
c.accept("maruti","swift",320,20,105)
c.milage()
c.cost()
c.display()