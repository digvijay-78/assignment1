'''
2.
Find the Most Frequently Occurring Word
News Channel Keyword Analyzer

A news agency analyzes breaking news headlines to identify the most repeated keyword in a report.

Write a Python program to find the word with the highest frequency.

Input:
india won the match and india created history
Output:
india

n = input("=").split()

max_count = 0
max_word = ""

for i in n:
    count = 0
    for j in n:
        if i == j:
            count += 1

    if count > max_count:
        max_count = count
        max_word = i

print(max_word)
'''


n = input("=").split()

count = 0
c = ""

for i in n:
    if n.count(i) > count:
        count = n.count(i)
        c = i

print(c)