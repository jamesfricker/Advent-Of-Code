with open("input.txt") as f:
    lines = f.read().splitlines()


def letter_to_int(letter):
    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.
    int_letter = ord(letter)
    if int_letter < 97:
        return int_letter % 65 + 27
    else:
        return int_letter % 97 + 1


total_score = 0
for line in lines:
    half = len(line) // 2
    first_half = line[:half]
    second_half = line[half:]

    letters = list(set(first_half).intersection((set(second_half))))

    for letter in letters:
        total_score += letter_to_int(letter)

print(total_score)
# 7889

# part 2

sublists = [lines[i : i + 3] for i in range(0, len(lines), 3)]

total_score = 0

for l in sublists:
    common_letters = list(set(l[0]).intersection(set(l[1]), set(l[2])))
    for letter in common_letters:
        total_score += letter_to_int(letter)

print(total_score)
# 2825
