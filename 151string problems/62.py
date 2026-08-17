#62Count vowels and consonants. 
# S = "apple" Vowels: 2, Consonants: 3
s="apple"
v=0
c=0
for i in s:
    if i in "aeiouAEIOU":
        v+=1
    elif ("a"<=i<="z") or ("A"<=i<="Z"):
        c+=1
print("vowels",v,"consonants",c)