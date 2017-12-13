input = open("inputs/day9.txt")
input = input.readline()

# gcd
indicies = []
startIndex = 0
inGarbage = False
shouldSkipNext = False

for i in range(len(input)):
    if shouldSkipNext:
        shouldSkipNext = False
        continue
    if input[i] == "!":
        shouldSkipNext = True
        continue

    if input[i] == "<" and not inGarbage:
        inGarbage = True
        startIndex = i
        continue

    if input[i] == ">" and inGarbage:
        inGarbage = False
        indicies.append((startIndex, i + 1))

filtered = input
for index in indicies:
    startIndex = index[0]
    endIndex = index[1]
    length = endIndex - startIndex
    filtered = filtered[:startIndex] + " "*length + filtered[endIndex:]
filtered = "".join(list(filter(lambda x: x != " " and x != ",", filtered)))

value = 0
summa = 0
for char in filtered:
    if char == "{":
        value += 1
        summa += value
    if char == "}":
        value -= 1

print("Part 1 result:", summa)

garbages = []
for index in indicies:
    startIndex = index[0]
    endIndex = index[1]
    garbages.append(input[startIndex+1:endIndex-1])

def counter(string):
    shouldSkipNext = False
    count = 0
    for i in range(len(string)):
        if shouldSkipNext:
            shouldSkipNext = False
            continue
        if string[i] == "!":
            shouldSkipNext = True
            continue
        count += 1
    return count

result = sum(list(map(counter, garbages)))
print("Part 2 result:", result)
