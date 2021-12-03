import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, "data.txt")

oxygen_generator_values = []
oxygen_generator_rating = ""
oxygen_generator_rating_decimal = 0
co2_scrubber_values = []
co2_scrubber_rating = ""
co2_scrubber_rating_decimal = 0
oxygen_times_co2 = 0

# returns positive value if there are more 1's than 0's
# returns negative value if there are more 0's than 1's
# returns 0 if there is an equal number of 1's and 0's
def bit_criteria(idx, collection):
    ones = 0
    zeros = 0
    for item in collection:
        if item[idx] == "1":
            ones += 1
        if item[idx] == "0":
            zeros += 1
            
    return ones - zeros

def binary_to_decimal(binary):
    return int(binary, 2)     

def filter_values(idx, collection, ones):
    ret_collection = []

    for item in collection:
        if ones:
            if item[idx] == "1":
                ret_collection.append(item)
        else:
            if item[idx] == "0":
                ret_collection.append(item)

    return ret_collection

# calculate the product of horizontal position and depth after a series of movements
with open(filename) as data:
    lines = data.readlines()

    oxygen_generator_values = lines
    co2_scrubber_values = lines

    for i in range(0, 12):
        if len(oxygen_generator_values) > 1:
            if bit_criteria(i, oxygen_generator_values) >= 0:
                oxygen_generator_values = filter_values(i, oxygen_generator_values, True)
            else:
                oxygen_generator_values = filter_values(i, oxygen_generator_values, False)

    for i in range(0, 12):
        if len(co2_scrubber_values) > 1:
            if bit_criteria(i, co2_scrubber_values) < 0:
                co2_scrubber_values = filter_values(i, co2_scrubber_values, True)
            else:
                co2_scrubber_values = filter_values(i, co2_scrubber_values, False)

oxygen_generator_rating_decimal = binary_to_decimal(oxygen_generator_values[0])
co2_scrubber_rating_decimal = binary_to_decimal(co2_scrubber_values[0])
oxygen_times_co2 = oxygen_generator_rating_decimal * co2_scrubber_rating_decimal

print("+====================================+")
print("oxygen_generator_rating: " + str(oxygen_generator_values[0]))
print("oxygen_generator_rating_decimal: " + str(oxygen_generator_rating_decimal))
print("co2_scrubber_rating: " + str(co2_scrubber_values[0]))
print("co2_scrubber_rating_decimal: " + str(co2_scrubber_rating_decimal))
print("oxygen times co2: " + str(oxygen_times_co2))
