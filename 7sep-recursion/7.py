"""3.
Cricket Tournament – Highest Run Scorer
A cricket academy wants to reward the player who scored the highest number of runs in a tournament.
Write a Python program to identify the highest run scorer using reduce() and a lambda expression.

Input
players = [
    ("Virat", 78),
    ("Rohit", 102),
    ("Gill", 89),
    ("KL Rahul", 65),
    ("Iyer", 91)
]
Expected Output
Highest Run Scorer: Rohit"""
from functools import reduce
n=int(input("enter the payers : "))
m=[]
for i in range(n):
    name = input(f"enter the name {i+1}: ")
    age = int(input(f"enter the score {i+1}: "))
    m.append((name, age))
result=reduce(lambda x,y:x if x[1]>y[1] else y,m)
print("the highest run scorer :",result[0])