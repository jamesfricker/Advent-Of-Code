with open("input.txt") as f:
    lines = f.read().splitlines()

register = 1
cycle = 1
s = 0

register_values = [20, 60, 100, 140, 180, 220]

for line in lines:
    cmd = line.split()
    if cmd[0] == "noop":
        cycle += 1
        if cycle in register_values:
            s += register * cycle
    if cmd[0] == "addx":
        cycle += 2
        if cycle - 1 in register_values:
            s += register * (cycle - 1)
        v = cmd[1]
        register += int(v)
        if cycle in register_values:
            s += register * cycle


print(s)

## part 2

register = 1
cycle = 1
s = 0

images = [[] for i in range(7)]

image = []
for index, line in enumerate(lines):
    cmd = line.split()
    if cmd[0] == "noop":
        print(register, cycle)
        if (
            register == (cycle % 40) + 1
            or register == (cycle % 40)
            or register == (cycle % 40) - 1
        ):
            images[cycle // 40].append("#")
        else:
            images[cycle // 40].append(".")
        cycle += 1

    if cmd[0] == "addx":
        print(register, cycle)
        if (
            register == (cycle % 40) + 1
            or register == (cycle % 40)
            or register == (cycle % 40) - 1
        ):
            images[cycle // 40].append("#")
        else:
            images[cycle // 40].append(".")
        cycle += 1
        print(register, cycle)
        v = cmd[1]

        register += int(v)

        if (
            register == (cycle % 40) + 1
            or register == (cycle % 40)
            or register == (cycle % 40) - 1
        ):
            images[cycle // 40].append("#")
        else:
            images[cycle // 40].append(".")
        cycle += 1

    print(cycle, register, s)
    print(images[cycle // 40])

# the top line is wrong but the rest is correct, possible to still see the letters
# even if they aren't fully correct
for image in images:
    print(image)
