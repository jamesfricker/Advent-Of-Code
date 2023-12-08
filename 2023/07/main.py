from dataclasses import dataclass
from typing import List, Dict
# read example.txt

with open("example.txt") as f:
    example = f.read().splitlines()

# with open("example_p2.txt") as f:
#     example_p2 = f.read().splitlines()

with open("input.txt") as f:
    input_txt = f.read().splitlines()

@dataclass
class HandType:
    five_of_a_kind = 6
    four_of_a_kind = 5
    full_house = 4
    three_of_a_kind = 3
    two_pair = 2
    one_pair = 1
    high_card = 0

@dataclass
class Hand:
    cards: List[str]
    card_count: Dict[str, int]
    bid: int
    hand_type: int

@dataclass
class HandP2:
    cards: List[str]
    card_count: Dict[str, int]
    bid: int
    hand_type: int
    num_jokers: int


@dataclass
class Game:
    hands: List[Hand]


def card_to_value(card: str) -> int:
    mapper ={
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14
    }
    c = mapper.get(card)
    return c if c else int(card)

def p2_card_to_value(card: str) -> int:
    mapper ={
        "J": 1,
        "T": 10,
        "Q": 11,
        "K": 12,
        "A": 13
    }
    c = mapper.get(card)
    return c if c else int(card)

def read_input(text) -> Game:
    g = Game(hands=[])
    for line in text:
        h = Hand(cards=[], bid=0, card_count={}, hand_type=0)
        str_line = str(line)
        cards, bid = str_line.split(" ")
        for card in cards:
            card = card.strip()
            if card:
                h.cards.append(card)
                if not h.card_count.get(card):
                    h.card_count[card] = 1
                else:
                    h.card_count[card] += 1
        h.bid = int(bid)
        g.hands.append(h)
    return g


def sort_hands(hands):
    return sorted(hands, key=lambda hand: (
        [card_to_value(card) for card in hand.cards]
    ))



def part_one(game: Game):
    for hand in game.hands:
        if len(hand.card_count) == 1:
            hand.hand_type = HandType.five_of_a_kind
        elif len(hand.card_count) == 2:
            if 4 in hand.card_count.values():
                hand.hand_type = HandType.four_of_a_kind
            else:
                hand.hand_type = HandType.full_house
        elif len(hand.card_count) == 3:
            if 3 in hand.card_count.values():
                hand.hand_type = HandType.three_of_a_kind
            else:
                hand.hand_type = HandType.two_pair
        elif len(hand.card_count) == 4:
            hand.hand_type = HandType.one_pair
        else:
            hand.hand_type = HandType.high_card

    # sort hands by hand type and card values
    new_hands = sorted(game.hands, key=lambda hand: (hand.hand_type, [card_to_value(card) for card in hand.cards]), reverse=False)

    # return the hand bid * position among all hands
    total = 0
    idx = 1
    for hand in new_hands:
        total += hand.bid * idx
        idx += 1
    return total

def part_two(game: Game):
    # same as part 1 but J is now a joker and has value 1
    for hand in game.hands:
        if len(hand.card_count) == 1:

    return 0

def main():
    e = read_input(example)
    e1 = part_one(e)
    print(e1)
    assert e1 == 6440
    print("example 1 passed")
    p1 = part_one(read_input(input_txt))
    print(p1)

    e2 = part_two(read_input(example))
    print(f"e2: {e2}")
    assert e2 == 5905

    p2 = part_two(read_input(input_txt))
    print(p2)


    return 0

if __name__ == "__main__":
    main()
