'''
#26Find the first occurrence of a word. S = "Test this test", Word = "test" 10 (index)0
s="Test this test"
a="test"
d=0
c=""
print(s.find(a))
for i in range(len(s)-len(a)+1):
    count=0
    for j in range(len(a)) :
        if s[i+j]==a[j]:
            count+=1

    if count == len(a):
        print(i)
        break


#27Find the last occurrence of a word. S = "Test this test", Word = "test" 15 (index)
s="Test this test"
a="test"
print(s.rfind(a))
for i in range(len(s)-len(a)+1):
    count=0
    for j in range(len(a)) :
        if s[i+j]==a[j]:
            count+=1

    if count == len(a):
        print(i)


#28Count occurrences of a word. S = "word word other word", Word = "word" 3
s = "word word other word"
a="word"
count=0
for i in range(len(s)-len(a)+1):
    c=0
    for k in range(len(a)):
        if s[i+k]==a[k]:
            c+=1
    if c==len(a):
        count+=1
print(count)

'''
#29Remove occurrences of a word. S = "a test b test c", Word = "test", Remove All "a b c"
s=input("enter the string").split()
a="test"
ans=""
for i in s:
    if i!=a:
        ans+=i+" "
print(ans)
