f = open("data/Day16-2015_Input")
lines = []
sues = []

for i in range(500):
    sue = {}
    sue["number"] = (i+1)
    sue["children"] = -1
    sue["cats"] = -1
    sue["samoyeds"] = -1
    sue["pomeranians"] = -1
    sue["akitas"] = -1
    sue["vizslas"] = -1
    sue["goldfish"] = -1
    sue["trees"] = -1
    sue["cars"] = -1
    sue["perfumes"] = -1
    sue["eliminated"] = False
    sues.append(sue)

for w in f:
    lines.append(w.rstrip())

for line in lines:
    sue_number = int(line.split(" ")[1][0:-1])
    data = line.split(" ")
    colon = line.find(":")
    data = line[colon+2:].rstrip()
    sue_attr = data.split(",")
    for attr in sue_attr:
        attr_data = attr.split(":")
        attr_key = attr_data[0].strip()
        attr_value = int(attr_data[1].rstrip())
        sue_to_update = sues[sue_number-1]
        sue_to_update[attr_key] = attr_value

for sue in sues:
    if sue["children"] != -1 and sue["children"] != 3:
        sue["eliminated"] = True
    if sue["cats"] != -1 and sue["cats"] <= 7:
        sue["eliminated"] = True
    if sue["samoyeds"] != -1 and sue["samoyeds"] != 2:
        sue["eliminated"] = True
    if sue["pomeranians"] != -1 and sue["pomeranians"] >= 3:
        sue["eliminated"] = True
    if sue["akitas"] != -1 and sue["akitas"] != 0:
        sue["eliminated"] = True
    if sue["vizslas"] != -1 and sue["vizslas"] != 0:
        sue["eliminated"] = True
    if sue["goldfish"] != -1 and sue["goldfish"] >= 5:
        sue["eliminated"] = True
    if sue["trees"] != -1 and sue["trees"] <= 3:
        sue["eliminated"] = True
    if sue["cars"] != -1 and sue["cars"] != 2:
        sue["eliminated"] = True
    if sue["perfumes"] != -1 and sue["perfumes"] != 1:
        sue["eliminated"] = True

for sue in sues:
    if sue["eliminated"] == False:
        print(sue)