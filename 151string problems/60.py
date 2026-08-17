#60Append two strings but remove adjacent duplicates. 
# S1="miss", S2="issippi" "misisipi"

S1="miss"
S2="issippi"
#s1re=""
#s2re=""
#for i in range(len(S1)):
#    if i>0 and S1[i-1]==S1[i]:
#        pass
#    else:
#        s1re+=S1[i]
#for i in range(len(S2)):
#    if i>0 and S2[i-1]==S2[i]:
#        pass
#    else:
#        s2re+=S2[i] 
#print(s1re+s2re)
#
#


s = S1 + S2
result = ""

for i in range(len(s)):
    if i == 0 or s[i] != s[i-1]:
        result += s[i]

print(result)