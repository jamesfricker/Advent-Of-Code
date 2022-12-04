with open("input.txt") as f:
    lines = f.read().splitlines()

count = 0
for l in lines:

    p1 = l.split(",")[0]
    p2 = l.split(",")[1]
    low_1 = int(p1.split("-")[0])
    high_1 = int(p1.split("-")[1])
    low_2 = int(p2.split("-")[0])
    high_2 = int(p2.split("-")[1])

    if low_2 <= low_1 and high_2 >= high_1:
        count += 1
    elif low_1 <= low_2 and high_1 >= high_2:
        count += 1

print(count)

# part 2

count = 0
for l in lines:

    p1 = l.split(",")[0]
    p2 = l.split(",")[1]
    low_1 = int(p1.split("-")[0])
    high_1 = int(p1.split("-")[1])
    low_2 = int(p2.split("-")[0])
    high_2 = int(p2.split("-")[1])

    if low_1 <= low_2 <= high_1:
        count += 1
    elif low_2 <= low_1 <= high_2:
        count += 1

print(count)
