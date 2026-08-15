#31Remove duplicate words. S = "the cat and the dog" "the cat and dog"
s= "the cat and the dog"
a=s.split()
z=""
for i in range(len(a)):
    if a[i] not in z:
        z=z+a[i]+" "

print(z)

#32Count frequency of each word. S = "apple banana apple" apple: 2, banana: 1

s="apple banana apple"
a=s.split()
for i in range(len(a)):
    c=0
    v=a[0]
    if v==a[i]:
        c+=1
    v=a[i]
    print(v)
    print(a[i],":",c)