reindeers = []
points = {}

f = open("data/Day14-2015_Input")
race_distance = 2503
race_tracking = {}
for i in range(race_distance):
    race_tracking[str(i+1)] = []

for w in f:
    line = w.rstrip()
    data = line.split(" ")
    name = data[0]
    change = int(data[3])
    rest_interval = int(data[6])
    rest_length = int(data[13])
    reindeer = {}
    reindeer["name"] = name
    points[name] = 0
    reindeer["change"] = change
    reindeer["rest_interval"] = rest_interval
    reindeer["rest_length"] = rest_length
    reindeers.append(reindeer)

results = []

for reindeer in reindeers:
    name = reindeer["name"]
    change = reindeer["change"]
    rest_interval = reindeer["rest_interval"]
    rest_length = reindeer["rest_length"]
    resting = False

    distance = 0
    moved = 0
    rest_length_counter = 0
    for second in range(race_distance):

        if not resting:
            distance += change
            moved += 1

        if resting:
            rest_length_counter += 1

        if moved == rest_interval:
            resting = True


        if rest_length_counter == rest_length:
            resting = False
            rest_length_counter = 0
            moved = 0

        race_tracking[str(second+1)].append((name, distance))

    results.append((name, distance))

for second_info in race_tracking.keys():
    second_data = race_tracking[second_info]
    times = []
    for item in second_data:
        times.append(item[1])
    max_time = max(times)

    for item in second_data:
        if item[1] == max_time:
            name = item[0]
            points[name] += 1

max = 0
max_name = ""

print(points)

for result in results:
    name = result[0]
    distance = result[1]
    if distance > max:
        max = distance
        max_name = name

print(max_name, max)