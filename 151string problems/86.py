#86Print all permutations of a string without repetition. S = "ab" "ab", "ba"
s="abc"
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        print((s[i:j]))
        