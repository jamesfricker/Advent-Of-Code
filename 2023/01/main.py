# read example.txt

with open("example.txt") as f:
    example = f.read().splitlines()

with open("example_p2.txt") as f:
    example_p2 = f.read().splitlines()

with open("input.txt") as f:
    input_txt = f.read().splitlines()


def get_calibration_values(text):
    total_calibration = 0
    for line in text:
        first_value = None
        last_value = None
        for value in line:
            # if value is a number
            if value.isdigit():
                if not first_value:
                    first_value = int(value)
                last_value = int(value)
        total_calibration += first_value * 10 + last_value
    return total_calibration


def get_calibration_values_part_two(text):
    total_calibration = 0
    number_word_mapping = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    for line in text:
        all_indexes = [
            (index, int(char)) for index, char in enumerate(line) if char.isdigit()
        ]

        for word, number in number_word_mapping.items():
            index = line.find(word)
            while index != -1:
                all_indexes.append((index, number))
                index = line.find(word, index + 1)

        all_indexes.sort(key=lambda x: x[0])
        if all_indexes:
            first_value = all_indexes[0][1]
            last_value = all_indexes[-1][1]
            total_calibration += first_value * 10 + last_value

    return total_calibration


def main():
    example_answer = get_calibration_values(example)
    print(example_answer)
    assert example_answer == 142
    print(get_calibration_values(input_txt))

    example_answer_p2 = get_calibration_values_part_two(example_p2)
    assert example_answer_p2 == 281
    print(get_calibration_values_part_two(input_txt))


if __name__ == "__main__":
    main()
