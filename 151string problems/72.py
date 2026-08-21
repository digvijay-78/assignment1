#72Print all substrings of length n. S = "abc", n = 2 "ab, bc"
a="abc"
n=2
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        if len(a[i:j])==n:
            print(a[i:j])