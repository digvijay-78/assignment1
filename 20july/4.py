'''
# 4. Cloud Storage Duplicate File Name Resolver

A cloud storage company stores uploaded filenames from users.

Sometimes multiple duplicate filenames are uploaded.

The system should:

* Keep the first occurrence unchanged
* Add (1), (2), (3)... for duplicates

### Input:

text
file file image file image data


### Output:

text
file file(1) image file(2) image(1) data
'''
n=input("=").split()
c=""
d=""
count=0
for i in n:
    if c not in  n:
        d=d+i+"({count})"+" "
        count+=1

    else:
        d=d+i+" "
print(d)