f = open("data/Day1-2015_Input")

lines = []
for w in f:
    lines.append(w.rstrip())


for input in lines:
    counter = 0
    position = 1
    for char in input:
        if char == '(':
            counter += 1
        if char == ')':
            counter -= 1
        if counter == -1:
            print(position)
        position += 1
    print(counter)