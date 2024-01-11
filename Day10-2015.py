def create_new_sequence(number_string):
    i = 0
    new_string = ""
    while i < len(number_string):
        current_char = number_string[i]
        j = i
        streak = 0
        while j < len(number_string):
            if number_string[j] == current_char:
                streak += 1
                if j == len(number_string) - 1:
                    new_string = new_string + str(streak) + current_char
            else:
                new_string = new_string + str(streak) + current_char
                i = j - 1
                break
            j += 1

        i += 1
    return new_string


puzzle_input = "1113222113"
for i in range(50):
    puzzle_input = create_new_sequence(puzzle_input)
    print(i, len(puzzle_input))
