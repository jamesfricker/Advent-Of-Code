# https://adventofcode.com/2022/day/1

with open("input.txt") as f:
    lines = f.read().splitlines()

print(lines)

import functools

lines = [0 if x == "" else x for x in lines]
print(lines)

lines = list(map(int, lines))
print(lines)
# print(functools.reduce(lambda a, b: a+b if b != 0 and a!=0 else 0, lines))

count = 0
max_count = -1
for index, num in enumerate(lines):
    if num == 0:
        count = 0
    else:
        count += num
    if count > max_count:
        max_count = count

print(f"P1 Solution: {max_count}")

import bisect

# bisect.insort(list, n)

max_count = -1
counts = []
count = 0
for index, num in enumerate(lines):
    if num == 0:
        bisect.insort(counts, count)
        count = 0
    else:
        count += num

print(counts[-3:])
print(sum(counts[-3:]))
