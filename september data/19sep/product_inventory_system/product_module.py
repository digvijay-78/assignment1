products=[]
class product:
    def __init__(self) :
        self.id=input("enter the id of the product : ").lower()
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
            if i.quantity<10:
                print(i.name)
    def high_price(self):
        print("Highest Price Product:")
        a=0
        highest=[]
        for i in products:
            if a<i.price:
                a=i.price
                highest.append(i)
        print(highest[-1].name,a,"\n")
    def total_investment(self):
        v=0
        for i in products:
            print("Total Inventory Value:")
            v+=i.price*i.quantity
            print(v)
    def search(self):
        s=input("enter the id").lower()
        print("Searching... Product Id: ",s)
        for i in products:
            if i.id==s:
                print("\nProduct Found:\n",i.id,i.name,i.price,i.quantity)
        else:
            print("not found")