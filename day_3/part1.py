import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, "data.txt")

gamma_rate = ""
gamma_decimal = 0
epsilon_rate = ""
epsilon_decimal = 0
gamma_times_epsilon = 0

def binary_to_decimal(binary):
    return int(binary, 2)     

def more_ones_than_zeros(idx, lines):
    ones = 0
    zeros = 0
    for line in lines:
        if line[idx] == "1":
            ones += 1
        if line[idx] == "0":
            zeros += 1
            
    return ones > zeros

# calculate the product of horizontal position and depth after a series of movements
with open(filename) as data:
    lines = data.readlines()

    for i in range (0, 12):
        if (more_ones_than_zeros(i, lines)):
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

gamma_decimal = binary_to_decimal(gamma_rate)
epsilon_decimal = binary_to_decimal(epsilon_rate)
gamma_times_epsilon = gamma_decimal * epsilon_decimal

print("+====================================+")
print("gamma_rate: " + gamma_rate)
print("gamma_decimal: " + str(gamma_decimal))
print("epsilon_rate: " + epsilon_rate)
print("epsilon_decimal: " + str(epsilon_decimal))
print("gamma times epsilon: " + str(gamma_times_epsilon))
