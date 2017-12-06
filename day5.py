input = open("inputs/day5.txt")
_numbers = []
for line in input:
    _numbers.append(int(line))
length = len(_numbers)

# part 1
numbers = list(_numbers)
index = 0
steps = 0
while True:
    if index < 0 or index >= length:
        break
    newIndex = numbers[index]
    numbers[index] += 1
    index += newIndex
    steps += 1

print("Part 1 result:", steps)

# part 2
numbers = list(_numbers)
index = 0
steps = 0
while True:
    if index < 0 or index >= length:
        break
    newIndex = numbers[index]
    if newIndex >= 3:
        numbers[index] -= 1
    else:
        numbers[index] += 1
    # numbers[index] += -1 if newIndex >= 3 else 1
    index += newIndex
    steps += 1

print("Part 2 result:", steps)
