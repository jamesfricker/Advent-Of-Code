from dataclasses import dataclass

with open("example.txt") as f:
    example = f.read().splitlines()

# with open("example_p2.txt") as f:
#     example_p2 = f.read().splitlines()

with open("input.txt") as f:
    input_txt = f.read().splitlines()


@dataclass
class Game:
    red: int
    blue: int
    green: int


@dataclass
class GameSet:
    number: int
    Games: [Game]


def parse_lines(text) -> [GameSet]:
    games_sets: [GameSet] = []
    for line in text:
        # convert line to str
        str_line = str(line)
        game_number = int(str_line.split(":")[0].split(" ")[1])
        g = GameSet(number=game_number, Games=[])

        games_list = str_line.split(":")[1].split(";")
        for game_list in games_list:
            game_list = game_list.strip()
            numbers = game_list.split(",")
            game = Game(red=0, blue=0, green=0)
            for num in numbers:
                num = num.strip()
                count = num.split(" ")[0]
                t = num.split(" ")[1]
                if t == "red":
                    game.red = int(count)
                elif t == "blue":
                    game.blue = int(count)
                elif t == "green":
                    game.green = int(count)
            g.Games.append(game)
        games_sets.append(g)

    return games_sets


def part_one(games: [GameSet]):
    max_red = 12
    max_green = 13
    max_blue = 14

    sum_valid_games_ids = 0
    for game in games:
        game_set_is_valid = True
        for g in game.Games:
            if g.red > max_red or g.green > max_green or g.blue > max_blue:
                game_set_is_valid = False
        if game_set_is_valid:
            sum_valid_games_ids += game.number
    return sum_valid_games_ids


def part_two(games: [GameSet]):
    # its like part 1, but we calculate the max valid
    # and return the sum of products of the maximums
    sum_game_products = 0
    for game in games:
        max_red = -1
        max_blue = -1
        max_green = -1
        for g in game.Games:
            if g.red > max_red:
                max_red = g.red
            if g.green > max_green:
                max_green = g.green
            if g.blue > max_blue:
                max_blue = g.blue
        product = max_red * max_green * max_blue
        sum_game_products += product
    return sum_game_products


def main():
    example_game = parse_lines(example)

    e1 = part_one(example_game)
    print(e1)
    assert e1 == 8

    games = parse_lines(input_txt)
    p1 = part_one(games)
    print(p1)

    e2 = part_two(example_game)
    print(e2)
    assert e2 == 2286

    p2 = part_two(games)
    print(p2)


if __name__ == "__main__":
    main()
