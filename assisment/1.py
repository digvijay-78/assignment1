"""Problem 1: Check Whether a String Is a Valid Shuffle of Two Strings(3)

Write a program to check whether a given string result is a valid shuffle of two strings str1 and str2.

A string is a valid shuffle if all characters of both input strings appear in the result in the same relative order as in their original strings.

Input Format:
- First line: String str1
- Second line: String str2
- Third line: String result

Output Format:

Print Valid Shuffle if the result is a valid shuffle; otherwise, print Invalid Shuffle.
Sample Test Cases
Test Case Input (str1, str2, result) Expected Output
1 ab, cd, acbd Valid Shuffle
2 ab, cd, abcd Valid Shuffle
3 ab, cd, adcb Invalid Shuffle
4 abc, def, adbcef Valid Shuffle
5 abc, def, abcdefg Invalid Shuffle
6 aab, axy, aaxaby Valid Shuffle
7 abc, def, abdecf Valid Shuffle
8 abc, def, abdfec Invalid Shuffle
9 ``, abc, abc Valid Shuffle
10 abc, def, abcdef Valid Shuffle

Additional Constraints
- The result must contain exactly all characters from both input strings.
- The relative order of characters in each original string must be preserved.
- Duplicate characters must be handled correctly.
- The solution should work for strings of different lengths.
-"""

str1=input("enter the first string")
str2=input("enter the 2 string")
res=input("enter the result you want")
m=(str1+str2).strip()

for i in range(len(res)):
    if m[i]!=res[i]:
        print("Invalid Shuffle")
        break
else:
    print("Valid Shuffle")    