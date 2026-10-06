"""Assignment 3: Bank Account Operations
 A bank wants to perform basic operations on a customer's account.
Create a class BankAccount with the following attributes:
Account number
Account holder name
Balance
Create the following methods:
deposit() – Add an amount to the balance.
withdraw() – Subtract an amount from the balance.
display_account() – Display account details and final balance.
Sample data:
Account Number: 1001
Account Holder: Rahul
Opening Balance: 25000
Deposit: 5000
Withdrawal: 3000
Expected result:
Final Balance: 27000"""
class bank:
    def accept(self,no,name,balance):
        self.name=name
        self.no=no
        self.balance=balance
    def deposit(self,dep):
        self.dep=dep
        self.d=self.balance+self.dep
    def withdrawal(self,wit):
        self.wit=wit
        self.m=self.d-self.wit
    def display(self):
        print("Final Balance:",self.m)
ba=bank()
a=input("Account Number:")
b=input("Account Holder: ")
c=float(input("Opening Balance:"))

ba.accept(a,b,c)

l=float(input("Deposit:"))
s=float(input("Withdrawal: "))
ba.deposit(l)
ba.withdrawal(s)
ba.display()