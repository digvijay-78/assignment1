great=[]
students=[]
class Student :
    
    def __init__(self) :
        
        self.rollno=input("enter the roll no")
        self.name=input("enter the name")
        self.marks=float(input("enter the marks "))
        print()
        students.append(self)
    def display(self):
        print("All students")
        for i in students:
             print(i.rollno, i.name, i.marks)
    def greater_60(self):
        for i in students:
            if i.marks>60:
                great.append(i)
        print("Students having marks greater than 60:")
        for i in great:
            print(i.rollno, i.name, i.marks)
    def highest(self):
        a=0
        highest=[]
        for i in students:
         if i.marks>a:
            a=i.marks
            highest.append(i)
        print("\nHighest Marks:")
        print(highest[-1].rollno,highest[-1].name,highest[-1].marks,"\n")
    def avg(self):
        a=0
        c=0
        for i in students:
            a+=i.marks
            c+=1
        if c!=0:
            avg=a/c
            print("Average Marks:\n",avg," \n")
        else:
            print("not valid")
        
