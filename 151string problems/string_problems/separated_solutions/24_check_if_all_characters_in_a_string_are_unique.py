#24Check if all characters in a string are unique. S1 = "abc", S2 = "abca" S1: True, S2: False

s= "abc"
z=""
for i in s:
    if s.count(i)==2:
        print(bool(0))
        break
else:
    print(bool(1))
