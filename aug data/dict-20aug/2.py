# """2.
# Secure Password Analysis
# A cybersecurity team wants to identify pairs of passwords having no common 
# characters.
# Problem Statement:
# Given N strings, count the number of pairs that do not share any common character.
# Example:
# Input
# N = 4
# passwords[] = {"abc", "de", "fg", "ad"}
# Output
# 3
# Explanation
# ("abc","de")
# ("abc","fg")
# ("de","fg")"""

# pas=["abc", "de", "fg", "ad"]
# n=4
# c=0
# for i in range(n):
#     for j in range(i+1,len(pas)):
#         m=0
#         for k in pas[i]:
#             if k in pas[j]:
#                 m=1
#                 break
#         if m==0:
#             c+=1
# print(c)