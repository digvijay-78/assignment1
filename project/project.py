#project
import random
print("="*40)
print(" Welcome to the aptti Games  ")
print(" ------------------------------   ")
print(" GAIN KNOWLEGE WHILE PLAYIG ")
print("="*40)

print("\nChoose The Mode level ")
print("\n1)easy          2)medium         3)Hard".lower())

mode=(input("Mode= "))

level=0
if mode=="1" or mode=="easy":
    level=1
elif mode=="2" or mode=="medium":
    level=2
elif mode=="3" or mode=="hard":
    level=3
else:
    print("not allowed")

play_again="yes"

while play_again=="yes":
    count=0
    i=0

    while i<10:
        if level==1:
            question=random.randint(1,5)
        elif level==2:
            question=random.randint(5,10)
        elif level==3:
            question=random.randint(11,15)
        else:
            print("error in level")
            break

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
                last_digit = no % 10
                print(f"The given no is buzz no. or not:{no}")
                answer=input("Enter the answer:yes/no").lower()
                
                buzz = (last_digit == 7 or no % 7 == 0)
                if buzz and answer == "yes":
                    print("bingo")
                    count += 1
                elif not buzz and answer == "no":
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
                profit_percentage=abs(profit/cost)*100
                if profit >= 0:
                    print(f"The cost price is {cost} and the selling price is {selling}.")
                    print("Find the Profit Percentage.")
                else:
                    print(f"The cost price is {cost} and the selling price is {selling}.")
                    print("Find the Loss Percentage.")
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
                answer = int(input("Enter the answer: "))
                if answer==a:
                    print("bingo")
                    count += 1
                else:
                    print("wrong answer")
            case 9:

                #a
                a11 = random.randrange(0, 9)
                a12 = random.randrange(0, 9)
                a21 = random.randrange(0, 9)
                a22 = random.randrange(0, 9)

                #b
                b11 = random.randrange(0, 9)
                b12 = random.randrange(0, 9)
                b21 = random.randrange(0, 9)
                b22 = random.randrange(0, 9)

                #answer
                c11 = a11*b11 + a12*b21
                c12 = a11*b12 + a12*b22
                c21 = a21*b11 + a22*b21
                c22 = a21*b12 + a22*b22

                print("Multiply the following matrices:\n")

                print("Matrix A")
                print(a11, a12)
                print(a21, a22)

                print("\nMatrix B")
                print(b11, b12)
                print(b21, b22)

                print("\nEnter the resultant matrix row-wise.")
                print("Format: c11 c12 c21 c22")


                u11, u12, u21, u22 = map(int, input("Answer: ").split())


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
                month=random.randrange(1,12+1)
                if month==2:
                    if (year%400==0) or (year%4==0 and year%100!=0):
                        day=random.randrange(1,29+1)
                    else:
                        day=random.randrange(1,28+1)

                elif month==4 or month==6 or month==9 or month==11:
                    day=random.randrange(1,30+1)

                else:
                    day=random.randrange(1,31+1)

                print(f"What will be the day on {day}-{month}-{year}?")
                answer=input("Enter the answer: ").lower()
                d=day
                m=month
                y=year
                if m==1:
                    m=13
                    y=y-1
                elif m==2:
                    m=14
                    y=y-1
                K=y%100
                J=y//100
                h=(d+(13*(m+1))//5+K+K//4+J//4+5*J)%7


                if h==0:
                    if answer=="saturday":
                        print("bingo")
                        count+= 1
                    else:
                        print("Wrong answer")
                        print("Correct answer = Saturday")

                elif h==1:
                    if answer=="sunday":
                        print("bingo")
                        count+= 1
                    else:
                        print("Wrong answer")
                        print("Correct answer = Sunday")

                elif h==2:
                    if answer=="monday":
                        print("bingo")
                        count+= 1
                    else:
                        print("Wrong answer")
                        print("Correct answer = Monday")

                elif h == 3:
                    if answer == "tuesday":
                        print("bingo")
                        count+= 1
                    else:
                        print("Wrong answer")
                        print("Correct answer = Tuesday")

                elif h==4:
                    if answer=="wednesday":
                        print("bingo")
                        count+= 1
                    else:
                        print("Wrong answer")
                        print("Correct answer = Wednesday")

                elif h==5:
                    if answer=="thursday":
                        print("bingo")
                        count+= 1
                    else:
                        print("Wrong answer")
                        print("Correct answer = Thursday")

                else:
                    if answer=="friday":
                        print("bingo")
                        count+= 1
                    else:
                        print("Wrong answer")
                        print("Correct answer = Friday")
            case 12:
                no=random.randrange(2,64)
                binary = bin(no)[2:]
                print(f"Convert the binary number {binary} into decimal.")
                answer=int(input("Enter the answer: "))
                if answer==no:
                    print("bingo")
                    count+=1
                else:
                    print("wrong answer")
                    print("Correct answer =",no)
            case 13:
                a=random.randrange(2,8)
                b=random.randrange(2,8)
                c=random.randrange(2,8)
                d=random.randrange(2,8)
                x=a*c
                y=b*d
                print(f"If A:B = {a}:{b} and B:C = {c}:{d}, find A:C.")
                answer1=int(input("Enter the x part: "))
                answer2=int(input("Enter the y part: "))

                if answer1==x and answer2==y:
                    print("bingo")
                    count+=1
                else:
                    print("wrong answer")
                    print(f"Correct answer ={x}:{y}")
            case 14:
                a=random.randrange(10,50)
                b=random.randrange(10,50)
                #febonaki
                c=a+b
                d=b+c
                e=c+d
                f=d+e
                print("Find the missing number:")
                print(f"{a}, {b}, {c}, {d}, {e}, ?")
                answer=int(input("Enter the answer: "))
                if answer==f:
                    print("bingo")
                    count+=1
                else:
                    print("wrong answer")
                    print("Correct answer =",f)

            case 15:
                value=random.randrange(1000,10000)
                a=random.randrange(5,30)
                b=random.randrange(5,30)
                f=value*((100+a)/100) * ((100+b)/100)
                print(f"The price of an item is {value}.")
                print(f"It increases by {a}% and then increases by {b}%.")
                print("Find the final price.")

                answer=float(input("Enter the answer: "))
                if answer==f:
                    print("bingo")
                    count+=1
                else:
                    print("wrong answer")
                    print("Correct answer =",f)

        i += 1

    print("="*40)
    print("Game Over")
    print(f"Your Score : {count}/{i}")

    if i > 0:
        percentage = (count / i) * 100
    else:
        percentage = 0

    print("Percentage =", percentage, "%")

    if percentage >= 90:
        print("Grade : A+")
    elif percentage >= 75:
        print("Grade : A")
    elif percentage >= 60:
        print("Grade : B")
    elif percentage >= 40:
        print("Grade : C")
    else:
        print("Keep Practicing!")

    print("="*40)

    play_again=input("do you want to continue? (yes/no): ").lower()
    if play_again=="yes":
        print("great, let's go again!")
    else:
        print("thank you for playing!")