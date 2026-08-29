#31Remove duplicate words. S = "the cat and the dog" "the cat and dog"
s= "the cat and the dog"
a=s.split()
z=""
for i in range(len(a)):
    if a[i] not in z:
        z=z+a[i]+" "

print(z)
