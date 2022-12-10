with open("input.txt") as f:
    lines = f.read().splitlines()


text = lines[0]

window = text[:4]

index = -1
uniq = len(set(window))


for i in range(4, len(text)):
    uniq = len(set(window))
    if uniq == len(window):
        index = i
        break
    window = window[1:4]
    window += text[i]

print(index)

# test solution is 7
# test_2 solution is 11

# test_3 is 
