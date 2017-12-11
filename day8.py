input = open("inputs/day8.txt")

registers = {}
highest = 0
for line in input:
    line = line.split()

    register = line[0]
    conditionRegister = line[4]
    if register not in registers:
        registers[register] = 0
    if conditionRegister not in registers:
        registers[conditionRegister] = 0

    sign = 1 if line[1] == "inc" else -1
    command = "{}{}{}".format(registers[conditionRegister], line[5], int(line[6]))
    condition = eval(command)
    if condition:
        registers[register] += sign * int(line[2])
        if registers[register] > highest:
            highest = registers[register]

maxKey = max(registers, key=registers.get)
print("Part 1 result:", registers[maxKey])
print("Part 2 result:", highest)
