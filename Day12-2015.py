import json

def traverse_list(process_list, numbers):
    for item in process_list:
        if isinstance(item, (int)):
            numbers.append(item)
        if isinstance(item, (list)):
            traverse_list(item, numbers)
        if isinstance(item, (dict)):
            traverse_dict(item, numbers)


def traverse_dict(process_dict, numbers):

    for key in process_dict.keys():
        if process_dict[key] == "red":
            return

    for key in process_dict.keys():
        item = process_dict[key]
        if isinstance(item, (int)):
            numbers.append(item)
        if isinstance(item, (list)):
            traverse_list(item, numbers)
        if isinstance(item, (dict)):
            traverse_dict(item, numbers)

f = open("data/Day12-2015_Input")
lines = []

for w in f:
    lines.append(w.rstrip())


data = lines[0]
data_json = json.loads(data)

numbers = []

if isinstance(data_json, (dict)):
    traverse_dict(data_json, numbers)
if isinstance(data_json, (list)):
    traverse_list(data_json, numbers)


print(sum(numbers))