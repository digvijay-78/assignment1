age=int(input("enter the age"))
am=int(input("enter the amount"))
type=input("enter the accident type")

if age>2 and am<50000 and type.lower()=="minor":
    print("approve the claim")
elif age>2 and am<50000 and type.lower()!="minor":
    print("approve it with inspection")
if age>2 and am>50000 and am<200000 and type.lower()=="major":
     print("approve it with inspection")





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
Highest Stock = 500

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
                    print("")'''


a=int(input("Enter tax: "))
if a<=250000:
		print("no tax")
elif a>=250001 :
		per=a-250000
		per1=(per*5/100)
		print("tax payable",per1)
elif a>=500001 :
		per2=a-250000 
		per3=(per2*5/100)
		per4=a-500000
		per5=(per4*20/100)
		print("tax payable",per5)
else:
		per6=a-250000 
		per7=(per6*5/100)
		per8=a-500000
		per9=(per8*20/100)
		per10=a-1000000
		per11=(per10*30/100)
		print("tax payable",per11)