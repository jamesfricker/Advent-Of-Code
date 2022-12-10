with open("input.txt") as f:
    lines = f.read().splitlines()


text = lines[0]

window = text[:14]

index = -1
uniq = len(set(window))


for i in range(14, len(text)):
    uniq = len(set(window))
    if uniq == len(window):
        index = i
        break
    window = window[1:14]
    window += text[i]

# test_3 is 29
print(index)
