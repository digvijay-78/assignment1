#94Find the smallest window containing all characters of another string. 
# S1 = "ADOBECODEBANC", S2 = "ABC" "BANC"

s1 = "ADOBECODEBANC"
s2 = "ABC"
l=0
r=0
s=""
c=""
while r<len(s1):
    s+=s1[r]
    if s1[l] in s2:
        c+=s1[l]