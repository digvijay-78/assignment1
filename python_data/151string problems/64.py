#64Count frequency of each vowel. S = "programming" o: 1, a: 1 (e, i, u: 0)

a = input("enter the string: ")
vowel = "aeiouAEIOU"
result = ""
print("====Vowel Occured====")
for i in a:
    count =0
    if i in vowel and i not in result:
        print(i, ":", a.count(i), end =" ")
        result+=i
print()
print("====Vowels Not Occured====")
for i in vowel:
    if i not in result:
        print(i, ":", 0, end= " ")
        