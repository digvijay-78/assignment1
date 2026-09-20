products=[]
class product:
    def __init__(self) :
        self.id=input("enter the id of the product : ")
        self.name=input("enter the product name : ")
        self.price=float(input("enter the product price : "))
        self.quantity=int(input("enter the product quantity : "))
        products.append(self)
    def display(self):
        for i in products:
            print("\nAll Products:\n",i.id,i.name,i.price,i.quantity)
    def total_value(self):
        for i in products:
            print("\nProduct Total Values:\n",i.name,"=",i.price*i.quantity)
    def low_stock(self):
        print("Low Stock Products:")
        for i in products:
            if i.quatity<10:
                print(i.name)
    def high_price(self):
        print("Highest Price Product:")
        
