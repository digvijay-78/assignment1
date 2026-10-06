accounts=[]
class Account:
    def __init__(self):
        self.no=input("enter the account no").lower()
        self.name=input("enter the account holder name")
        self.balance=float(input("enter the balance"))
        accounts.append(self)
    def display(self):
        for i in accounts:
            print(i.no,i.name,i.balance)
    def search(self):
        a=input("enter the account no").lower()
        for i in accounts:
            if i.no==a:
                print(i.no,i.name,i.balance)
                return
        print("id not found")
    def deposit(self):
        a = input("Enter account no: ").lower()
        b = float(input("Enter amount to deposit: "))
        for i in accounts:
            if i.no==a:
                i.balance=i.balance+b
                print("after deposit\n")
                print(i.no,i.name,i.balance)
                return 
        print("account not found")
    def withdraw(self):
        a = input("Enter account no: ").lower()
        b = float(input("Enter amount to deposit: "))
        for i in accounts:
            if i.no==a:
                i.balance=i.balance-b
                print("after withdrwal\n")
                print(i.no,i.name,i.balance)
                return 
        print("account not found")
    def greater_50k(self):
        print("\nAccounts having balance greater than 50000:\n")
        for i in accounts:
            if i.balance>50000:
                print(i.no,i.name,i.balance)
    def high_balance(self):
        h=accounts[0]
        for i in accounts:
            if i.balance>h.balance:
                h=i
        print("\nHighest Balance Account:\n",h.no,h.name,h.balance)
        