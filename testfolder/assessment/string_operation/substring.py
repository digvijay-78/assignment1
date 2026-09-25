#print all subsring


def all_string(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)+1):
            print(a[i:j])



