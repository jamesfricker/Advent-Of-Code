with open("input.txt") as f:
    lines = f.read().splitlines()

trees = []

for line in lines:
    row = []
    for t in line:
        row.append(int(t))
    trees.append(row)


visibility = [[0 for i in t] for t in trees]

for index, row in enumerate(trees):
    left_max = row[0]
    right_max = row[-1]
    top_max = trees[0][index]
    bottom_max = trees[-1][index]
    visibility[0][index] = 1
    visibility[-1][index] = 1
    visibility[index][0] = 1
    visibility[index][-1] = 1

    for i in range(1, len(row) - 1):
        r = len(row) - 1 - i
        # left
        if row[i] > left_max:
            left_max = row[i]
            visibility[index][i] = 1
        # right
        if row[r] > right_max:
            right_max = row[r]
            visibility[index][r] = 1
        # top
        if trees[i][index] > top_max:
            top_max = trees[i][index]
            visibility[i][index] = 1
        # bottom
        if trees[r][index] > bottom_max:
            bottom_max = trees[r][index]
            visibility[r][index] = 1

print(sum([sum(i) for i in visibility]))
# part 1
# 1816

## part 2

scenic = [[0 for i in t] for t in trees]

for index, row in enumerate(trees):
    for i in range(1, len(row) - 1):
        left, right, up, down = 0, 0, 0, 0

        for left_index in range(i - 1, -1, -1):
            left += 1
            if trees[index][left_index] >= row[i]:
                break
        for right_index in range(i + 1, len(row)):
            right += 1
            if trees[index][right_index] >= row[i]:
                break

        for down_index in range(index + 1, len(row)):
            down += 1
            if trees[down_index][i] >= row[i]:
                break

        for up_index in range(index - 1, -1, -1):
            up += 1
            if trees[up_index][i] >= row[i]:
                break

        scenic[index][i] = left * right * up * down

print(max([max(i) for i in scenic]))


# correct is
# 383520
