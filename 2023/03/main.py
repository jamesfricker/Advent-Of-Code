from dataclasses import dataclass

with open("example.txt") as f:
    example = f.read().splitlines()

# with open("example_p2.txt") as f:
#     example_p2 = f.read().splitlines()

with open("input.txt") as f:
    input_txt = f.read().splitlines()


def part_one(text):
    total = 0
    special_locations = []

    seen = [[0 for x in range(len(text[0]))] for y in range(len(text))]

    for y, line in enumerate(text):
        # convert line to str
        str_line = str(line)
        # search for non-digit, characters
        for x, char in enumerate(str_line):
            if not char.isdigit() and char != ".":
                special_locations.append((x, y))
    for x, y in special_locations:
        for left, right in [(-1, -1), (-1, 1), (-1, 0), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]:
            new_location = (x + left, y + right)
            if new_location[0] < 0 or new_location[1] < 0:
                continue
            if new_location[0] >= len(text[0]) or new_location[1] >= len(text):
                continue
            if seen[new_location[1]][new_location[0]] == 1:
                continue
            seen[new_location[1]][new_location[0]] = 1

            if text[new_location[1]][new_location[0]].isdigit():
                # we need to search left and right to get the full number
                number_start = new_location[0]
                number_end = new_location[0]

                # search left
                while number_start >= 0 and text[new_location[1]][number_start].isdigit():
                    number_start -= 1
                    seen[new_location[1]][number_start-1] = 1

                # search right
                while number_end < len(text[0]) and text[new_location[1]][number_end].isdigit():
                    number_end += 1
                    seen[new_location[1]][number_end-1] = 1

                number = text[new_location[1]][number_start + 1:number_end]
                total += int(number)

    return total


def part_two(text):
    total = 0
    special_locations = []
    seen = [[0 for x in range(len(text[0]))] for y in range(len(text))]

    for y, line in enumerate(text):
        # convert line to str
        str_line = str(line)
        # search for non-digit, characters
        for x, char in enumerate(str_line):
            if not char.isdigit() and char != ".":
                special_locations.append((x, y))

    for x, y in special_locations:
        found = 0
        numbers = []
        for left, right in [(-1, -1), (-1, 1), (-1, 0), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]:
            new_location = (x + left, y + right)
            if new_location[0] < 0 or new_location[1] < 0:
                continue
            if new_location[0] >= len(text[0]) or new_location[1] >= len(text):
                continue
            if seen[new_location[1]][new_location[0]] == 1:
                continue
            if text[new_location[1]][new_location[0]].isdigit():
                # we need to search left and right to get the full number
                number_start = new_location[0]
                number_end = new_location[0]

                # search left
                while number_start >= 0 and text[new_location[1]][number_start].isdigit():
                    number_start -= 1
                    seen[new_location[1]][number_start-1] = 1

                # search right
                while number_end < len(text[0]) and text[new_location[1]][number_end].isdigit():
                    number_end += 1
                    seen[new_location[1]][number_end-1] = 1

                number = text[new_location[1]][number_start + 1:number_end]
                found += 1
                numbers.append(int(number))

        if found == 2:
            total += numbers[0] * numbers[1]
    return total

def main():

    example_p1 = part_one(example)
    print(example_p1)
    assert example_p1 == 4361

    p1 = part_one(input_txt)
    print(p1)

    example_p2 = part_two(example)
    print(example_p2)
    assert example_p2 == 467835

    p2 = part_two(input_txt)
    print(p2)

if __name__ == "__main__":
    main()
