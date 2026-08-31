'''import math
n=int(input("enter the no"))
print(math.factorial(n))



n=int(input(""))
sum=0
i=1
while i<=n//2:
	if n%i==0:
		sum+=i
	i+=1
if sum==n:
	print("p")
else:
	print("v")


for i in range (1,21):
	if i%2==0:
		continue
	print(i)



a=[10,20,30]
b=[10,20,30]
print(a is not b)
print(a is b)
print(a ==b)


print(5|6)
print(5^6)
print(5&6)



s="Leetcode"
lower=0
uper=0
for i in s:
	if "a"<=i<="z":
		lower+=1
	else:
		uper+=1
if "A"<=s[0]<="Z":
	lower+=1
if len(s)==lower or len(s)==uper:
	print(True)
else:
	print(False)

'''
# n=int(input("enter the no."))
# for i in range(1,n+1):
#     print()
#     for j in range(1,i+1):
#         print(j,end=" ")


# for i in range(n,0,-1):
#     print()
#     for j in range(i,0,-1):
#         print(j,end=" ")


# word=input("")
# c=0
# for ch in word:
#     c+=1
# print(c)

#46Check if a substring appears at both the start and end. S = "abcabca", Sub="abca" TRUE
# s="abcabca"
# s1="abca"
# if s.startswith(s1) and s.endswith(s1):
#     print(True)
# else:
#     print(False)

# #87Print all permutations of a string with repetition. S = "aab" "aab", "aba", "baa"
# s="aab"
# a=[]
# for i in range(len(s)):
# 	for j in range(len(s)):
# 		for k in range(len(s)):
# 			if i!=j and i!=k and j!=k:
# 				x=(s[i]+s[j]+s[k])
# 				if x not in a:
# 					a.append(x)
# print(a)


#34Find the shortest word. S = "find the shortest word" "the"
# s="find the shortest word".split()
# a=s[0]
# for short in s:
#     if len(short)<len(a):
#         a=short
# print(a)


# 47Check if one string is a substring of another using only concatenation.
#  S1 = "CDAB", S2 = "ABCD" S1 is substring of S2S2 (ABCDABCD) → True
# s1="cdab"
# s2="abcd"
# if s2 in s1+s1:
#     print(True)
# else:
#     print(False)
    
#73Find the longest palindromic substring. S = "babad" "bab" (or "aba")
# s="babad"
# a=[]
# for i in range(len(s)):
#     for j in range(i,len(s)):
#         ch=s[i:j+1]
#         if ch==ch[::-1]:
#                 a.append(ch)
# print(max(a,key=len))


#28Count occurrences of a word. 
# S = "word word other word", Word = "word" 3
# s="word word other word".split()
# w="word"
# c=0
# for i in s:
#     if i==w:
#         c+=1
# print(c)


#61Count total alphabets, digits, and special characters. 
# S = "a1b!c2" Alphabets: 3, Digits: 2, Special: 1
# s="a1b!c2"
# a=0
# d=0
# sp=0
# for i in s:
#     if i.isalpha():
#         a+=1
#     elif i.isdigit():
#         d+=1
#     else:
#         sp+=1
# print("Alphabets: ",a ," Digits:",d," Special:", sp)



m=[[1,3,4],[6,7,8]]
ma=m[0][0]
for row in m:
    for v in row:
        if v> ma:
            ma=v
print("max",ma)





n=int(input("size"))
if n==0:
     print(-1)
else:
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    leadersum=0
    for i in range(n):
         isleader=True
         for j in range(i+1,n):
              if arr[i]<=arr[j]:
                   isleader=False
                   break
         if isleader:
            leadersum+=arr[i]
    print("sum is ",leadersum)