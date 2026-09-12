"""4. Billing Package
Create a package named "billing".
Create module:
billing_module.py
Implement:
generate_bill()
Take:
- Patient ID
- Consultation Charges
- Medicine Cost
- Test Charges
Calculate total amount:
Total Bill = Consultation Charges + Medicine Cost + Test Charges
Display complete bill."""
def generate_bill():
    id=input("enter Patient ID")
    con=float(input("enter the Consultation Fees"))
    med=float(input("enter the medicine cost"))
    test=float(input("enter the test charges"))
    total=con+med+test
    print("Patient ID:", id) 
    print("Consultation Charges:", con) 
    print("Medicine Cost:", med) 
    print("Test Charges:", test) 
    print("Total Bill:", total)
    return total
