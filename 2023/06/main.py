from dataclasses import dataclass
from typing import List
# read example.txt

with open("example.txt") as f:
    example = f.read().splitlines()

# with open("example_p2.txt") as f:
#     example_p2 = f.read().splitlines()

with open("input.txt") as f:
    input_txt = f.read().splitlines()


@dataclass
class Race:
    distance: int
    speed_increase: int
    time: int
    winning_distances: List[int]

def parse_input(text):
    times = text[0]
    distances = text[1]

    times = [int(x) for x in text[0].split(":")[1].split(" ") if x.isdigit()]
    distances = [int(x) for x in text[1].split(":")[1].split(" ") if x.isdigit()]
    # [int(x) for x in line_one.split(":")[1].split(" ") if x.isdigit()]
    print(times, distances)
    hold_speed_increase = 1
    races = []
    for i in range(len(times)):
        races.append(Race(distance=distances[i], speed_increase=hold_speed_increase, time=times[i], winning_distances=[]))
    return races

def part_one(races: List[Race]):
    ways_to_win = 1
    for race in races:
        wins = 0
        for hold in range(race.time):
            # eg if hold = 3, we can do (time - hold)*hold distance
            distance_run = (race.time-hold)*hold*race.speed_increase
            if distance_run > race.distance:
                wins += 1
        print(wins)
        ways_to_win *= wins

    return ways_to_win

def parse_q2_input(text) -> Race:
    time = "".join([x for x in text[0].split(":")[1].split(" ") if x.isdigit()])
    distance = "".join([x for x in text[1].split(":")[1].split(" ") if x.isdigit()])

    return Race(distance=int(distance), speed_increase=1, time=int(time), winning_distances=[])



def part_two(race: Race):
    import cmath  # Complex math library

    # f = h^2 - t*h + d < 0
    d = race.distance
    t = race.time

    print(f"t = {t}")
    print(f"d = {d}")

    a = 1
    b = -t
    c = d

    # Calculating the discriminant
    discriminant = cmath.sqrt(b**2 - 4*a*c)

    # Calculating the two roots
    root1 = (-b + discriminant) / (2 * a)
    root2 = (-b - discriminant) / (2 * a)

    return int(root1.real) - int(root2.real)

def main():
    e_input = parse_input(example)
    p1_input = parse_input(input_txt)
    e1 = part_one(e_input)
    assert e1 == 288
    print(part_one(p1_input))

    e2_input = parse_q2_input(example)
    q2_input = parse_q2_input(input_txt)
    e2 = part_two(e2_input)
    print(e2)
    assert e2 == 71503
    print(part_two(q2_input))


if __name__ == "__main__":
    main()
