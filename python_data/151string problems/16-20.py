#16Count total occurrences of a character. S = "programming", Char = 'g' 2
'''a=input("enter the chr")
s=input("enter the chr")
c=0
for i in range(len(a)):
    if a[i]==s:
        c+=1
print(c)
'''

#17Remove occurrences of a character. S = "banana", Char = 'a', Remove All "bnn"
'''a=input("enter the chr")
s=input("enter the chr")
c=""
for i in range(len(a)):
    if a[i]!=s:
        c=c+a[i]        
print(c)'''

#18Replace occurrences of a character. S = "apple", Old='p', New='x' "axxle"
'''a=input("enter the chr")
s=input("enter the alphabet wants to remove:")
ad=input("enter the alphabet wants to add:")
c=""
for i in range(len(a)):
    if a[i]==s:
        c+=ad
    else:
        c+=a[i]  

print(c)
'''

#19Find the highest frequency character. S = "abracadabra" a'
s="abcdsesaaaqaaa"
a=""
c=0
for i in s:
    b=s.count(i)
    if b>c :
        c=b
        a=i
print(a,c)




#20Find the lowest frequency character. S = "aabbcde" c', 'd', 'e' (any one or all)
s="abcdsesaaaqaaa"
a=""
c=len(s)
for i in s:
    b=s.count(i)
    if b<c :
        c=b
        a=i
print(a,c)
