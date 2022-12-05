with open("input.txt") as f:
    lines = f.read().splitlines()

l = len(lines[0])

for index, l in enumerate(lines):
    if "1" in l:
        setup_index = index
        break

box_lines = lines[:setup_index]

# Split the input into lines and determine the number of columns in the matrix


num_cols = max(len(line.split()) for line in box_lines)

lists = [["" for i in range(num_cols)] for j in range(num_cols)]

for index, line in enumerate(box_lines):
    print(line)
    for i in range(1, num_cols * 4, 4):
        try:
            print(i, i // 4, line[i], index)
            lists[i // 4][index] = line[i]
        except:
            lists[index][i // 4] = ""

print(lists)

for l in lists:
    l.reverse()

print(lists)
lists = [list(filter(lambda s: s, lst)) for lst in lists]
lists = [list(filter(lambda s: s != " ", lst)) for lst in lists]

print(lists)


rules_start = setup_index + 2

for i in lines[rules_start:]:
    i = i.split()
    number = int(i[1])
    out = int(i[3]) - 1
    to = int(i[5]) - 1

    temp = lists[out][-1 * number :]
    print(temp)
    lists[out] = lists[out][: number * -1]
    lists[to].extend(temp)


final_list = []
for l in lists:
    final_list.append(l[-1])

print("".join(final_list))
