f = open("data/Day8-2015_Input")

lines = []

for w in f:
    lines.append(w.rstrip())

total_real = 0
total_memory = 0

for line in lines:
    original_line = line
    original_length = len(line)
    line = line.replace("\\\\", "aaaa")
    line = line.replace("\\\"", "aaaa")
    real_length = len(line) + 4
    number_hex = line.count("\\x")
    real_length += number_hex
    print(original_length, real_length)
    total_real += original_length
    total_memory += real_length

print(total_memory - total_real)