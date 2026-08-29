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
