'''3.MATRIX PERFORMANCE EVALUATION SYSTEM
A company records the monthly performance scores of employees in a matrix format.
Each row represents an employee and each column represents a month.
The HR department wants a menu-driven application to analyze employee performance.
Menu
1. Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit
Requirements
Choice 1 – Find Employee with Highest Total Score
Calculate the sum of each row.
Display the employee number having the highest total score.
Choice 2 – Find Month with Lowest Average Score
Calculate the average of each column.
Display the month having the lowest average score.
Choice 3 – Display Employee-wise Maximum Score
Find and display the maximum value present in each row.
Sample Input
10 20 30
40 50 60
25 35 45
Output
Employee 2 has Highest Total Score = 150
Month 1 Average = 25
Month 2 Average = 35
Month 3 Average = 45

Employee 1 Max Score = 30
Employee 2 Max Score = 60
Employee 3 Max Score = 45'''


print("WELCOME to MATRIX PERFORMANCE EVALUATION SYSTEM")
while True:
    print("-"*32)
    print("MENU")
    print('''1. Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit''')
    a = int(input("ENTER YOUR CHOICE"))

    match a:
        case 1:
            a=[[10,20,30],[40,50,60],[25,35,45]]
            s=0
            e=0
            for i in range(len(a)):
                m=0
                for j in a[i]:
                    m=m+j
                if s<m:
                        s=m
                        e=i+1
            print("Employee", e, "has Highest Total Score =", s)
        case 2:
            a=[[10,20,30],[40,50,60],[25,35,45]]
            s=0
            for i in range(len(a)):
             for j in a[i]:
                    s=s+j
             v=s/len(a[i])
             print("Row", i+1, "Average =", v)
        case 3:
            a=[[10,20,30],[40,50,60],[25,35,45]]
            for i in range(len(a)):
                ma=a[i][0]
                for j in a[i]:
                    if ma<j:
                        ma=j
                print("Employee",i+1,"Max Score = ",ma)  

        case 4:
            print("Thank You")
            break               