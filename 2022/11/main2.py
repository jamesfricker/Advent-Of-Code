with open("input.txt") as f:
    lines = f.read().splitlines()


# get input
monkey_curr = []
monkey_div_by = []
monkey_send_to = []
for n in range(0, len(lines), 7):
    monkey_num = int(lines[n].split()[1][0])
    monkey_items = lines[n + 1].split(":")[1].split(",")
    monkey_items = list(map(int, monkey_items))
    monkey_curr.append(monkey_items)
    monkey_div = int(lines[n + 3].split()[-1])
    monkey_div_by.append(monkey_div)
    monkey_send_true = int(lines[n + 4].split()[-1])
    monkey_send_false = int(lines[n + 5].split()[-1])
    monkey_send_to.append([monkey_send_true, monkey_send_false])
    print(monkey_num)
    print(monkey_items)
    print(monkey_div)


def f1(old):
    return old * 5


def f2(old):
    return old + 6


def f3(old):
    return old + 5


def f4(old):
    return old + 2


def f5(old):
    return old * 7


def f6(old):
    return old + 7


def f7(old):
    return old + 1


def f8(old):
    return old * old


def t1(old):
    return old * 19


def t2(old):
    return old + 6


def t3(old):
    return old * old


def t4(old):
    return old + 3


monkey_functions = [f1, f2, f3, f4, f5, f6, f7, f8]
# monkey_functions = [t1, t2, t3, t4]

inspections = [0 for i in monkey_curr]

p = 1
for i in monkey_div_by:
    p *= i

for r in range(0, 10000):
    for m in range(len(monkey_curr)):
        new_curr = []
        for item in monkey_curr[m]:
            # print(f"ITEM: {item}")
            worry = monkey_functions[m](item)
            worry = worry % p
            inspections[m] += 1
            # print(f"WORRY: {worry}")
            if worry % monkey_div_by[m] == 0:
                # print(f"PASSED TO: {monkey_send_to[m][0]}")
                monkey_curr[monkey_send_to[m][0]].append(worry)
                if monkey_send_to[m][0] == m:
                    new_curr.append(worry)
            else:
                # print(f"PASSED TO: {monkey_send_to[m][1]}")
                monkey_curr[monkey_send_to[m][1]].append(worry)
                if monkey_send_to[m][1] == m:
                    new_curr.append(worry)
        monkey_curr[m] = new_curr

inspections = sorted(inspections)
print(inspections[-1] * inspections[-2])
