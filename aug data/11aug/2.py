'''2.
Secure Password Analysis
cybersecurity team wants to identify pairs of passwords having no common characters.
Problem Statement:
Given N strings, count the number of pairs that do not share any common character.
Example:
Input
N = 4
passwords[] = {"abc", "de", "fg", "ad"}

Output

3

Explanation

("abc","de")
("abc","fg")
("de","fg")
'''
n = int(input("Enter size of list:"))

password = []
for i in range(n):
    password.append(input("Enter Elements:"))
count = 0

for i in range(n-1):
    word = password[i]
    for j in range(i+1,n):
            for k in password[j]:
                 if k in word:
                      break
            else:
                 count+=1

print(count)