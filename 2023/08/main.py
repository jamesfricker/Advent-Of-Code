from dataclasses import dataclass
from typing import List, Tuple, Dict
import math
# read example.txt

with open("example.txt") as f:
    example = f.read().splitlines()

with open("example2.txt") as f:
    example_2 = f.read().splitlines()

with open("input.txt") as f:
    input_txt = f.read().splitlines()

with open("p2_e1.txt") as f:
    example_p2 = f.read().splitlines()

@dataclass
class Game:
    maps: Dict[str,Tuple[str, str]]
    instructions: List[str]

def read_input(text):
    l1 = text[0]
    g = Game(maps={}, instructions=[])
    for t in l1:
        g.instructions.append(t)

    for line in text[1:]:
        if line:
            current, to = line.split("=")
            current = current.strip()
            to_left = to.split(",")[0].replace("(", "").replace(")", "").strip()
            to_right = to.split(",")[1].replace("(", "").replace(")", "").strip()
            g.maps[current] = (to_left, to_right)
    print(g)
    return g

def part_one(game: Game, current_position="AAA"):
    instruction_index = 0
    num_steps = 0
    while not current_position.endswith("Z"):
        this_instruction = game.instructions[instruction_index%len(game.instructions)]
        instruction_index += 1
        print(f"current_position: {current_position}")
        print(f"this_instruction: {this_instruction}")

        if this_instruction == "L":
            next_position = game.maps.get(current_position)[0]
        elif this_instruction == "R":
            next_position = game.maps.get(current_position)[1]
        else:
            next_position = current_position
        current_position = next_position
        num_steps += 1


    return num_steps

@dataclass
class Position:
    current: str

    def next(self, instruction, game):
        if instruction == "L":
            next_position = game.maps.get(self.current)[0]
        elif instruction == "R":
            next_position = game.maps.get(self.current)[1]
        self.current = next_position

def part_two(game: Game):
    # find starting points, all those that end in A
    current_points: List[Position] = [Position(current=v) for v in game.maps.keys() if v.endswith("A")]
    steps = []
    for p in current_points:
        steps.append(part_one(game, p.current))

    return math.lcm(*steps)

def main():
    e1 = part_one(read_input(example))
    e2 = part_one(read_input(example_2))
    print(e1)
    print(e2)
    assert e1 == 2
    assert e2 == 6
    print("example 1 passed")
    p1 = part_one(read_input(input_txt))
    print(p1)

    e2 = part_two(read_input(example_p2))
    print(f"e2: {e2}")
    assert e2 == 6

    p2 = part_two(read_input(input_txt))
    print(p2)


    return 0

if __name__ == "__main__":
    main()
