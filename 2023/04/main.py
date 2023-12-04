from dataclasses import dataclass
from typing import List

with open("example.txt") as f:
    example = f.read().splitlines()

# with open("example_p2.txt") as f:
#     example_p2 = f.read().splitlines()

with open("input.txt") as f:
    input_txt = f.read().splitlines()


@dataclass
class Set:
    my_cards: [int]
    their_cards: [int]
    game_number: int
    multiplier: int = 0

@dataclass
class Game:
    sets: List[Set]

def read_input(text) -> Game:
    g = Game(sets=[])
    for line in text:
        s = Set(my_cards=[], their_cards=[], game_number=0)
        str_line = str(line)
        game_number = str_line.split(":")[0].split(" ")[-1].strip()
        s.game_number = int(game_number)

        my_cards = str_line.split(":")[1].split("|")[0].split(" ")
        their_cards = str_line.split(":")[1].split("|")[1].split(" ")

        for card in my_cards:
            if card.isdigit():
                s.my_cards.append(int(card))
        for card in their_cards:
            if card.isdigit():
                s.their_cards.append(int(card))

        g.sets.append(s)
    return g

def part_one(game: Game):
    total = 0
    for s in game.sets:
        score = 0
        for card in s.my_cards:
            if card in s.their_cards:
                if score == 0:
                    score = 1
                else:
                    score *= 2
        total += score
    return total

def part_two(game: Game):
    for s in game.sets:
        set_index = game.sets.index(s) + 1
        s.multiplier += 1
        for card in s.my_cards:
            if card in s.their_cards:
                game.sets[set_index].multiplier += s.multiplier
                set_index += 1

    return sum([s.multiplier for s in game.sets])

def main():

    example_input = read_input(example)
    game_input = read_input(input_txt)

    e1 = part_one(example_input)
    print(f"example: {e1}")
    assert e1 == 13


    p1 = part_one(game_input)
    print(f"part 1: {p1}")

    e2 = part_two(example_input)
    print(f"example: {e2}")
    assert e2 == 30

    p2 = part_two(game_input)
    print(f"part 2: {p2}")



if __name__ == "__main__":
    main()
