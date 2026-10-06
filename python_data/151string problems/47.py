#47Check for substring using concatenation trick.
#  S1="CDAB", S2="ABCD" True (S1 is in S2+S2)
s="CDAB"
s2="ABCD"
if s in s2+s2:
    print(True)
else:
    print(False)