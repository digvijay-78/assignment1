"""n=input("=")
result=""
i=0
while i<len(n):
    ch=n[i]
    if (ch>="A" and ch<="Z")or (ch>="a" and ch<="z")or(ch>="0" and ch<="9"):
        result=result+ch
    i=i+1
print("result without special char =",result)
"""
'''
"first non repeated char"
n=input("=")
c=0
for i in n:
    if n.count(i)==1:
        print(i)
        break

s=input("=")
found=0
i=0
while i<len(s):
    count=0
    j=0
    while j<len(s):
        if s[i]==s[j]:
            count=count+1
        j=j+1
    if count==1:
        print(s[i])
        found=1
        break
    i=i+1
if found==0:
    print("not")

s=input("=").split()
w=s[0]
for i in range(len(s)):
    if s[i]<w:
        w=s[i]

print(w)


"""unique char"""
n=input("=")
c=0

for i in n:
    if n.count(i)==1:
        c=c+1
print(c)

s=input("=")
unique=0
i=0
while i<len(s):
    count=0
    j=0
    while j<len(s):
        if s[i]==s[j]:
            count=count+1
        j=j+1
    if count==1:
        print("unique",s[i])
        unique+=1
        
    i=i+1
print(unique)

'''
"""occurance of a word
programmingisgraming=print(gram)"""
# a=input("=")
# b=input("=")
# 
# count=a.count(b)
# print(count)

s=input("=")
word=input("=")
c=0
i=0
while i<=len(s)-len(word):
    j=0
    match=1
    while j<len(word):
        if s[i+j]!=word[j]:
            match=0
            break
        j=j+1
    if match==1:
        c=c+1
    i=i+1
print(c)





