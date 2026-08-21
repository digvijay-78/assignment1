#71Print all substrings. S = "abc" "a, b, c, ab, bc, abc"
a="abc"
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        print(a[i:j],end=" ")