def count_vowels(input):
    count = 0
    for c in input:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            count += 1
    if count >= 3:
        return True
    else:
        return False

def back_to_back_letters(input):
    i = 0
    while i < len(input) - 1:
        first = input[i]
        second = input[i+1]
        if first == second:
            return True
        i += 1
    return False

def check_invalid_strings(input):
    check1 = input.find("ab")
    check2 = input.find("cd")
    check3 = input.find("pq")
    check4 = input.find("xy")
    if check1 == -1 and check2 == -1 and check3 == -1 and check4 == -1:
        return True
    return False

def check_duplicate_pair(input):
    i = 0
    pairs = []
    while i <= len(input) - 2:
        sub = input[i:i+2]
        pairs.append(sub)
        i += 1

    i = 0
    while i < len(pairs) - 1:
        first = pairs[i]
        second = pairs[i+1]
        if first == second:
            pairs.pop(i)
        i += 1

    pair_map = {}

    for pair in pairs:
        if pair in pair_map.keys():
            return True
        else:
            pair_map[pair] = 1

    return False

def check_triple_letter_pattern(input):
    i = 0
    while i < len(input) - 2:
        sub = input[i:i+3]
        if sub[0] == sub[2]:
            return True
        i += 1
    return False


lines = []
f = open("data/Day5-2015")
for w in f:
    lines.append(w.rstrip())

nice = 0
for input in lines:
    check1 = check_duplicate_pair(input)
    check2 = check_triple_letter_pattern(input)

    if check1 and check2:
        print(input)
        nice += 1

print(nice)
