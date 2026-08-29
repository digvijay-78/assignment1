#22Find the last repeating character. S = "abracadabra" r'
s = "abracadabra"
z=""
for i in s:
    if s.count(i)==2:
        z=i
print(z)
