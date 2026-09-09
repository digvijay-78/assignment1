#94Find the smallest window containing all characters of another string. 
# S1 = "ADOBECODEBANC", S2 = "ABC" "BANC"

s1 = "ADOBECODEBANC"
s2 = "ABC"
l=0
r=0
max=0
for i in range(len(s1)):
    for j in range(i+1,len(s1)+1):
        if j< len(s2) and s2[j] in s1[i:j]:
            print(s1[i:j])