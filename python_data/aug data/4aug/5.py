'''5.
 Student Grade Classification System (Python List Assignment)


A school stores student marks in a list. The system must analyze the marks and
generate a *clear performance report*
by grouping students into grade categories.



Write a Python program to:

* Iterate through the list of marks
* Assign grades based on marks:

  * *>= 90 → A*
  * *>= 75 and < 90 → B*
  * *>= 50 and < 75 → C*
  * *< 50 → Fail*
* Store each category in separate lists
* Count students in each category
* Display a *final structured report (important)*

---

## 📌 Output Format (Mandatory)

Your output must be displayed exactly in this format:


===== STUDENT GRADE REPORT =====

A Grade Students   : [list]
B Grade Students   : [list]
C Grade Students   : [list]
Fail Students      : [list]

--------------------------------
A Count   : X
B Count   : X
C Count   : X
Fail Count: X
--------------------------------

Total Students: X


---

 Input

[95, 82, 67, 45, 30]

Output


===== STUDENT GRADE REPORT =====

A Grade Students   : [95]
B Grade Students   : [82]
C Grade Students   : [67]
Fail Students      : [45, 30]

--------------------------------
A Count   : 1
B Count   : 1
C Count   : 1
Fail Count: 2
--------------------------------


'''
n=list(map(int,input("enter the list").split()))

a=[]
b=[]
c=[]
d=[]

for i in n:
    if i>=90:
        a.append(i)
    elif i>=75 and i<90:
        b.append(i)
    elif i>=50 and i<75:
        c.append(i)
    else:
        d.append(i)

print("===== STUDENT GRADE REPORT =====\n")

print("A Grade Students   :",a)
print("B Grade Students   :",b)
print("C Grade Students   :",c)
print("FaiL Students   :",d)

print("-"*30)
print("A Count   :",len(a))
print("B Count   :",len(b))
print("C Count   :",len(c))
print("FaiL Count   :",len(d))
print("-"*30)
print("Total Students:", len(n))