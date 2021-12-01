import os

total_count = 0
increase_count = 0
prev_val = -1
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, "data.txt")

with open(filename) as data:
    lines = data.readlines()
    for line in lines:
        total_count += 1
        if prev_val != -1:
            if prev_val < int(line):
                increase_count += 1
        prev_val = int(line)

print("+====================================+")
print("total readings: " + str(total_count))
print("total increases: " + str(increase_count))
