import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, "data.txt")

aim = 0
distance = 0
depth = 0
distance_and_depth = 0

# calculate the product of horizontal position and depth after a series of movements
with open(filename) as data:
    lines = data.readlines()
    for line in lines:
        if line.split(' ')[0] == "forward":
            distance += int(line.split(' ')[1])
            depth += (aim * int(line.split(' ')[1]))
        if line.split(' ')[0] == "down":
            aim += int(line.split(' ')[1])
        if line.split(' ')[0] == "up":
            aim -= int(line.split(' ')[1])

distance_and_depth = distance * depth

print("+====================================+")
print("distance: " + str(distance))
print("depth: " + str(depth))
print("distance * depth: " + str(distance_and_depth))
