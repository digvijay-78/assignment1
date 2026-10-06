#51Extract only digits. S = "a1b2c3" "123"
s="a1b2c3"
z="" 
for i in s:
    if ("0"<= i <="9"):
        z+=i
print(z)