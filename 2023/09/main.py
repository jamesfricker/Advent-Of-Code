from dataclasses import dataclass
from typing import List, Tuple, Dict
import math


with open("example.txt") as f:
    example = f.read().splitlines()

with open("input.txt") as f:
    input_txt = f.read().splitlines()


@dataclass
class Game:
    lines: List[List[int]]

def read_input(text):
    g = Game(lines=[])
    for line in text:
        g.lines.append([int(x) for x in line.split(" ")])
    return g

def part_one(g: Game):
    total = 0
    for line in g.lines:
        all_diffs = []
        diffs = [line[k] - line[k-1] for k in range(1, len(line))]
        all_diffs.append(diffs)
        # while diffs is not all 0
        is_all_zero = False
        while not is_all_zero:
            diffs = [all_diffs[-1][k] - all_diffs[-1][k-1] for k in range(1, len(all_diffs[-1]))]
            all_diffs.append(diffs)
            is_all_zero = all([x == 0 for x in diffs])

        new_history = 0
        for i in range(1, len(all_diffs)):
            index = len(all_diffs) - 1 - i
            new_history = new_history + all_diffs[index][-1]

        total += new_history + line[-1]

    return total


def part_two(g: Game):
    total = 0
    for line in g.lines:
        all_diffs = []
        diffs = [line[k] - line[k-1] for k in range(1, len(line))]
        all_diffs.append(diffs)
        # while diffs is not all 0
        is_all_zero = False
        while not is_all_zero:
            diffs = [all_diffs[-1][k] - all_diffs[-1][k-1] for k in range(1, len(all_diffs[-1]))]
            all_diffs.append(diffs)
            is_all_zero = all([x == 0 for x in diffs])

        new_history = 0
        for i in range(1, len(all_diffs)):
            index = len(all_diffs) - 1 - i
            new_history = all_diffs[index][0] - new_history
        this_new_value = line[0] - new_history
        total += this_new_value

    return total


def main():
    e1 = part_one(read_input(example))
    print(e1)
    assert e1 == 114
    print("example 1 passed")
    p1 = part_one(read_input(input_txt))
    print(p1)

    e2 = part_two(read_input(example))
    print(e2)
    assert e2 == 2

    p2 = part_two(read_input(input_txt))
    print(p2)


    return 0

if __name__ == "__main__":
    main()
