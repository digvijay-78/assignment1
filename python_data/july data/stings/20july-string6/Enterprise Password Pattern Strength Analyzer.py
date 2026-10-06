'''
 7. Enterprise Password Pattern Strength Analyzer

A cybersecurity company wants to validate advanced passwords.

## Conditions:

* Minimum 10 characters
* At least:

  * 1 uppercase letter
  * 1 lowercase letter
  * 1 digit
  * 1 special character
* No consecutive repeating characters
* No spaces allowed

### Input:

text
Pyth@n1234


### Output:

text
Strong Password


### Input:

text
Paaass@12


### Output:

text
Weak Password


---
'''
p=input("=")
u=0;l=0;di=0;s=0;sp=0;c=0
for i in range(len(p)):
    ch=p[i]
    if ch.isupper():
        u=1
    elif ch.islower():
        l=1
    elif ch.isdigit():
        di=1
    elif ch .isspace():
        s=1
    else:
        sp=1

    if i > 0 and p[i] == p[i - 1]:
        c = 1
if len(p)>=10 and l==1 and u==1 and s==0 and di==1 and sp==1 and c==0:
    print("valid")
else:
    print("invalid")