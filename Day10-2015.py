def do_thing(input):
    i = 0
    new_string = ""
    while i < len(input):
        current_char = input[i]
        j = i
        streak = 0
        while j < len(input):
            if input[j] == current_char:
                streak += 1
                if j == len(input) - 1:
                    new_string = new_string + str(streak) + current_char
            else:
                new_string = new_string + str(streak) + current_char
                i = j - 1
                break
            j += 1

        i += 1
    return new_string

input = "1113222113"
for i in range(50):
    print("Processing thing", i)
    input = do_thing(input)

print(len(input))