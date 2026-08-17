#45Check whether a string starts/ends with another string. 
# S = "apple pie", Prefix = "apple", Suffix = "pie" Start: True, End: True
s= "apple pie"
p= "apple"
l="pie"
if s.startswith(p) and s.endswith(l):
    print("TRUE")
else:
    print("false")


if s[:len(p)] == p and s[len(s)-len(l):] == l:
    print("TRUE")
else:
    print("false")