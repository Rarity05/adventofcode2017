from operator import itemgetter
numbers = [11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11]
length = len(numbers)

# part 1
history = ["".join(map(str, numbers))]
steps = 0
while True:
    maxElem = max(enumerate(numbers), key = itemgetter(1))
    maxIndex = maxElem[0]
    maxValue = maxElem[1]
    numbers[maxIndex] = 0
    for i in range(maxValue):
        numbers[(maxIndex + i + 1) % length] += 1

    newHistory = "".join(map(str, numbers))
    steps += 1
    if newHistory in history:
        break
    history.append(newHistory)

print("Part 1 result:", steps)

# part 2
numbers = [11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11]
length = len(numbers)

history = ["".join(map(str, numbers))]
steps = 0
loopfound = False
loopHistory = ""
while True:
    maxElem = max(enumerate(numbers), key = itemgetter(1))
    maxIndex = maxElem[0]
    maxValue = maxElem[1]
    numbers[maxIndex] = 0
    for i in range(maxValue):
        numbers[(maxIndex + i + 1) % length] += 1

    newHistory = "".join(map(str, numbers))
    if not loopfound:
        if newHistory in history:
            loopfound = True
            loopHistory = newHistory
        else:
            history.append(newHistory)
    else:
        steps += 1
        if loopHistory == newHistory:
            break

print("Part 1 result:", steps)
