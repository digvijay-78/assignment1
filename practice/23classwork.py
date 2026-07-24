'''
5c32ba
final abc235
s=input("")
s1=s2=result=""
for x in s:
    if x.isalpha():
        s1=s1+x
    else:
        s2=s2+x

for x in sorted(s1):
    result=result+x

for x in sorted(s2):
    result=result+x
print("final",result)'''

'''
a3b4=aaabbbb
s = input("")
result = ""
previous = ""

for x in s:
    if x.isalpha():
        result += x
        previous = x
    else:
        result += previous * (int(x) - 1)

print("result", result)

'''
'''
a3b5=adbg
s = input("")
result = ""
previous = ""
for x in s:
    if x.isalpha():
        result += x
        previous = x
    else:
        newchar=chr(ord(previous)+int(x))
        result=result+newchar
print("final",result)
'''
'''
abcde=edcba
s=input("")
rev=""
# for i in range(len(s)-1,-1,-1):
    # rev=rev+s[i]
for x in s:
    rev=x+rev
print("reverse is ",rev)
'''
'''
ccc bbb aaa=ccc bbb aaa
s=input("=").split()
rev=""
# for i in s:
    # rev=i+" "+rev
# 
# print("result",rev)

s=s[::-1]
print(" ".join(s))
'''
'''
s=input("=").split()
for i in range(len(s)):
    w=s[i]
    rev=" "
    for j in range(len(w)-1,-1,-1):
        rev=rev+w[j]
    print(rev,end=" ")
'''
s=input("=").split()
for i in s:
    print(i[::-1], end=" ")