#39Search all occurrences of a character. S = "banana", Char='a' 1, 3, 5 (indices)
s="banana"
ch="a"
z=" "
for i in range(len(s)):
    if ch==s[i]:
        z+=str(i)+" "
print(z)

a = input("Enter the string: ")
b = input("Enter the character to find: ")
for i in range(len(a)):
    if b==a[i]:
        print(i, end =" ")