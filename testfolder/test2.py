"""QNO 1:(3+3)
======
Develop a *menu-driven Python application* that performs different String and List operations.

The application must be designed using *Packages and Modules*. The business logic for
 each operation should be written in separate modules, while main.py should be responsible for displaying the menu,
accepting user input, and calling the appropriate functions.

---

==>Required Project Structure

Assessment/
│
├── main.py
│
├── string_operations/
│   ├── _init_.py
│   └── substring.py
│
└── list_operations/
    ├── _init_.py
    └── subarray.py


---

=> Menu

The application should continuously display the following menu:

========== MENU ==========

1. Print All Substrings
2. Minimum Size Subarray Sum
3. Exit

Enter your choice:

## Option 1 – Print All Substrings

Ask the user to enter a string.

Create a function inside:

text
string_operations/substring.py


The function should print all possible substrings of the given string.

=>Sample Input

Enter your choice: 1

Enter a string: ABC

Expected Output

All substrings are:

A
AB
ABC
B
BC
C

Option 2 – Minimum Size Subarray Sum

Ask the user to enter the number of elements, list elements, and target value.

Create a function inside:

list_operations/subarray.py

The function should find the **minimum length of a contiguous subarray** whose sum is greater than or equal to the given target.

If no such subarray exists, return `0`.

==> Sample Input

Enter your choice: 2

Enter number of elements: 6

Enter elements:
2
3
1
2
4
3

Enter target: 7

=>Expected Output

List: [2, 3, 1, 2, 4, 3]
Target: 7

Minimum size subarray: 2

Explanation:

[4, 3] → Sum = 7
Length = 2


 Option 3 – Exit

When the user selects `3`, display:

Thank you for using the application.

and terminate the program.

---

# Important Requirements

1. The application must be **menu-driven**.
2. The menu should continue displaying until the user selects **Exit**.
3. Use separate **packages and modules** as specified.
4. Do not write the complete business logic inside `main.py`.
5. Create separate functions for both operations.
6. Take all required data from the user.
7. Use proper function calling and module importing.
8. For Option 2, consider only **positive integers**.
9. Do not use external libraries to directly solve either problem.
10. Handle an invalid menu choice appropriately.

### Invalid Choice Example

Enter your choice: 5

Invalid choice. Please enter a valid choice.

## Complete Application Flow

text
========== MENU ==========

1. Print All Substrings
2. Minimum Size Subarray Sum
3. Exit

Enter your choice: 1

Enter a string: ABC

All substrings are:

A
AB
ABC
B
BC
C


========== MENU ==========

1. Print All Substrings
2. Minimum Size Subarray Sum
3. Exit

Enter your choice: 2

Enter number of elements: 6
Enter elements:
2
3
1
2
4
3

Enter target: 7

Minimum size subarray: 2


========== MENU ==========

1. Print All Substrings
2. Minimum Size Subarray Sum
3. Exit

Enter your choice: 3

Thank you for using the application.

=========================================="""