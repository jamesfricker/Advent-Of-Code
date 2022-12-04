with open("input.txt") as f:
    lines = f.read().splitlines()


# calculate gamma rate
# gamma rate is most common 0 or 1 in each column
total_lines = len(lines)

sums = [0 for i in range(len(lines[0]))]
for l in lines:
    for i, x in enumerate(l):
        sums[i] += int(x)

print(sums)
print(total_lines)

gamma_binary = [1 if x > total_lines / 2 else 0 for x in sums]
epsilon_binary = [1 if x < total_lines / 2 else 0 for x in sums]

# int(bin,2) to convert to decimal
gamma_rate = int("".join(map(str, gamma_binary)), 2)
epsilon_rate = int("".join(map(str, epsilon_binary)), 2)

power_consumption = epsilon_rate * gamma_rate
print(power_consumption)

# part 2

# life_support_rating = oxygen_generator_rating * co2_scrubber_rating


# find most common element

oxygen_generator_nums = lines
co2_scrubber_nums = lines
oxygen_generator_num = -1
co2_scrubber_num = -1
for index in range(len(sums)):
    common_element_upper = sum([int(x[index]) for x in oxygen_generator_nums])
    common_element_lower = sum([int(x[index]) for x in co2_scrubber_nums])

    bool_element_upper = (
        1 if common_element_upper >= len(oxygen_generator_nums) / 2 else 0
    )
    bool_element_lower = 1 if common_element_lower < len(co2_scrubber_nums) / 2 else 0
    oxygen_generator_nums = list(
        filter(
            lambda x: str(x[index]) == str(bool_element_upper), oxygen_generator_nums
        )
    )
    co2_scrubber_nums = list(
        filter(lambda x: str(x[index]) == str(bool_element_lower), co2_scrubber_nums)
    )
    if len(oxygen_generator_nums) == 1:
        oxygen_generator_num = oxygen_generator_nums[0]
    if len(co2_scrubber_nums) == 1:
        co2_scrubber_num = co2_scrubber_nums[0]


oxygen_generator_rating = int("".join(oxygen_generator_num), 2)
print(oxygen_generator_rating)
co2_scrubber_rating = int("".join(co2_scrubber_num), 2)
print(co2_scrubber_rating)
life_support_rating = oxygen_generator_rating * co2_scrubber_rating
print(life_support_rating)
# 4406844
