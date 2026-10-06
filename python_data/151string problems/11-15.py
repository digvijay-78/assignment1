#11Get the character at a given index. S = "Python", Index = 2 t
s="python"
print(s[2])


#12 Get the Unicode code point of a character at index. S = "A", Index = 0 65
'''a=input("enter the chr")
s=int(input("enter the index"))
b= a[s]
print(ord(b))'''


#13Get the Unicode code point before index. S = "Hello", Index = 1 72 (Unicode for 'H')
'''
a=input("enter the chr")
s=int(input("enter the index"))
b= a[s-1]
print(b)
print(ord(b))
'''

#14Find the first occurrence of a character. S = "banana", Char = 'a' 1 (index)
'''a=input("enter the chr")
s=input("enter the chr")
for i in range(len(a)):
    if a[i]==s:
        print(i)
        break
'''



#15Find the last occurrence of a character. S = "banana", Char = 'a' 5 (index)
'''a=input("enter the chr")
s=input("enter the chr")
c=0
for i in range(len(a)):
    if a[i]==s:
        c=i
print(c)
'''


