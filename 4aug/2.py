'''2.Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []
'''
n=list(map(int,input("enter the list").split()))
avg=sum(n)/len(n)
abavg=[]
rem=[]
for i in n:
    if i>avg:
        abavg.append(i)
    if i>15000:
        rem.append(i)
print(n,end="")
print("Average=",avg,end="")
print("Above average",abavg)
print("Remaining list",rem)