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
