#23Print all characters that occur exactly twice. S = "aabbcdee" b', 'e'
s= "aabbcdee"
z=""
for i in s:
    if s.count(i)==2:
        if i not in  z :
            z+=i+" "
print(z)
