"""

5. Website URL Verification System

A software company is developing an automated website registration
portal. Before saving a website address, the system must verify whether
the URL follows the required company format.

Conditions: - Must start with www - Must end with .com

Input: Enter website: www.amazon.com

Output: Valid Website
"""

n = input("=")
# if " " not in n:
# if n[0:3]=="w" or n[0:3]=="W":
# if n[-1]=="m" or n[-1]=="M":
# if n[-2]=="O" or n[-1]=="o":
# if n[-3]=="m" or n[-1]=="M":
# if n[3]==".":
# if n[-4]==".":
# print("valid")
# else:
# print("invalid")

s = input("Enter the string: ").lower()
last = ""
if s[0] == "w" and s[1] == "w" and s[2] == "w" and s[3] == ".":
    last = s[len(s) - 4 :]
    if last == ".com":
        print("Valid Website")
    else:
        print("Invalid Website")
else:
    print("Invalid Website")
