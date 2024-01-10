f = open("data/Day3-2015_Input")

for w in f:
    directions = w.rstrip()

santa_delivery_map = {}
robot_delivery_map = {}
santa_r = 0
santa_c = 0
robot_r = 0
robot_c = 0
santa_delivery_map[(santa_r, santa_c)] = 1

counter = 0
for d in directions:

    if counter % 2 == 0:
        if d == ">":
            santa_c += 1
        if d == "<":
            santa_c -= 1
        if d == "^":
            santa_r += 1
        if d == "v":
            santa_r -= 1

        if (santa_r, santa_c) in santa_delivery_map.keys():
            santa_delivery_map[(santa_r, santa_c)] += 1
        else:
            santa_delivery_map[(santa_r, santa_c)] = 1

    else:
        if d == ">":
            robot_c += 1
        if d == "<":
            robot_c -= 1
        if d == "^":
            robot_r += 1
        if d == "v":
            robot_r -= 1

        if (robot_r, robot_c) in robot_delivery_map.keys():
            robot_delivery_map[(robot_r, robot_c)] += 1
        else:
            robot_delivery_map[(robot_r, robot_c)] = 1
    counter += 1

all_locations = []

for k in santa_delivery_map.keys():
    all_locations.append(k)

for k in robot_delivery_map.keys():
    if not k in all_locations:
        all_locations.append(k)

print(len(all_locations))
