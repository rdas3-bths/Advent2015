def convert_to_password_string(integer_list):
    password = ""
    for number in integer_list:
        number = number+96
        password += chr(number)
    return password


def check_for_three_sequence(integer_list):
    for i in range(len(integer_list)-2):
        if integer_list[i] == integer_list[i+1]-1 == integer_list[i+2]-2:
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
            pair_map[pair] += 1
        else:
            pair_map[pair] = 1

    return pair_map


def check_multiple_duplicate_pair(password):
    count = 0
    pair_map = check_duplicate_pair(password)
    for key in pair_map.keys():
        if key[0] == key[1]:
            count += 1

    if count > 1:
        return True
    else:
        return False


def check_all_valid_letters(password):
    for character in password:
        if character == 'i' or character == 'o' or character == 'l':
            return False
    return True


def increment_integer_list(integer_list, current_index):
    if current_index == 0:
        if integer_list[current_index] == 26:
            return
        else:
            integer_list[current_index] += 1
            return
    else:
        if integer_list[current_index] != 26:
            integer_list[current_index] += 1
            return
        else:
            integer_list[current_index] = 1
            increment_integer_list(integer_list, current_index-1)

password = "ghijklmn"

password_integer = []
for character in password:
    integer_value = ord(character)-96
    password_integer.append(integer_value)

while True:
    check1 = check_for_three_sequence(password_integer)
    check2 = check_multiple_duplicate_pair(password)
    check3 = check_all_valid_letters(password)
    if check1 and check2 and check3:
        print(password, check1, check2, check3)
        break
    else:
        print(password, check1, check2, check3)
        increment_integer_list(password_integer, len(password_integer)-1)
        password = convert_to_password_string(password_integer)
