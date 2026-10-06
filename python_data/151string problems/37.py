#37Reverse each word. S = "cat dog" "tac god"
s="cat dog"
b=s[::-1]
a=b.split()
c=a[::-1]
print(" ".join(c))


a = input("Enter the String: ").split()
result=""
for i in a:
    result+= i[::-1]+" "
print("resultant: ", result)