import math
p1 = int(input("Please give point 1's x value"))
q1 = int(input("Please give point 1's y value"))
p2 = int(input("Please give point 2's x value"))
q2 = int(input("Please give point 2's y value"))
d = math.sqrt(math.pow(p2 - p1, 2) + math.pow(q2 - q1, 2))
print("The distance between P1 and P2 is", d)