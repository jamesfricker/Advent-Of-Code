#  https://adventofcode.com/2016/day/6

from collections import defaultdict

INPUT_Q1 = "input.txt"
TEST_INPUT_Q1 = "test_input.txt"


def read_input(loc: str) -> list[str]:
    with open(loc) as f:
        data = f.read().splitlines()
    return data


def p1(data: list[str]) -> str:
    maxs = [defaultdict(int) for _ in range(len(data[0]))]

    max_counts = [(None, 0) for _ in range(len(data[0]))]

    for l in data:
        for i, c in enumerate(l):
            maxs[i][c] += 1
            r = maxs[i][c]
            if r >= max_counts[i][1]:
                max_counts[i] = (c, r)

    return "".join([v[0] for v in max_counts])


def p2(data: list[str]) -> str:
    # for each list, get the most frequent, append to result

    maxs = [defaultdict(int) for _ in range(len(data[0]))]

    for l in data:
        for i, c in enumerate(l):
            maxs[i][c] += 1

    res = ""
    for i, d in enumerate(maxs):
        m = (None, float("inf"))
        for k, v in d.items():
            if v < m[1]:
                m = (k, v)
        res += m[0]

    return res


if __name__ == "__main__":
    test = read_input(TEST_INPUT_Q1)
    t1 = p1(test)
    assert t1 == "easter"

    sol_q1 = read_input(INPUT_Q1)
    a1 = p1(sol_q1)
    print(a1)

    t2 = p2(test)
    # assert t2 == ""
    print(t2)
    a2 = p2(sol_q1)
    print(a2)
