"""Assignment 9: Product Inventory Management
A shopkeeper wants to manage the stock of a product.
Create a class Product with the following attributes:
Product ID
Product name
Price
Available quantity
Create the following methods:
add_stock() – Increase the available quantity.
sell_product() – Decrease the available quantity.
calculate_stock_value() – Calculate price × available quantity.
display_product() – Display product and stock details.
Sample operations:
Product Name: Laptop
Price: 45000
Initial Quantity: 10
Add Stock: 5
Sell Product: 3
Expected result:
Available Quantity: 12
Total Stock Value: 540000"""

class product:
    def accept(self,id,name,price,quantity):
        self.id=id
        self.name=name
        self.price=price
        self.quantity=quantity
    def add_stock(self,a):
        self.a=a
        self.add=self.quantity+self.a
    def sell(self,b):
        self.b=b
        if self.a==0:
            self.s=self.quantity-self.b
        else:
            self.s=self.add-self.b
    def display(self):