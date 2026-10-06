#61Count total alphabets, digits, and special characters. 
# S = "a1b!c2" Alphabets: 3, Digits: 2, Special: 1

s= "a1b!c2"
ac=0
dc=0
sc=0
for i in s:

    if ("a"<=i<="z") or ("A"<=i<="Z"):
        ac+=1
    elif "0"<=i<="9":
        dc+=1
    else:
        sc+=1

print("Alphabets:" ,ac," Digits: ",dc," Special:",sc)