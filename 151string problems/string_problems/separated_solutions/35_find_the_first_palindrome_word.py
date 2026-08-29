#35Find the first palindrome word. S = "this madam is here" "madam"

s="this madam is here"
a=s.split()
for i in a:
    if i==i[::-1]:
        print("first palindrome no is ",i)
        break
