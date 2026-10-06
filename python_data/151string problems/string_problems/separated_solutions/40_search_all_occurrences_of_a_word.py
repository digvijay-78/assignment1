#40Search all occurrences of a word. S = "a b a b", Word='b' 2, 6 (start indices)
s=input("enter the sentence").split()
a=input("enter the word")
for i in range(len(s)):
    if a==s[i]:
         print(i, end =" ")
