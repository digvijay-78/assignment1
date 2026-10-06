customers=[]
class Customer:
    def __init__(self):
        self.id=input("enter the id").lower()
        self.name=input("enter the name of customer")
        self.city=input("enter the city").lower()
        self.purchase_amount=float(input("enter the purchase price"))
        customers.append(self)
    def display(self):
        for i in customers:
            print(i.id,i.name,i.city,i.purchase_amount)
    def particular_city(self):
        self.particular=input("enter the city").lower()
        for i in customers:
            if i.city==self.particular:
                print(i.id,i.name,i.city,i.purchase_amount)
    def greater_10k(self):
        for i in customers:
            if i.purchase_amount>10000:
                print(i.id,i.name,i.city,i.purchase_amount)
    def high(self):
        a=customers[0]
        for i in customers:
            if i.purchase_amount>a.purchase_amount:
                a=i
        print("Highest Purchase Customer:\n",a.id,a.name,a.city,a.purchase_amount)
    def total_sale(self):
        self.a=0
        self.c=0
        for i in customers:
            self.a+=i.purchase_price
            self.c+=1
        print("Total Sales:\n",self.a)
    def avg(self):
        self.average=self.a/self.c
        print("Average Purchase Amount:\n",self.average)
    def customer(self):
        c=input("enter the customer id").lower()
        for i in customers:
            if i.id==c:
                print("Customer Found:\n",i.id,i.name,i.city,i.purchase_amount)