from itertools import combinations

bottles = []
total_amount = 150

f = open("data/Day17-2015_Input")

for w in f:
    n = int(w.rstrip())
    bottles.append(n)

storage_combinations = {}

total = 0
for i in range(len(bottles)):
    storage_combinations[str(i+1)] = 0
    for comb in combinations(bottles, i+1):
        if sum(comb) == total_amount:
            storage_combinations[str(len(comb))] += 1
            total += 1

print("Total number of combinations:", total)
for i in range(len(bottles)):
    if storage_combinations[str(i+1)] != 0:
        print("Minimum needed is:", str(i+1), "bottles")
        print("Amount of ways to store is:", storage_combinations[str(i+1)])
        break
