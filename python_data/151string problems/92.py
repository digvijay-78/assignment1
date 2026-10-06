#92Check if two strings are pq-balanced. S1 = "pqqp", S2 = "qpqp" 
# Example dependent on specific "pq-balanced" definition
s1 = "pqqp"
s2 = "qpqp"

if s1.count("p") == s1.count("q"):
    print("S1 is pq-balanced")
else:
    print("S1 is not pq-balanced")

if s2.count("p") == s2.count("q"):
    print("S2 is pq-balanced")
else:
    print("S2 is not pq-balanced")