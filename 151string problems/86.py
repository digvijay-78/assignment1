#86Print all permutations of a string without repetition. S = "ab" "ab", "ba"
s="abc"
for i in range(len(s)):
    for j in range(len(s)):
        for k in range(len(s)):
            if i!=j and j!=k and i!=k:
                print(s[i]+s[j]+s[k])
        