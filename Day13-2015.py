from itertools import permutations

def get_happiness_change(person, neighbor, happiness_map):
    for key in happiness_map:
        if key[0] == person and key[1] == neighbor:
            return happiness_map[key]
    return 0

f = open("data/Day13-2015_Input")

lines = []

for w in f:
    lines.append(w.rstrip())

first_name = lines[0].split(" ")[0]
original_name_list = [ first_name ]
happiness_map = {}

for line in lines:
    data = line.split(" ")
    if data[0] == first_name:
        original_name_list.append(data[len(data)-1].replace(".", ""))

    person = data[0]
    neighbor = data[len(data)-1].replace(".", "")
    change = int(data[3])
    if data[2] == "lose":
        change = change * -1

    happiness_map[(person, neighbor)] = change

# part 2
for person in original_name_list:
    happiness_map[person, 'me'] = 0
    happiness_map['me', person] = 0

original_name_list.append('me')


happiness_numbers = []
for all_names in permutations(original_name_list):

    total_happiness = 0
    for i in range(len(all_names)):
        person = all_names[i]
        to_right = i+1
        to_left = i-1
        if to_right == len(all_names):
            to_right = 0
        if to_left == -1:
            to_left = len(all_names)-1
        neighbor1 = all_names[to_right]
        neighbor2 = all_names[to_left]
        happiness_change1 = get_happiness_change(person, neighbor1, happiness_map)
        happiness_change2 = get_happiness_change(person, neighbor2, happiness_map)
        total_happiness += happiness_change1
        total_happiness += happiness_change2

    happiness_numbers.append(total_happiness)

print(max(happiness_numbers))


