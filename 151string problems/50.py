#50Remove all digits. S = "a1b2c3" "abc"
s="a1b2c3"
z="" 
for i in s:
    if not ("0"<=i<="9"):
        z+=i
print(z)