#42Check if two strings are equal without equals(). S1 = "abc", S2 = "abc" TRUE
a="abc"
s="abc"
if len(a)!=len(s):
    print("FALSE")
elif (a<=s) and (s<=a):
    print("True")
#internally equal use hora hai 

a = "abc"
s = "abc"

if len(a) != len(s):
    print("FALSE")
else:
    for i in range(len(a)):
        if a[i] != s[i]:
            print("FALSE")
            break
    else:
        print("TRUE")