'''4.
Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 11

NOTE:

Ignore case sensitivity (treat A and a same)
Consider only English alphabets for vowel/consonant counting
Vowels: A, E, I, O, U'''

n=input("enter =")#.lower()
st="aeiou"
count=0

for i in n:
	if i==" ":
		continue 
	if i not in st:
		 count+=1
print(count)