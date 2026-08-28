#87Print all permutations of a string with repetition. S = "aab" "aab", "aba", "baa"
s="aab"
for i in range(len(s)):
    for j in range(len(s)):
        for k in range(len(s)):
                print(s[i]+s[j]+s[k])




s = "aab"
z = []
for i in range(len(s)):
    for j in range(len(s)):
        for k in range(len(s)):
            if i != j and j != k and i != k:
                x = s[i] + s[j] + s[k]
                if x not in z:
                    z.append(x)
for x in z:
    print(x)