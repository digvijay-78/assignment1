#29Remove occurrences of a word. S = "a test b test c", Word = "test", Remove All "a b c"
s=input("enter the string").split()
a="test"
ans=""
for i in s:
    if i!=a:
        ans+=i+" "
print(ans)

'''
