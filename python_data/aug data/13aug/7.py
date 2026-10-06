'''7.

A cricket academy wants to analyze player performance. Each player's information is stored as a tuple.

Tuple Format:

(player_id, player_name, runs_scored)

Requirements:

Read N player records from the user and store them as tuples in a list.
Display all player records.
Find and display the player who scored the highest runs.
Find and display the player who scored the lowest runs.
Calculate and display the total runs scored by all players.
Calculate and display the average runs scored.
Display players who scored more than 50 runs.

Test Case:

Input:

Enter number of players: 5

101 Virat 82
102 Rohit 45
103 Gill 120
104 Hardik 38
105 SKY 76

Expected Output:

All Players:
(101, 'Virat', 82)
(102, 'Rohit', 45)
(103, 'Gill', 120)
(104, 'Hardik', 38)
(105, 'SKY', 76)

Highest Scorer:
(103, 'Gill', 120)

Lowest Scorer:
(104, 'Hardik', 38)

Total Runs:
361

Average Runs:
72.2

Players Scoring More Than 50 Runs:
(101, 'Virat', 82)
(103, 'Gill', 120)
(105, 'SKY', 76)
'''


players = []
n = int(input("enter number of players: "))
for i in range(n):
    p_id = int(input("enter player ID: "))
    p_name = input("enter player Name: ")
    runs = int(input("enter Runs: "))
    player = (p_id, p_name, runs)
    players.append(player)
print("All Players:")
for p in players:
    print(p)

highest = players[0]
for p in players:
    if p[2] > highest[2]:
        highest = p
print("Highest Scorer:")
print(highest)

lowest = players[0]
for p in players:
    if p[2] < lowest[2]:
        lowest = p
print("Lowest Scorer:")
print(lowest)

total = 0
for p in players:
    total = total + p[2]
print("Total Runs:")
print(total)
average = total / n
print("Average Runs:")
print(average)

print("Players Scoring More Than 50 Runs:")
for p in players:
    if p[2] > 50:
        print(p)