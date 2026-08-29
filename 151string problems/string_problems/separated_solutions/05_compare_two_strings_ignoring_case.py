#5Compare two strings ignoring case. S1 = "Test", S2 = "test" Equal (or 0)
s1 = "Test"
s2 = "test"

if s1.lower() == s2.lower():
    print("Equal")
    print(0)
else:
    print("Not Equal")
