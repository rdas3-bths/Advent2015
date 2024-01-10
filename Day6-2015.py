lights = []

for i in range(1000):
    row = []
    for j in range(1000):
        row.append(0)
    lights.append(row)

f = open("data/Day6-2015_Input", "r")
lines = []
for w in f:
    lines.append(w.rstrip())

for instruction in lines:
    instruction = instruction.split(" ")
    if instruction[0] == "toggle":
        instruction.insert(1, "toggle")

    start_row = int(instruction[2].split(",")[0])
    start_column = int(instruction[2].split(",")[1])

    end_row = int(instruction[4].split(",")[0])
    end_column = int(instruction[4].split(",")[1])

    action = instruction[1]

    current_row = start_row
    row_counter = start_row + (end_row - start_row)
    current_column = start_column
    column_counter = start_column + (end_column - start_column)

    while (current_row <= row_counter):
        current_column = start_column
        while (current_column <= column_counter):
            if action == "on":
                lights[current_row][current_column] += 1
            if action == "off":
                lights[current_row][current_column] -= 1
                if lights[current_row][current_column] < 0:
                    lights[current_row][current_column] = 0
            if action == "toggle":
                lights[current_row][current_column] += 2
            current_column += 1
        current_row += 1

count = 0
for i in range(len(lights)):
    for j in range(len(lights[0])):
        count += lights[i][j]

print(count)