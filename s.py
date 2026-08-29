'''s=input("enter the string")
i=len(s)-1
while i>=0:
	print(s[i])
	i=i-1
    
s=input("enter the string")
n=len(s)
i=-1
while i>=-n:
	print(s[i])
	i=i-1

s=input("enter the string")
sub=input("enter the sub string")
if sub in s:
    print("found")
else:    
	print("not found")
    

s=input("enter the string")
#print(s.title())
#print(chr(ord("a")-32))
result=" "
i=0
while i<len(s):
    if i==0 or s[i-1]==" ":
		if s[i]>="a" and s[i]<="z":
			result=result+chr(ord(s[i])-32)
		else:
			result=result+s[i]
    else:
		result=result+s[i]
	i=i+1
print(result)


s1=input("enter the string")
s2=input("enter the string")
if len(s1)==len(s2):
    if sorted(s1)==sorted(s2):
        print("anagram")
    else:
        print("not anagram")
else:
    print("not anagram")

s1=input("enter the string")
s2=input("enter the string")
if len(s1)!=len(s2):
    print("not anagram")
else:
    x=1
    for ch in s1:
        if s1.count(ch)!=s2.count(ch):
            x=0
            break
    if x==1:
        print("anagram")
    else:
        print("not anagram")

s1=input("enter the string")
ch=input("enter the string")
count=0
for i in s1:
    if i==ch:
        count+=1
print(count)


s1=input("enter the string")
s2=input("enter the string")
if len(s1)!=len(s2):
    print("not anagram")
else:
    visited=[]
    x=1
    i=0
    while i<len(s1):
        ch=s1[i]
        if ch not in visited:
            c1=0
            c2=0
            j=0
            while j<len(s1):
                if s1[j]==ch:
                    c1=c1+1
                j=j+1
            j=0
            while j<len(s1):
                if s2[j]==ch:
                    c2=c2+1
                j=j+1
            if c1!=c2:
                x=0
                print("not anagram")
                break
            visited.append(ch)
        i=i+1
    if x==1:
        print("anagram")
    else:
        print("not")        
'''

# s1=input("enter the string")
# s2=input("enter the string")
# if len(s1)!=len(s2):
#     print("not anagram")
# else:
#     visited=[]
#     x=1
#     i=0
#     while i<len(s1):
#         ch=s1[i]
#         c1=0
#         c2=0
#         j=0
#         while j<len(s1):
#             if s1[j]==ch:
#                 c1=c1+1
#             j=j+1
#         j=0
#         while j<len(s1):
#             if s2[j]==ch:
#                 c2=c2+1
#             j=j+1
#         if c1!=c2:
#             x=0
#             print("not anagram")
#             break
#         i=i+1
#     if x==1:
#         print("anagram")
#     else:
#         print("not")      

