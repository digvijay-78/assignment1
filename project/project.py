#project
import random
import datetime
print("                                      ==============================   ")
print("                                     | Welcome to the aptti Games  |")
print("                                      ------------------------------   ")
print("                                     |  GAIN KNOWLEGE WHILE PLAYIG |")
print("                                      ==============================  ")

print("                                            LOGIN/SIGN UP")

print("                                        ALREADY HAVE AN ACCOUNT?")
print("                                            or Guest account")
user=(input("yes/no                                       --->")).lower()
print("\n")
if user=="yes":
    print("                                         Welcome,cheaf")
elif user=="no":
    print("                                     lets make the account")
elif user=="guest":
    print("                                          Welcome Boss")
else:
    print("error")

print("                                           Choose The Mode level ")
print("                               Bigg          Intermediate         Advanced")

mode=input("Mode                                          = ").lower()
question=0
count=0

level=0
if mode=="bigg":
    level=1
elif mode=="intermediate":
    level=2
elif mode=="advanced":
    level=3
else:
    print("not allowed")
i=0

while True:
    if level==1:
        question=random.randint(1,5)
    elif level==2:
        question=random.randint(5,10)
    elif level==3:
        question=random.randint(11,15)
    else:
        print("error in level")
        break
    # match level:
        # case "bigg":
        #     question=random.randint(1,3)
        # case "intermediate":
        #     question=random.randint(5,10)
        # case "advanced":
        #     question=random.randint(10,15)
    match question:
        case 1:
            no=random.randrange(20)
            a=no*no
            print(f"what is the square of {no}")
            answer=int(input("Enter the answer"))
            if answer==a:
                print("bingo")
                count+=1
            else:
                print("wrong answer")
        case 2:
            no=random.randrange(15)
            a=no**3
            print(f"what is the cube of {no}")
            answer=int(input("Enter the answer"))
            if answer==a:
                print("bingo")
                count+=1
            else:
                print("wrong answer")
        case 3:
            no1=random.randrange(1,50)
            no2=random.randrange(1,40)
            a=no1*no2
            print(f"what is the area of rectangle, whose lenght is {no1} and bredth is {no2}")
            answer=int(input("Enter the answer"))
            if answer==a:
                print("bingo")
                count+=1
            else:
                print("wrong answer")
        case 4:
            no=random.randrange(100)
            c=no
            a=no%10
            b=c%7
            sum=0
            print(f"The given no is buzz no. or not:{no}")
            answer=input("Enter the answer:yes/no").lower()
            if (a == 7 or b == 0) and answer == "yes":
                print("bingo")
                count += 1
            else:
                print("wrong answer")
        
        case 5:
            p=random.randrange(1000)
            r=random.randrange(1,14)
            t=random.randrange(1,5)
            a=(p*r*t)/100
            print(f"What is the simple interest for principal amount = {p}, rate = {r}% and time = {t} years?")
            answer=float(input("Enter the answer: "))
            if answer==a:
                print("bingo")
                count += 1
            else:
                print("wrong answer")
        case 6:
            p=random.randrange(1000)
            r=random.randrange(1,14)
            t=random.randrange(1,5)
            a=p*((1+(r/100))**t)-p
            print(f"What is the CI for principal amount = {p}, rate = {r}% and time = {t} years?")
            answer=float(input("Enter the answer: "))
            if answer==a:
                print("bingo")
                count += 1
            else:
                print("wrong answer")
        case 7:
            cost=random.randrange(1000,20000)
            selling=random.randrange(1000,30000)
            profit=selling-cost
            profit_percentage=(profit/cost)*100
            print(f"The cost price of an item is {cost} and the selling price is {selling}. Find the profit/loss percentage.")  
            answer=float(input("Enter the answer: "))
            if answer==profit_percentage:
                print("bingo")
                count += 1
            else:
                print("wrong answer")
        case 8:
            no1=random.randrange(1,10)
            no2=random.randrange(1,5)
            a=no1**no2
            print(f"If the power of {no1} is {no2} , what will be the answer")
            answer=float(input("Enter the answer: "))
            if answer==a:
                print("bingo")
                count += 1
            else:
                print("wrong answer")
        case 9:

            # Matrix A
            a11 = random.randrange(0, 9)
            a12 = random.randrange(0, 9)
            a21 = random.randrange(0, 9)
            a22 = random.randrange(0, 9)

            # Matrix B
            b11 = random.randrange(0, 9)
            b12 = random.randrange(0, 9)
            b21 = random.randrange(0, 9)
            b22 = random.randrange(0, 9)

            # Correct Answer
            c11 = a11*b11 + a12*b21
            c12 = a11*b12 + a12*b22
            c21 = a21*b11 + a22*b21
            c22 = a21*b12 + a22*b22

            # Display Question
            print("Multiply the following matrices:\n")

            print("Matrix A")
            print(a11, a12)
            print(a21, a22)

            print("\nMatrix B")
            print(b11, b12)
            print(b21, b22)

            print("\nEnter the resultant matrix row-wise.")
            print("Format: c11 c12 c21 c22")

            # User Input
            u11, u12, u21, u22 = map(int, input("Answer: ").split())

            # Check Answer
            if (u11 == c11 and u12 == c12 and
                u21 == c21 and u22 == c22):
                print(" Correct Answer!")
                count+=1
            else:
                print(" Incorrect Answer.")
                print("Correct Result:")
                print(c11, c12)
                print(c21, c22)
        case 10:
            a=random.randrange(1,20)
            b=random.randrange(1,25)
            d = (a**2 + b**2) ** 0.5
            print(f"A right-angled triangle has sides of length {a} cm and {b} cm. Find the length of the hypotenuse.")
            answer=float(input("Enter the answer: "))
            if answer==d:
                print("bingo")
                count += 1
            else:
                print("wrong answer")
        
        case 11:
            year=random.randrange(1900,2101)
            month=random.randrange(1,13)
            

    if count == 5:
        print("Congratulations! You completed the game.")
        break