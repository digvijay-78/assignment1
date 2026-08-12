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
#a=int(input("N="))
#pas=[]
#print("enter array elements:")
#for i in range(a):
#    pas.append(input())
#print()
pas=["abc","de","fg","ad"]
c=0
re=[]
for i in range(len(pas)) :
      s=pas[i]
      for j in range(len(pas)):
           re.append(s+pas[j])
for i in re:
     if re.count(i)==1:
          c+=1
print(c)
        