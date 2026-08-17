#48Remove all vowels. S = "aeiou XYZ" " XYZ"
s=input("aeiou XYZ www")
z=""
for i in s:
    if i not in "aeiou" :
        z+=i
print(z)

#print(z.strip())

a = input("Enter the string: ")
result = ""
for i in a:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="O" or i== "U" or i=="I":
        pass
    else:
        result+=i
print(result) 