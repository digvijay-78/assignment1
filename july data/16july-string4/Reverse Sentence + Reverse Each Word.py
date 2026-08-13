'''
2. Reverse Sentence + Reverse Each Word

Secret Military Communication Decoder
A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.

You must use the split() method.
Input:


Python is powerful


Output:


lufrewop si nohtyP
'''
n=input("=")
rev=""
for i in range(len(n)-1,-1,-1):
    rev += n[i]
    i-=1
s=rev
print(s)