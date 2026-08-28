#88Rearrange a string so that identical characters are at least d distance apart. 
# S = "aaabc", d = 2 "abaca" ,S = "aabbc" "abcab"
s=input("enter the string ")
d=int(input("enter the string"))
rep=""
non=""
res=""
for string in range(len(s)):
    if s.count(s[string])>1:
        rep+=s[string]
    else:
        non+=s[string]
r=0
n=0
for i in range(len(s)):
    if i%d==0:
        res+=rep[r]
        r+=1
    elif i%d !=0:
        res+=non[n]
        n+=1
print(res)









s = input("Enter the string: ")
d = int(input("Enter the distance: "))

res = ""
used = ""

for i in range(len(s)):

    # har position par aisa character dhundo
    for j in range(len(s)):

        ch = s[j]

        # character pehle use nahi hua ya uski frequency baaki hai
        if ch not in used:

            # character ko result mein add karo
            res += ch
            used += ch

            # same character ko d distance ke baad add karo
            for k in range(d - 1):
                pass

            break

print(res)