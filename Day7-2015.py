import struct

f = open("data/Day7-2015_Input", "r")

lines = []

for w in f:
    lines.append(w.rstrip())

circuit_map = {}

i = 0
while len(lines) != 0:
    instructions = lines[i].split(" ")
    destination = instructions[len(instructions)-1]
    operation = ""
    operand_one = ""
    operand_two = ""
    if instructions[0] == "NOT":
        operation = "NOT"
        operand_one = instructions[1]
        if operand_one in circuit_map.keys():
            number = ~circuit_map[operand_one]
            number = struct.unpack('H', struct.pack('h', number))[0]
            circuit_map[destination] = number
            lines.pop(i)
            i = 0
            continue
    elif instructions[0].isdigit() and instructions[1] == "->":
        print("Set", destination, instructions[0])
        circuit_map[destination] = int(instructions[0])
        lines.pop(i)
        i = 0
        continue
    elif instructions[1] == "->":
        if instructions[0] in circuit_map.keys():
            circuit_map[instructions[2]] = circuit_map[instructions[0]]
            lines.pop(i)
            i = 0
            continue
    else:
        operation = instructions[1]
        operand_one = instructions[0]
        operand_two = instructions[2]

        if operation == "AND":

            if operand_one == "1" and operand_two in circuit_map.keys():
                number = 1 & circuit_map[operand_two]
                circuit_map[destination] = number
                lines.pop(i)
                i = 0
                continue
            if operand_one in circuit_map.keys() and operand_two in circuit_map.keys():
                number = circuit_map[operand_one] & circuit_map[operand_two]
                #number = struct.unpack('H', struct.pack('h', number))[0]
                circuit_map[destination] = number
                lines.pop(i)
                i = 0
                continue
        if operation == "OR":
            if operand_one in circuit_map.keys() and operand_two in circuit_map.keys():
                number = circuit_map[operand_one] | circuit_map[operand_two]
                #number = struct.unpack('H', struct.pack('h', number))[0]
                circuit_map[destination] = number
                lines.pop(i)
                i = 0
                continue
        if operation == "LSHIFT":
            if operand_one in circuit_map.keys():
                number = circuit_map[operand_one] << int(operand_two)
                #number = struct.unpack('H', struct.pack('h', number))[0]
                circuit_map[destination] = number
                lines.pop(i)
                i = 0
                continue
        if operation == "RSHIFT":
            if operand_one in circuit_map.keys():
                number = circuit_map[operand_one] >> int(operand_two)
                #number = struct.unpack('H', struct.pack('h', number))[0]
                circuit_map[destination] = number
                lines.pop(i)
                i = 0
                continue

    i += 1

print(circuit_map["a"])


