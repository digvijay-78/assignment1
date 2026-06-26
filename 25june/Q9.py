'''9. Neon Number LED Unlock Game
You're programming a new LED display game. The game level unlocks only when a neon number is entered.

A neon number is a number where the sum of the digits of its square is equal to the number itself.
Example: 9 → 9² = 81 → 8 + 1 = 9

Accept a number from the player.
Check whether it is a neon number using loops.

If true, display:
Glowing Success! You've found the Neon Number!

Otherwise display:
Try again! Not quite glowing yet.

Input:
9

Output:
Glowing Success! You've found the Neon Number!'''


n=int(input("= "))
product=n**2
t=n**2
f=0
s=0
while product > 0:
	d=product%10
	s=s+ d
	product=product//10

if s==n:
	print("Glowing Success! You've found the Neon Number!")
else:
	print("Try again! Not quite glowing yet.")

for i in range(len(str(t))):
	d=t%10
	f=f+ d
	t=t//10
if f==n:
	print("Glowing Success! You've found the Neon Number!")
else:
	print("Try again! Not quite glowing yet.")
