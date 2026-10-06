#43Check if two strings are rotations of each other. S1 = "abcde", S2 = "cdeab" TRUE
s="abcde"
s1="cdeab"
if len(s)!=len(s1):
    print("false")
else:
    for i in range(len(s)):
        if s[i] not in s1:
            print("false")
            break
    else:
        print("true")
#occurance check krra hai (sir ka output chal jaayega)

if len(s)!=len(s1):
    print("false")
elif s1 in s + s:
    print("true")
else:
    print("false")
