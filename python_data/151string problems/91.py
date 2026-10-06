#91Check if two strings are interleaving of another string. 
# S1 = "aab", S2 = "axy", S3 = "aaxaby" TRUE
s="aab"
s2="axy"
s3="aaxaby"
r=1
if len(s3)!=len(s)+len(s2):
    r=0
else:
    i=0
    j=0
    for k in range(len(s3)):
        if i<len(s) and s3[k]==s[i]:
            i+=1
        elif j<len(s2) and s3[k]==s2[j]:
            j+=1
        else:
            r=0
            break
    if i!=len(s) or j!=len(s2):
        r=0
if r==1:
    print("true")
else:
    print("false")