#44Check if two strings are anagrams. S1 = "listen", S2 = "silent" TRUE
s="listen"
s1="silent"
if len(s)!=len(s1):
    print("false")
else:
    for i in range(len(s)):
        if s.count(s[i]) != s1.count(s[i]):
            print("false")
            break
    else:
        print("true")