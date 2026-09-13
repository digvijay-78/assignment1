import sumofdidgitpackage
import strongpackage
import spypackage
import reversepackage
import primepackage
import perfectpackage
import palpackage
import neonpackage
import harshpackage
import factpackage
import eonopackage
import countpackage
import automorphicpackage
import armpackage
while True:
    print("""========================================
       NUMBER ANALYSIS SYSTEM
========================================

1. Check Perfect Number
2. Check Palindrome Number
3. Check Strong Number
4. Check Armstrong Number
5. Check Prime Number
6. Check Even or Odd
7. Find Factorial
8. Find Sum of Digits
9. Reverse a Number
10. Find Number of Digits
11. Check Automorphic Number
12. Check Neon Number
13. Check Spy Number
14. Check Harshad Number
15. Exit""")
    choice=int(input("enter the choice"))
    match choice:
        case 1:
            print("1. Check Perfect Number")
            number=int(input("enter the no"))
            print(perfectpackage.perfectn(number))
        case 2:
            print("2. Check Palindrome Number")
            n=input("enter the no")
            print(palpackage.paln(n))
        case 3:
            print("3. Check Strong Number")
            n=int(input("enter the no"))
            print(strongpackage.strongn(n))
        case 4:
            print("4. Check Armstrong Number")
            n=input("enter the no")
            print(armpackage.armstrong(n))
        case 5:
            print("5. Check Prime Number")
            if primepackage.prime(int(input("enter the no") ))==0:
                 print("not prime")
            else:
                 print("prime")
        case 6:
            print("6. Check Even or Odd")
            n=int(input("enter the no"))
            print(eonopackage.evenodd(n))
        case 7:
            print("7. Find Factorial")
            n=int(input("enter the no"))
            print(factpackage.fact(n))
        case 8:
            print("8. Find Sum of Digits")
            n=int(input("enter the no"))
            print(sumofdidgitpackage.su(n))
        case 9:
            print("9. Reverse a Number")
            n=(input("enter the no"))
            print(reversepackage.reverse(n))
        case 10:
            print("10. Find Number of Digits")
            n=int(input("enter the no"))
            print(countpackage.count(n))
        case 11:
            print("11. Check Automorphic Number")
            n=input("enter the no")
            print(automorphicpackage.auto(n))
        case 12:
            print("12. Check Neon Number")
            n=input("enter the no")
            print(neonpackage.neon(n))
        case 13:
            print("13. Check Spy Number")
            n=input("enter the no")
            print(spypackage.spy(n))
        case 14:
            print("14. Check Harshad Number")
            n=input("enter the no")
            print(harshpackage.harsh(n))
        case 15:
            print("Thank you for using Number Analysis System! Program terminated.")
            break
        case _:
            print("invalid choice")