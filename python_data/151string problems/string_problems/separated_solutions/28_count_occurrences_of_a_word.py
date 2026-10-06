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
