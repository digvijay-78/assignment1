'''1.Student Marks Management
Create a program to store student marks in a List and perform operations.

Requirements:

Add student marks into a List
Display all marks
Find highest and lowest marks
Count students who scored above 75

Test Cases:

Input: [45, 67, 89, 90, 76] → Highest = 90, Lowest = 45, Count Above 75 = 3
Input: [10, 20, 30] → Highest = 30, Lowest = 10, Count Above 75 = 0
Input: [100, 99, 98] → Highest = 100, Lowest = 98, Count Above 75 = 3
'''
# a=input("enter the marks using space ").split()
# print(a)
# # print(max(a))
# # print(min(a))
# l=a[0]
# s=a[0]
# for i in a:
#    if i>l:
#        l=i
#    if i<s:
#       s=i

# print("Highest=",l)
# print("lowest=",s)
# c=0
# for i in range(len(a)):
#    if int(i)>=75:
#         c+=1
# print("Count Above 75 =",c)


a =int(input("Enter the size of list: "))
nums = []
for i in range(a):
	x = int(input("Enter marks: "))
	nums.append(x)
print("All Students marks: ", nums)
print("Highest Marks: ", max(nums))
print("Lowest Marks: ", min(nums))
count = 0
for i in nums:
	if i>75:
		count+=1
print("Count students who scored above 75: ", count)