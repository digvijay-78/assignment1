#Add Binary

a = "11"
b = "1"
e=bin(int(a))+bin(int(b))
print(e)


a = input("Enter 1st binary number: ")
b = input("Enter 2nd binary number: ")
result= int(a,2) + int(b,2)
print(int(a,2))
print("sums is: ", bin(result)[2:])
