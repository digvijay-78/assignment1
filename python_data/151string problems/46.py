#46Check if a substring appears at both the start and end. S = "abcabca", Sub="abca" TRUE
s="abcabca"
sub="abca"
if s[:len(sub)]==sub and s[len(s)-len(sub):]==sub:
    print("True")
else:
    print(False)
    