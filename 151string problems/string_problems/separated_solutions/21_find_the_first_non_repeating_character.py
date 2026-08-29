#21Find the first non-repeating character. S = "aabbcde" c'
s = "aabbcde"
for i in s:
    if s.count(i)==1:
        print(i)
        break
