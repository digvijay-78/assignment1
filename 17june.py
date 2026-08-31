
# # problem 2:-   3 marks
# # Matrix Multiplication
# # Write a Python program to read two matrices from the user and perform matrix multiplication.
# # Before multiplying the matrices, check whether multiplication is possible. Matrix multiplication is possible only if
# # the number of columns in the first matrix is equal to the number of rows in the second matrix.
# # Requirements
# # Read the number of rows and columns for the first matrix.
# # Read all the elements of the first matrix from the user.
# # Read the number of rows and columns for the second matrix.
# # Read all the elements of the second matrix from the user.
# # Check whether matrix multiplication is possible.
# # If possible, multiply the matrices using nested loops.
# # Display the resulting matrix.
# # If multiplication is not possible, display:
# # Matrix multiplication is not possible.


# rows1=int(input("enter the no of rows "))
# col1=int(input("enter the no of col "))
# m=[]
# for i in range( rows1):
#     row=[]
#     for j in range(col1):
#         row.append(int(input()))
#     m.append(row)


# r2=int(input("enter rows for sec matrix"))
# c2=int(input("enter col for sec matrix"))
# print("enter elements for sec matrix")
# B=[]
# for i in range(r2):
#     row=[]
#     for j in range(c2):
#         row.append(int(input()))
#     B.append(row)
# res=[]
# if col1==r2:
#     for i in range(rows1):
#         row=[]
#         for j in range(c2):
#             row.append(0)
#         res.append(row)
#     for i in range(rows1):
#         for j in range(c2):
#             for k in range(col1):
#                 res[i][j]=res[i][j]+m[i][k]*B[k][j]
#     print("result is ")
#     print(*res)
# else:
#     print("Matrix multiplication is not possible")

"""1. 3 marks
 Check if Two Strings Differ by Exactly One Character**
A typing tutor application compares a student's typed word with the expected word.
The application should determine whether the typed word differs from the expected word by exactly one character.
 A difference can occur in one of the following ways:
* One character is inserted
* One character is deleted
* One character is replaced
Write a Python program to check whether two given strings differ by exactly one character. If they do, 
display *True; otherwise, display **False*.
*Input Format:*
* The first line contains the first string S1.
* The second line contains the second string S2.
*Output Format:*
* Print True if the two strings differ by exactly one character.
* Otherwise, print False.
*Constraints:*
* The strings contain only lowercase English alphabets.
* 1 ≤ length of string ≤ 100
*Sample Input 1:*
pale
ple
*Sample Output 1:*
True
*Explanation:*
The strings "pale" and "ple" differ by exactly one character because removing 'a' from "pale" results in "ple".
*Sample Input 2:*
pale
bale
*Sample Output 2:*
True
*Explanation:*
The strings differ by exactly one character because 'p' in "pale" is replaced by 'b' in "bale".
*Sample Input 3:*
pale
pales
*Sample Output 3:*
True
*Explanation:*
The strings differ by exactly one character because 's' is inserted at the end of "pale".
*Sample Input 4:*
pale
pale
*Sample Output 4:*
False
*Explanation:*
The strings are identical and do not differ by any character.
*Sample Input 5:*
pale
bake
*Sample Output 5:*
False
*Explanation:*
More than one character change is required to convert "pale" into "bake"."""


# s = input("")
# s1 = input("")
# i = 0
# j = 0
# c = 0
# while i < len(s) and j < len(s1):
#     if s[i] != s1[j]:
#         c += 1
#         if len(s) > len(s1):
#             i += 1
#         elif len(s) < len(s1):
#             j += 1
#         else:
#             i += 1
#             j += 1
#     else:
#         i += 1
#         j += 1
# if i < len(s) or j < len(s1):
#     c += 1
# if c == 1:
#     print(True)
# else:
#     print(False)


"""
2.   3.5 marks
A cricket academy wants to analyze player performance. Each player's information is stored as a tuple.
Tuple Format:
(player_id, player_name, runs_scored)
Requirements:
Read N player records from the user and store them as tuples in a list.
Display all player records.
Find and display the player who scored the highest runs.
Find and display the player who scored the lowest runs.
Calculate and display the total runs scored by all players.
Calculate and display the average runs scored.
Display players who scored more than 50 runs.
Test Case:
Input:
Enter number of players: 5
101 Virat 82
102 Rohit 45
103 Gill 120
104 Hardik 38
105 SKY 76
Expected Output:
All Players:
(101, 'Virat', 82)
(102, 'Rohit', 45)
(103, 'Gill', 120)
(104, 'Hardik', 38)
(105, 'SKY', 76)
Highest Scorer:
(103, 'Gill', 120)
Lowest Scorer:
(104, 'Hardik', 38)
Total Runs:
361
Average Runs:
72.2
Players Scoring More Than 50 Runs:
(101, 'Virat', 82)
(103, 'Gill', 120)
(105, 'SKY', 76)"""

# from collections import namedtuple

# player=namedtuple("player",["player_id","player_name","runs"])

# n=int(input("enter no of players =>"))
# p=[]

# for i in range(n):
#     print("enter details")
#     id=int(input("enter player.id>"))
#     name=input("enter name")
#     runs=int(input("enter runs"))
#     s=player(id,name,runs)
#     p.append(s)

# print("details")
# for x in p:
#     print(x.player_id,x.player_name,x.runs)

# c=p[0]
# for y in p:
#     if y.runs>c.runs:
#         c=y
# print("Highest Scorer:")
# print(c.player_id,c.player_name,c.runs)

# d=p[0]
# for y in p:
#     if y.runs<d.runs:
#         d=y
# print("Lowest Scorer:")
# print(d.player_id,d.player_name,d.runs)

# m=0
# for k in p:
#     m=m+k.runs

# print("Total Runs:")
# print(m)

# avg=m/n
# print("Average Runs:")
# print(avg)

# print("Players Scoring More Than 50 Runs:")
# for x in p:
#     if x.runs>50:
#         print(x.player_id,x.player_name,x.runs)




"""3. 3.5 marks
Secure Password Analysis
A cybersecurity team wants to identify pairs of passwords having no common characters.
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
("de","fg")"""

n=["abc", "de", "fg", "ad"] 
c=0
for i in range(len(n)):
    for j in range(i+1,len(n)):
        s=n[i]+n[j]
        x=0

        for k in s:
            if s.count(k)>1:
                 x=1
                 break
        if x==0:
            print(n[i],n[j])
            c+=1    
print(c)