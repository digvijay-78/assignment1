from list_operation.subarray import mini
from string_operation.substring import all_string

while True:
    
    v=int(input("enter the choice:"))
    match v:
        case 1:
            a=input("enter the string")
            all_string(a)
        case 2:
            v=int(input("enter the no of elements"))
            a=[]
            for i in range(v):
                a.append(int(input("")))
            k=int(input("enter the target"))
            mini(a,k)
        case 3:
            print("thankyou")
            break
        case _:
            print("invalid syntax")

