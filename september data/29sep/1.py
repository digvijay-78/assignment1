"""============================================================
QUESTION 1: ONLINE PAYMENT MANAGEMENT SYSTEM
============================================================
Develop a MENU-DRIVEN Online Payment Management System for an
e-commerce company.
The company supports different payment methods:
1. UPI
2. Credit Card
3. Debit Card
4. Net Banking
5. Wallet
Every payment method follows a common payment process, but the
actual validation, authentication, processing fee and payment
processing logic are different.
Therefore, the system must be designed using ABSTRACTION.
------------------------------------------------------------
ABSTRACT CLASS:
------------------------------------------------------------
Create an abstract class named:
Payment
The class should define the following abstract methods:
1. validate_payment()
2. calculate_processing_fee()
3. authenticate_payment()
4. process_payment()
5. generate_receipt()
Create separate child classes for:
1. UPIPayment
2. CreditCardPayment
3. DebitCardPayment
4. NetBankingPayment
5. WalletPayment
Each child class must provide its own implementation of all
required abstract methods.
-----------------------------------------------------------
MAIN MENU:
------------------------------------------------------------
========================================
       ONLINE PAYMENT SYSTEM
========================================
1. Make Payment
2. View Payment Details
3. Exit
Enter your choice:
------------------------------------------------------------
OPTION 1: MAKE PAYMENT
------------------------------------------------------------
Ask the user to enter:
Customer Name
Order ID
Order Amount
Then display:
Select Payment Method
1. UPI
2. Credit Card
3. Debit Card
4. Net Banking
5. Wallet
Enter your choice:
------------------------------------------------------------
UPI:
------------------------------------------------------------
Input:
UPI ID
UPI PIN
Processing Fee:
0%
-----------------------------------------------------------
CREDIT CARD:
------------------------------------------------------------
Input:
Card Number
Card Holder Name
CVV
Expiry Date
Processing Fee:
2% of Order Amount
------------------------------------------------------------
DEBIT CARD:
------------------------------------------------------------
Input:
Card Number
Card Holder Name
CVV
Expiry Date
Processing Fee:
1% of Order Amount
------------------------------------------------------------
NET BANKING:
------------------------------------------------------------
Input:
Bank Name
Account Number
Customer ID
Processing Fee:
0.5% of Order Amount
------------------------------------------------------------
WALLET:
------------------------------------------------------------
Input:
Wallet Name
Mobile Number
Wallet PIN
Processing Fee:
1.5% of Order Amount
------------------------------------------------------------
SAMPLE INPUT:
------------------------------------------------------------
Enter Customer Name: Rahul
Enter Order ID: ORD1052
Enter Order Amount: 5000
Select Payment Method:
1. UPI
2. Credit Card
3. Debit Card
4. Net Banking
5. Wallet
Enter your choice: 2
Enter Card Number: 4567891234567890
Enter Card Holder Name: Rahul Singh
Enter CVV: 321
Enter Expiry Date: 12/29
------------------------------------------------------------
EXPECTED OUTPUT:
------------------------------------------------------------
========================================
          PAYMENT PROCESSING
========================================
Customer Name       : Rahul
Order ID            : ORD1052
Payment Method      : Credit Card
Order Amount        : Rs.5000.00
Processing Fee      : Rs.100.00
Final Amount        : Rs.5100.00
Validating payment details...
Payment details validated successfully.
Authenticating payment...
Authentication successful.
Processing payment...
Payment processed successfully.
Transaction ID      : TXN785421
Payment Status      : SUCCESS
========================================
OPTION 2: VIEW PAYMENT DETAILS
------------------------------------------------------------
Ask:
Enter Order ID:
If the order exists, display:
Order ID
Customer Name
Payment Method
Order Amount
Processing Fee
Final Amount
Transaction ID
Payment Status
If the order does not exist:
Payment record not found.
OPTION 3:
Display:
Thank you for using Online Payment System.
"""
from abc import ABC,abstractmethod
class Payment(ABC):
    def __init__(self,customer_name,order_id,order_amount):
        self.customer=customer_name
        self.order_id=order_id
        self.order_amount=order_amount
    @abstractmethod
    def validate_payment(self):
        pass
    @abstractmethod
    def calculate_processing_fee(self):
        pass
    @abstractmethod
    def authenticate_payment(self):
        pass
    @abstractmethod
    def process_payment(self):
        pass
    @abstractmethod
    def generate_receipt(self):
        pass

