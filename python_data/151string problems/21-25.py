#21Find the first non-repeating character. S = "aabbcde" c'
s = "aabbcde"
for i in s:
    if s.count(i)==1:
        print(i)
        break



#22Find the last repeating character. S = "abracadabra" r'
s = "abracadabra"
z=""
for i in s:
    if s.count(i)==2:
        z=i
print(z)


#23Print all characters that occur exactly twice. S = "aabbcdee" b', 'e'
s= "aabbcdee"
z=""
for i in s:
    if s.count(i)==2:
        if i not in  z :
            z+=i+" "
print(z)



#24Check if all characters in a string are unique. S1 = "abc", S2 = "abca" S1: True, S2: False

s= "abc"
z=""
for i in s:
    if s.count(i)==2:
        print(bool(0))
        break
else:
    print(bool(1))


#25Count total words in a string. S = "This is a test" 4
s = "This is a test".split()
print(len(s))
