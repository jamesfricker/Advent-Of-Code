with open("input.txt") as f:
    lines = f.read().splitlines()

head_pos = [0, 0]
tail_pos = [0, 0]
tail_history = set()

for line in lines:
    cmd = line.split()
    d = cmd[0]
    for m in range(int(cmd[1])):
        if d == "U":
            head_pos[1] += 1
        elif d == "D":
            head_pos[1] -= 1
        elif d == "L":
            head_pos[0] -= 1
        else:
            head_pos[0] += 1
        if (
            head_pos[0] != tail_pos[0]
            and head_pos[1] != tail_pos[1]
            and (
                abs(head_pos[0] - tail_pos[0]) > 1 or abs(head_pos[1] - tail_pos[1]) > 1
            )
        ):
            if head_pos[0] > tail_pos[0]:
                tail_pos[0] += 1
            else:
                tail_pos[0] -= 1
            if head_pos[1] > tail_pos[1]:
                tail_pos[1] += 1
            else:
                tail_pos[1] -= 1
        elif abs(head_pos[0] - tail_pos[0]) > 1:
            if head_pos[0] > tail_pos[0]:
                tail_pos[0] += 1
            else:
                tail_pos[0] -= 1
        elif abs(head_pos[1] - tail_pos[1]) > 1:
            if head_pos[1] > tail_pos[1]:
                tail_pos[1] += 1
            else:
                tail_pos[1] -= 1

        print(head_pos, tail_pos)
        tail_history.add((tail_pos[0], tail_pos[1]))

print(tail_history)
print(len(tail_history))

# 5981

## part 2
rope = [[0, 0] for _ in range(10)]
p9_history = set()
for line in lines:
    cmd = line.split()
    d = cmd[0]
    m = int(cmd[1])
    for _ in range(m):

        if d == "U":
            rope[0][1] += 1
        elif d == "D":
            rope[0][1] -= 1
        elif d == "L":
            rope[0][0] -= 1
        else:
            rope[0][0] += 1

        for i in range(1, len(rope)):
            nextx, nexty = rope[i - 1]
            curra, currb = rope[i]
            if (
                nextx != curra
                and nexty != currb
                and (abs(nextx - curra) > 1 or abs(nexty - currb) > 1)
            ):
                if nextx > curra:
                    curra += 1
                else:
                    curra -= 1
                if nexty > currb:
                    currb += 1
                else:
                    currb -= 1
            elif abs(nextx - curra) > 1:
                if nextx > curra:
                    curra += 1
                else:
                    curra -= 1
            elif abs(nexty - currb) > 1:
                if nexty > currb:
                    currb += 1
                else:
                    currb -= 1
            rope[i] = [curra, currb]
            if i == 9:
                p9_history.add((curra, currb))
print(len(p9_history))
