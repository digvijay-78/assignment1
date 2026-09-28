class Student:
    school = "ABC School"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name)
        print(self.marks)

student = Student("Rahul", 85)
student.display()
