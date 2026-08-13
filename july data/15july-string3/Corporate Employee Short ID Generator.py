'''2.  Corporate Employee Short ID Generator

A multinational company wants to automatically generate short IDs for
employees while creating official email accounts. The system should take
the employee’s full name and create an ID using the first character of
each word.

Conditions: - Take first character of every word - Convert all
characters to uppercase

Input: Enter employee name: ajay singh thakur

Output: Employee Short ID: AST'''
s = input("Enter the string: ")
result = ""
i = 0

while i < len(s):
    if i == 0 or s[i-1] == " ":
        if "a" <= s[i] <= "z":
            print(chr(ord(s[i]) - 32), end=" ")
        elif "A" <= s[i] <= "Z":
            print(s[i], end=" ")
        else:
            print("No digit")
            break
    i += 1