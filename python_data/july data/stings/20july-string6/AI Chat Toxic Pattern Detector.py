'''
# 6. AI Chat Toxic Pattern Detector

An AI moderation system wants to detect whether a sentence contains three consecutive repeating characters.

If found:

text
Spam Pattern Found


Else:

text
Clean Message


### Input:

text
heyyy broooo welcome


### Output:

text
Spam Pattern Found
'''
n=input("=")
count=1
for i in range(1,len(n)):
    if n[i]==n[i-1]:
        count+=1
        if count>=3:
            print("Spam Pattern Found")
            break
    else:
        count=1

else:
    print("Clean Message")