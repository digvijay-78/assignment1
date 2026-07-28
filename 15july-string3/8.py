'''
QNo 8:-- SMART TEXT PROCESSING SYSTEM
A software company is developing a Smart Text Processing System for handling user messages. Different users require different text transformations. To avoid creating separate applications, the company wants a menu-driven program where users can select operations according to their requirements.
The system should continue executing until the user selects Exit.
====================================================== MENU
===== Smart Text Processing System =====
    1. Reverse Complete String
    2. Reverse Every Word
    3. Reverse Word Order
    4. Exit
====================================================== Choice 1 :
Conditions: - Reverse the complete string - Ignore extra spaces - Keep special characters (@,#,$,%) in their original positions - Do not use built-in reverse functions
Example: Input: ja@va#py
Output: yp@av#aj
Test Case 1: ab@cd#ef Output: fe@dc#ba
Test Case 2: py@th#on Output: no@ht#yp
Test Case 3: java@proOutput : orpa@vaj
====================================================== Choice 2 :
Conditions: - Reverse every word separately - Words containing digits should not be reversed - Ignore extra spaces between words - First letter of each reversed word should become uppercase
Example: Input: java is easy123 programming
Output: Avaj Si easy123 Gnimmargorp
Test Case 1: python full stack22 developer Output: Nohtyp Lluf stack22 Repoleved
Test Case 2: hello java99 world Output: Olleh java99 Dlrow
====================================================== Choice 3 :
Conditions: - Reverse order of words - Remove duplicate words - Ignore case while checking duplicates - Keep only first occurrence
Example: Input: Java python Java react Python
Output: React Python Java
Test Case 1: HTML CSS HTML Java CSS Output: Java CSS HTML
Test Case 2: Python React Java Python React Output: Java React Python
====================================================== Choice 4
Program Closed Successfully
'''

while True:
     print("\n1.  Reverse Complete String")
     print("2.  Reverse Every Word")
     print("3.  Reverse Word Order")
     print("4.  Exit")
     ch = int(input("Enter your choice: "))
     match ch:
          case 1:
                    ip = input("    Input : ") .lower()
                    ch = ""
                    sp = ""
                    for i in ip:
                         if i.isalpha():
                              ch+=i
                         elif i == "!" or i == "@"  or i == "$" or i == "#" or i == "%" or i == "^" or i == "&":
                              sp+=i
                         else:
                              continue
                    rev = ch[::-1]
                    result = ""
                    j = 0
                    k = 0
                    while k<len(ip):
                         if "a" <=ip[k] <= "z":
                              result +=rev[j]
                              j+=1
                         else:
                              result +=ip[k]
                         k+=1
                    print(result)