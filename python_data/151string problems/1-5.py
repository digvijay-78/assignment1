#1)Find the length of a string.

s = input("programming")
print(len(s))


#2)Copy one string to another.
S1 =input( "source")
s2=S1
print(s2)


#3)Concatenate two strings.
#S1 = "Hello", S2 = "World"
s=input("")
s2=input("")
z=s+s2
print(z)



#4Compare two strings (case-sensitive). S1 = "Test", S2 = "test" Not Equal (or non-zero value)
S1 = "Test"
S2 = "test"

if S1 == S2:
    print("Equal")
else:
    print("Not Equal")



#5Compare two strings ignoring case. S1 = "Test", S2 = "test" Equal (or 0)
s1 = "Test"
s2 = "test"

if s1.lower() == s2.lower():
    print("Equal")
    print(0)
else:
    print("Not Equal")




