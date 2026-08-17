#33Find the longest word. S = "find the longest word" "longest"

s="find the longest word"
c=s.split()
co=c[0]
for i in c:
    if len(i)>len(co):
        co=i
print("longest Word :",co)

#34Find the shortest word. S = "find the shortest word" "the"
s="find the longest word"
c=s.split()
co=c[0]
for i in c:
    if len(i)<len(co):
        co=i
print("shortest",co)

#35Find the first palindrome word. S = "this madam is here" "madam"

s="this madam is here"
a=s.split()
for i in a:
    if i==i[::-1]:
        print("first palindrome no is ",i)
        break