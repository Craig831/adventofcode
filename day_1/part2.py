import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, "data.txt")

total_count = 0
increase_count = 0
prev_sum = 0
start_index = 0
end_index = 3
sum = 0

# read a collection of values
# calculate the sum of each incremental set of 3 values
# caclulate the number of times a sum is larger than the previous sum
with open(filename) as data:
    lines = data.readlines()

    while end_index < len(lines):
        for i in range(start_index, end_index):
            sum += int(lines[i])

        total_count += 1
        if prev_sum < sum:
            increase_count += 1

        start_index += 1
        end_index += 1
        prev_sum = sum
        sum = 0

print("+====================================+")
print("total summed groups of 3: " + str(total_count))
print("total increases: " + str(increase_count))