class UPIPayment(Payment):
    def __init__(self, customer_name, order_id, order_amount,upi_id,upi_pin,processing_upi_fee):
        super().__init__(customer_name, order_id, order_amount)
        self.upi_id=upi_id
        self.upi_pin=upi_pin
        self.processing_upi_fee=processing_upi_fee
    def validate_payment(self):
        return "Payment details validated successfully."
    def calculate_processing_fee(self):
        self.processing_fee = self.order_amount * self.processing_upi_fee / 100
        self.f_amount = self.order_amount + self.processing_fee
    def authenticate_payment(self):
        return "Authentication successful."
    def process_payment(self):
        return "Payment processed successful"
    def generate_receipt(self):
                print(f"""
========================================
          PAYMENT PROCESSING
========================================

Customer Name       : {self.customer}
Order ID            : {self.order_id}
Payment Method      : UPI

Order Amount        : Rs.{self.order_amount}
Processing Fee      : Rs.{self.processing_upi_fee}
Final Amount        : Rs.{self.f_amount}

Validating payment details...
{self.validate_payment()}

Authenticating payment...
{self.authenticate_payment()}

Processing payment...
{self.process_payment()}

Transaction ID      : TXN785421
Payment Status      : SUCCESS

========================================""")

class CreditCardPayment(Payment):
        
    def __init__(self, customer_name, order_id, order_amount,card_no,card_holder_name,cvv,expiry_date,processing_credit_fee):
        super().__init__(customer_name, order_id, order_amount)
        self.card_no=card_no
        self.card_holder_name=card_holder_name
        self.cvv=cvv
        self.expiry_date=expiry_date
        self.processing_credit_fee=processing_credit_fee
    def validate_payment(self):
            return("Payment details validated successfully.")
    def calculate_processing_fee(self):
        self.processing_fee = self.order_amount * self.processing_credit_fee / 100
        self.f_amount = self.order_amount + self.processing_fee
    def authenticate_payment(self):
        return("Authentication successful.")
    def process_payment(self):
        return("Payment processed successfully.")
    def generate_receipt(self):
                print(f"""
========================================
          PAYMENT PROCESSING
========================================

Customer Name       : {self.customer}
Order ID            : {self.order_id}
Payment Method      : CREDIT card

Order Amount        : Rs.{self.order_amount}
Processing Fee      : Rs.{self.processing_fee}
Final Amount        : Rs.{self.f_amount}

Validating payment details...
{self.validate_payment()}

Authenticating payment...
{self.authenticate_payment()}

Processing payment...
{self.process_payment()}

Transaction ID      : TXN785421
Payment Status      : SUCCESS

========================================""")
        
        
class DebitCardPayment(Payment):
    def __init__(self, customer_name, order_id, order_amount,debit_card_no,debit_card_holder_name,
                 debit_cvv,debit_expiry_date,debit_processing_fee):
        super().__init__(customer_name, order_id, order_amount)
        self.debit_card_no=debit_card_no
        self.debit_card_holder_name=debit_card_holder_name
        self.debit_cvv=debit_cvv
        self.debit_expiry_date=debit_expiry_date
        self.debit_processing_fee=debit_processing_fee
    def validate_payment(self):
        return("Payment details validated successfully.")
    def calculate_processing_fee(self):
        self.processing_fee = self.order_amount * self.debit_processing_fee / 100
        self.f_amount = self.order_amount + self.processing_fee
    def authenticate_payment(self):
        return("Authentication successful.")
    def process_payment(self):
        return("Payment processed successfully.")
    def generate_receipt(self):
                print(f"""
========================================
          PAYMENT PROCESSING
========================================

Customer Name       : {self.customer}
Order ID            : {self.order_id}
Payment Method      : DEBIT CARD

Order Amount        : Rs.{self.order_amount}
Processing Fee      : Rs.{self.debit_processing_fee}
Final Amount        : Rs.{self.f_amount}

Validating payment details...
{self.validate_payment()}

Authenticating payment...
{self.authenticate_payment()}

Processing payment...
{self.process_payment()}

Transaction ID      : TXN785421
Payment Status      : SUCCESS

========================================""")
class NetBankingPayment(Payment):
    def __init__(self, customer_name, order_id, order_amount,
                 bank_name, account_no,customer_id,processing_net_fee):
         super().__init__(customer_name, order_id, order_amount)
         self.bank_name=bank_name
         self.account_no=account_no
         self.customer_id=customer_id
         self.processing_net_fee=processing_net_fee
    def validate_payment(self):
        return("Payment details validated successfully.")
    def calculate_processing_fee(self):
        self.processing_fee = self.order_amount * self.processing_net_fee / 100
        self.f_amount = self.order_amount + self.processing_fee
    def authenticate_payment(self):
        return "Authentication successful."
    def process_payment(self):
        return "Payment processed successfully."
    def generate_receipt(self):
                print(f"""
========================================
          PAYMENT PROCESSING
========================================

Customer Name       : {self.customer}
Order ID            : {self.order_id}
Payment Method      : NET BANKING

Order Amount        : Rs.{self.order_amount}
Processing Fee      : Rs.{self.processing_net_fee}
Final Amount        : Rs.{self.f_amount}

Validating payment details...
{self.validate_payment()}

Authenticating payment...
{self.authenticate_payment()}

Processing payment...
{self.process_payment()}

Transaction ID      : TXN785421
Payment Status      : SUCCESS

========================================""")
class WalletPayment(Payment):
    def __init__(self, customer_name, order_id, order_amount,wallet_name,
                 mobile_no,wallet_pin,processing_wallet_fee):
        super().__init__(customer_name, order_id, order_amount)
        self.wallet_name=wallet_name
        self.mobile_no=mobile_no
        self.wallet_pin=wallet_pin
        self.processing_wallet_fee=processing_wallet_fee
    def validate_payment(self):
        return ("Payment details validated successfully.")
    def calculate_processing_fee(self):
        self.processing_fee = self.order_amount * self.processing_wallet_fee / 100
        self.f_amount = self.order_amount + self.processing_fee
    def authenticate_payment(self):
        return "Authentication successful."
    def process_payment(self):
        return "Payment processed successfully."
    def generate_receipt(self):
                print(f"""
========================================
          PAYMENT PROCESSING
========================================

Customer Name       : {self.customer}
Order ID            : {self.order_id}
Payment Method      : WALLET

Order Amount        : Rs.{self.order_amount}
Processing Fee      : Rs.{self.processing_wallet_fee}
Final Amount        : Rs.{self.f_amount}

Validating payment details...
{self.validate_payment()}

Authenticating payment...
{self.authenticate_payment()}

Processing payment...
{self.process_payment()}

Transaction ID      : TXN785421
Payment Status      : SUCCESS

========================================""")

