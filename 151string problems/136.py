#136Check if two strings are one edit distance apart. 
# S1 = "pale", S2 = "ple" TRUE
s="pale"
s1="ple"

r=0
l=0
mis=0

while l<max(len(s),len(s1)):
    if abs(len(s)-len(s1))>=2:
        print(False)
        break
    elif len(s)==len(s1):
        if s[l]!=s1[r]:
            mis+=1
        l+=1
        r+=1
    else:
            if s1[r] == s[l]:
                l += 1
                r += 1
            else:
                mis += 1

                if len(s) > len(s1):
                    l += 1
                else:
                    r += 1   
if mis==1:
    print(True)
else:
    print(False)