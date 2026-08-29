#36Reverse order of words. S = "one two three" "three two one"

s= "one two three"
a=s.split()
b=a[::-1]
print(" ".join(b))

word=s.split()
for i in range(len(word)-1,-1,-1):
    print("Reversed Order ->",word[i], end = " ")