while True:
    print(f"""========================================
       ONLINE PAYMENT SYSTEM
========================================
1. Make Payment
2. View Payment Details
3. Exit""")
    a=int(input("enter your choice"))
    match a:
        case 1:
            print(f"""------------------------------------------------------------
OPTION 1: MAKE PAYMENT
------------------------------------------------------------""")
            customer_name=input("enter the customer name")
            order_id=input("enter the order id")
            order_amount=int(input("enter the order amount "))
            print(f"""Select Payment Method
1. UPI
2. Credit Card
3. Debit Card
4. Net Banking
5. Wall""")
            b=int(input("enter your choice"))
            match b:
                case 1:
                    print(f"""------------------------------------------------------------
UPI:
------------------------------------------------------------""")
                    upi_id=input("enter the UPI id")
                    upi_pin=input("enter the UPIpin ")
                    processing_upi_fee=0
                    payment= UPIPayment(customer_name,order_id, order_amount,upi_id,upi_pin,processing_upi_fee)
                    payment.calculate_processing_fee()
                case 2:
                    print(f"""-----------------------------------------------------------
CREDIT CARD:
------------------------------------------------------------""")
                    card_no=int(input("enter the card number"))
                    card_holder_name=input("enter the card holder name")
                    cvv=int(input("enter the cvv"))
                    expiry_date=input("enter the expiry date")
                    processing_credit_fee= 2
                    payment=CreditCardPayment(customer_name,order_id, order_amount,card_no,card_holder_name,cvv,expiry_date,processing_credit_fee)
                    payment.calculate_processing_fee()
                case 3:
                    print(f"""------------------------------------------------------------
DEBIT CARD:
------------------------------------------------------------""")
                    debit_card_no=input("enter the card number")
                    debit_card_holder_name=input("enter the card holder name")
                    debit_cvv=input("enter the cvv")
                    debit_expiry_date=input("enter the expiry date")
                    debit_processing_fee= 1
                    payment=DebitCardPayment(customer_name,order_id, order_amount,debit_card_no,debit_card_holder_name,debit_cvv,debit_expiry_date,debit_processing_fee)
                    payment.calculate_processing_fee()
                case 4:
                    print(f"""------------------------------------------------------------
NET BANKING:
------------------------------------------------------------""")
                    bank_name=input("enter the bank name")
                    account_no=input("enter the account no")
                    customer_id=input("enter the customer id")
                    processing_net_fee=0.5

                    payment=NetBankingPayment(customer_name,order_id, order_amount,bank_name,account_no,customer_id,processing_net_fee)
                    payment.calculate_processing_fee()

                case 5:
                    print(f"""------------------------------------------------------------
WALLET:
------------------------------------------------------------""")
                    wallet_name=input("enter wallet name")
                    mobile_no=input("enter the mobile no")
                    wallet_pin=input("enter the wallet pin")
                    processing_wallet_fee=1.5
                    payment=WalletPayment(customer_name,order_id, order_amount,wallet_name,mobile_no,wallet_pin,processing_wallet_fee)
                    payment.calculate_processing_fee()
                case _:
                      print("invalid case")
        case 2:
            o_id = input("Enter Order ID:")
            if order_id == o_id:
                payment.generate_receipt()
            else: 
                print("Payment record not found.")
        case 3:
              print("thankyou for using online payment system")
              break
        case _:
              print("invalid case")