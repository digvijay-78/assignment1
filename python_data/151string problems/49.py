#49Replace all consonants with '*' (Example suggests replacing non-vowels). 
# S = "apple" "a***e" (or similar output depending on implementation)
a = input("Enter the string: ")
r= ""
for i in a:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="O" or i== "U" or i=="I":
        r+=i
    else:
        r+="*"
print(r) 