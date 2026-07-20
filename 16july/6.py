'''
6. Find Occurrence of a Word in a String

Product Review Analysis System

An e-commerce company wants to analyze customer reviews.

The company wants a Python program to count how many times a particular word appears in a review.

Input Sentence:


iphone is good and iphone battery is strong


Word:


iphone


Output:


2


---
'''
n=input("==").split()
a=input("=")
count=0
for i in n:
    if i == a :
        count+=1
print(count)

# sentence = input().split()
# word = input()
# 
# print(sentence.count(word))