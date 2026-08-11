import math

# Ask user for the coordinates of the first point.
x1point = int(input("Please give point 1's x value"))
y1point = int(input("Please give point 1's y value"))

# Ask user for the coordinates of the second point.
x2point = int(input("Please give point 2's x value"))
y2point = int(input("Please give point 2's y value"))

# Calculate the distance using the distance formula and sqrt() and pow().
distance = math.sqrt(math.pow(x2point - x1point, 2) + math.pow(y2point - y1point, 2))

# Output or give the Answer
print("The distance between Point 1 and Point 2 is", distance)
