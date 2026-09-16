"""Assignment 5: Shopping Bill Calculator
 A retail shop wants to calculate the total bill for a customer.
Create a class ShoppingBill with the following attributes:
Product name
Product price
Quantity
Discount percentage
GST percentage
Create the following methods:
calculate_subtotal() – Calculate price × quantity.
calculate_discount() – Calculate the discount amount.
calculate_gst() – Calculate GST on the discounted amount.
calculate_final_bill() – Calculate the final payable amount.
display_bill() – Display the complete bill details.
Formula:
Subtotal = Price × Quantity
Discounted Amount = Subtotal - Discount
GST = Discounted Amount × GST Percentage / 100
Final Bill = Discounted Amount + GST"""
class shopping:
    def accept(self,n,p,q,di,g):
        self.n=n
        self.p=p
        self.q=q
        self.di=di
        self.g=g
    def sub(self):
        self.s=self.p*self.q
    def dis(self):
        self.d=(self.p*self.q)-self.di
    def gst(self):
        self.gs=(((self.p*self.q)-self.di)*self.g)/100
    def final(self):
        self.fi=((self.p*self.q)-self.di)+self.g
    def display(self):
        print(f"""name:{self.n}
subtotal :{self.s}
discount : {self.d}
GST : {self.gs}
final : {self.fi}""")
k=shopping()
name=input("enter the name:")
price=float(input("enter the price"))
quality=int(input("enter the quality"))
percentage=float(input("enter the discount percentage"))
gs=float(input("gst percentage"))
k.accept(name,price,quality,percentage,gs)
k.sub()
k.dis()
k.gst()
k.final()
k.display()