'''8. A warehouse management system needs to identify the highest stock level among six different storage units to prioritize dispatch.
 The system should take the quantity of items stored in six units as input. It should compare all six values using nested conditions
 and determine which unit has the maximum stock. Display the highest stock value among all six units.

Input:
Unit1 = 120
Unit2 = 450
Unit3 = 300
Unit4 = 275
Unit5 = 500
Unit6 = 390

Output:
Highest Stock = 500'''

a=int(input("enter"))
b=int(input("enter"))
c=int(input("enter"))
d=int(input("enter"))
e=int(input("enter"))
f=int(input("enter"))

if a>b:
    if a>c:
            if a>d:
                  if a>e:
                        if a>f:
                              print("a is greater")
                        else:
                              print("f is greater")
                  else:
                        if e>f:
                              print("e is greater")                    
                        else:
                              print("f is greater")
            else:
                if d>e and d>f:
                    	    print("d is greater")
                else:
                    print("")