#59Rotate characters right by 3 positions. S = "abcde" "cdeab"
s=input("enter the char")
k=int(input("enter the no of rotation"))
res=""
for i in range(len(s)):
    res+=s[k:len(s)]
    res+=s[:k]
    break
print(res)





s = input("Enter the string: ")
k = int(input("Enter the no of rotation: "))

k = k % len(s)
res = s[k:] + s[:k]

print(res)