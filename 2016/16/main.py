# https://adventofcode.com/2016/day/16


Q1_TEST_1 = ""
Q1_INPUT = "11110010111001001"


def dragon_process(curr: str) -> str:
    b = curr[::-1]

    flipped_b = ""
    for s in b:
        if s == "0":
            flipped_b += "1"
        else:
            flipped_b += "0"

    return curr + "0" + flipped_b


def checksum(curr: str) -> str:
    res = ""
    for i in range(len(curr) // 2):
        c = i * 2
        n = c + 1
        if curr[c] == curr[n]:
            res += "1"
        else:
            res += "0"

    return res


def p1(s: str, size: int) -> str:
    while len(s) < size:
        s = dragon_process(s)

    s = s[:size]
    cs = checksum(s)
    while len(cs) % 2 == 0:
        cs = checksum(cs)

    return cs


if __name__ == "__main__":
    assert dragon_process("1") == "100"
    assert dragon_process("111100001010") == "1111000010100101011110000"

    assert checksum("110010110100") == "110101"

    t1 = p1("10000", 20)
    assert t1 == "01100"

    a1 = p1(Q1_INPUT, 272)
    print(a1)

    a2 = p1(Q1_INPUT, 35651584)
    print(a2)
    print("Done")
