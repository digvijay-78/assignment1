#project
import random
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
elif mode=="Intermediate":
    level=2
else:
    if mode=="Advanced":
        level=3
    else:
        print("not allowed")
i=0

while True:
    if level==1:
        question=random.randint(1,3)
    elif level==2:
        question=random.randint(5,10)
    elif level==3:
        question=random.randint(11,15)
    else:
        print("error in level")
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
            no=random.randrange(10)
            a=no**3
            print(f"what is the cube of {no}")
            answer=int(input("Enter the answer"))
            if answer==a:
                print("bingo")
                count+=1
            else:
                print("wrong answer")
        case 3:
            no1=random.randrange(1,20)
            no2=random.randrange(1,10)
            a=no1*no2
            print(f"what is the area of square whose lenght is {no1} and bredth is {no2}")
            answer=int(input("Enter the answer"))
            if answer==a:
                print("bingo")
                count+=1
            else:
                print("wrong answer")
        case 4:
            no=random.randrange(100)
            a=no//10
            b=no%7
            sum=0
            print(f"The given no is buzz no. or not:{no}")
            answer=input("Enter the answer:yes/no").lower()
            if (a == 7 or b == 0) and answer == "yes":
                print("bingo")
                count += 1
            else:
                print("wrong answer")
        
        case 5:
                    
            
    if count==5:
        break