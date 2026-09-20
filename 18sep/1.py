"""QNO 1: Bank Account Management System
ABC Bank wants to develop a software application to manage customer accounts.
Each customer has:
Account Number
Customer Name
Account Balance
A customer should be able to:
Deposit money
Withdraw money
Check account balance
Transfer money to another customer
The bank also wants to maintain information that is common for all customers:
Bank Name
Interest Rate
The bank management may change the interest rate in the future, and the 
change should apply to all customers.
Additionally, the application should provide some utility operations:
Validate whether an account number is valid.
Calculate interest on a given amount.
Generate a transaction ID.
Requirements
Class Variables
bank_name
interest_rate
Instance Variables
account_no
customer_name
balance
Instance Methods
deposit(amount)
withdraw(amount)
transfer_money(receiver, amount)
display_balance()
Class Methods
change_interest_rate(new_rate)
change_bank_name(new_name)
display_bank_info()
Static Methods
validate_account_number(account_no)
calculate_interest(amount, rate)
generate_transaction_id()
Sample Input
Customer 1
Account No : 1001
Name       : deepika
Balance    : 50000
Customer 2
Account No : 1002
Name       : Priya
Balance    : 30000
Deposit Amount : 10000
Transfer Amount : 15000
New Interest Rate : 7.5
Sample Output
Customer : deepika
Balance  : 45000
Customer : Priya
Balance  : 45000
Bank Name      : ABC Bank
Interest Rate  : 7.5%
Transaction ID : TXN1025
Task: Design a Python class named BankAccount and implement all
the above methods using instance methods, class methods, and static 
methods appropriately."""

class BankAccount:
    bank_name="ABC Bank"
    interest_rate=5.0
    def __init__(self,no,name,balance):
        self.no=int(input("enter the account no."))
        self.name=input("enter the account holder name")
        self.balance=int(input("enter the account balance"))


    def deposit(self):
       self.deposit_money=int(input("enter the deposit:"))

       self.balance=self.balance+self.deposit_money
       print("Deposit money :",self.deposit_money)
    def withdraw(self):
        self.withdraw_money=int(input("enter the amount to withdraw"))
        if self.withdraw_money<self.balance:

            self.balance=self.balance-self.deposit_money 
            print("withdraw amount :",self.withdraw_money)
        else:
            print("withdraw not possible ")
    def transfer(self,receiver, amount):
        self.receiver=receiver
        self.balance=self.balance-amount
        receiver.balance=receiver.balance+amount
    def display(self):
        print(f"""Customer : {self.name}
Balance  : {self.balance}""")
    @classmethod
    def change_interest_rate(cls,new_rate):
        cls.interest_rate=new_rate
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
    @classmethod
    def  display_bank_info(cls):
        print(f"""Bank Name      :{cls.bank_name}
Interest Rate  : {cls.interest_rate}""")      
