def calculate_area(dimensions):
    length = dimensions[0]
    width = dimensions[1]
    height = dimensions[2]
    total = (2 * length * width) + (2 * width * height) + (2 * height * length)
    min_side = min(length * width, width * height, length * height)
    return total + min_side

def calculate_ribbon(dimensions):
    length = dimensions[0]
    width = dimensions[1]
    height = dimensions[2]
    min_perimter = min(length + length + width + width, width + width + height + height, length + length + height + height)
    return min_perimter + (length * width * height)

f = open("data/Day2-2015_Input")

lines = []
for w in f:
    lines.append(w.rstrip())

total = 0
for line in lines:
    d = line.split("x")
    dimensions = (int(d[0]), int(d[1]), int(d[2]))
    #total += calculate_area(dimensions)
    total += calculate_ribbon(dimensions)
print(total)