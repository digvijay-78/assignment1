Q1. What is the value of result?



result = 2 \*\* 3 \*\* 2 + 10 // 3 \* 2 - 4 % 3



A) 512

B) 517

C) 519

D) 522

|answer==>(B) 517<br />3 \*\* 2 = 9, then 2 \*\* 9 = 512; 10//3\*2 = 6; 4%3 = 1 → 512+6-1 = 517.|
|-|



Q2. Evaluate this bitwise-logical hybrid:



x = 5

y = 2

z = 3

print(x \& y | z ^ x << 1)



A) 9

B) 13

C) 15

D) 7

|answer==>(A) 9<br />5 \& 2 = 0, 5 << 1 = 10, 3 ^ 10 = 9, then 0 \| 9 = 9.|
|-|





Q3. What does the following print?



print(not 5 > 3 \& 2 or 4 \*\* 2 // 3 + \~1 \& 7)



A) False

B) True

C) 11

D) 12

|answer==>(B) True<br />3 \& 2 = 2; 5 > 2 → True; not True → False.<br />Right side truthy hai, so overall result True.|
|-|



Q4. What is printed?



a = 256

b = 257

print((a is b - 1) == (a == b - 1))



A) True

B) False

C) TypeError

D) SyntaxError

|answer==>(A) True<br />b - 1 = 256. Dono comparisons True hain → True == True → True.|
|-|





Q5. What is the final value of res?



res = \~(5 + 3) << 2 \& 7 or not 10 // 3



A) 4

B) 0

C) True

D) 1

|answer==>(A) 4<br />\~8 = -9, -9 << 2 = -36, -36 \& 7 = 4.<br />4 or ... → 4.|
|-|





Q6. What is the type and value of result?



result = 0 or "Python" and \[] or 42



A) 42 (int)

B) \[] (list)

C) "Python" (str)

D) True (bool)

|answer==>(A) 42 (int)<br />and pehle evaluate hota hai: "Python" and \[] → \[].<br />Then 0 or \[] or 42 → 42.|
|-|





Q7. How many times is lst.pop() executed, and what is the final value of result?



lst = \[10, 20, 30, 40]

x = 0

result = (x > 0) and (lst.pop() > 15) or (lst.pop() < 25)



A) 1 call, True

B) 2 calls, True

C) 1 call, False

D) 2 calls, False

|answer==>(C) 1 call, False<br />x > 0 → False, so first pop() execute nahi hota.<br />Second pop() → 40; 40 < 25 → False.|
|-|



Q8. What is printed?



print(5 or 0 and 2, 0 and 5 or 2)



A) 5 2

B) True True

C) 5 0

D) 0 2

|answer==>(A) 5 2<br />5 or ... → 5<br />0 and 5 or 2 → 2.|
|-|



Q9. Why does this loop never terminate, and what is the fix?



i = 0

while i < 10:

&#x20;   if i % 3 == 0:

&#x20;       continue

&#x20;   print(i)

&#x20;   i += 1



A) i is never incremented when i%3==0; fix by moving i += 1 before the if.

B) The condition i < 10 is always true; fix by changing to <=.

C) continue is invalid inside while.

D) print(i) raises an error.

|answer==>(A)<br />i = 0 par continue execute hota hai aur i += 1 skip ho jata hai. Isliye i hamesha 0 rahega.|
|-|



Q10. Which of the following expressions does NOT raise a ZeroDivisionError?

A) 10 // 0 or 5

B) 0 or 10 // 0

C) 0 \& 10 // 0

D) 10 // 0 and 5

|answer==>(None of the options) ⚠️<br />Chaaro expressions mein 10 // 0 evaluate hota hai, isliye sabhi ZeroDivisionError raise karte hain.|
|-|





Q11. What is the output of:



print(-17 // 4, -17 % 4, 17 // -4, 17 % -4)



A) -5 3 -5 -3

B) -4 -1 -4 1

C) -5 3 -4 1

D) -4 3 -5 -3

|answer==>(A) -5 3 -5 -3<br />Python floor division mein negative result ko floor karta hai.<br />-17//4=-5, -17%4=3, 17//-4=-5, 17%-4=-3.|
|-|



Q12. Compute \~-5 and \~5 respectively:

A) 4, -6

B) -4, 6

C) 4, 6

D) -4, -6

|answer==>(A) 4, -6<br />Formula: \~n = -(n+1)<br />\~-5 = 4, \~5 = -6.|
|-|





Q13. What is the integer output of:



print((\~0b1010) \& 0b1111, (-5 >> 1) \& 0b111)



A) 5, 3

B) 5, 5

C) 10, 3

D) 10, 5

|answer==>(B) 5, 5<br />\~10 \& 15 = 5<br />(-5 >> 1) \& 7 = -3 \& 7 = 5.|
|-|





Q14. Verify the Euclidean identity: a = b \* (a // b) + (a % b).

Which of the following is FALSE for a = -10, b = 3?

A) a // b is -4

B) a % b is 2

C) 3 \* -4 + 2 = -10

D) a // b is -3

|answer==>(D) a // b is -3<br />Actually -10 // 3 = -4.|
|-|





Q15. What is printed?



print(True + True, False \* 3, \~False \& True)



A) 2 0 1

B) 2 0 0

C) 1 0 1

D) 2 3 0

|answer==>(A) 2 0 1<br />True = 1, False = 0.<br />True+True=2, False\*3=0, \~False \& True = -1 \& 1 = 1.|
|-|





