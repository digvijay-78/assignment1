#52Remove all special characters. S = "a!@b#c" "abc"
s="a!@b#C"
special = "!@#$%^&*()-_=+[]{}\\|;:'\",.<>/?~`"
z=""
for i in s:
    if i not in special:
        z+=i
print(z)