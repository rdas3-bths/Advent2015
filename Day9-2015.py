from itertools import permutations

f = open("data/Day9-2015_Input")
lines = []
for w in f:
    lines.append(w.rstrip())

nodes_parse = []
one_way_distances = []
distances_parse = {}
for line in lines:
    data = line.split()
    nodes_parse.append(data[0])
    nodes_parse.append(data[2])
    one_way_distance = {}
    one_way_distance[(data[0], data[2])] = int(data[4])
    one_way_distances.append(one_way_distance)

nodes = set(nodes_parse)
for node in nodes:
    distances_parse[node] = {}

for one_way in one_way_distances:
    location_one = ""
    location_two = ""
    distance = -1
    for k in one_way.keys():
        location_one = k[0]
        location_two = k[1]
        distance = one_way[k]
    distances_parse[location_one][location_two] = distance
    distances_parse[location_two][location_one] = distance

distances = distances_parse
total_distances = []
for items in permutations(nodes):
    total = 0
    for i in range(len(items)-1):
        total += distances[items[i]][items[i+1]]
    total_distances.append(total)

print("Min distance:", min(total_distances))
print("Max distance:", max(total_distances))
