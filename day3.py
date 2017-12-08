input = 347991

# part 1
sector = 0
square = 1
while square**2 < input:
    sector += 1
    square += 2

max = square**2
target = max - square + 1

while target > input:
    target -= (square - 1)
    max -= (square - 1)

halfpoint = (max + target) // 2
result = abs(input - halfpoint) + sector
print("Part 1 result:", result)

# part 2
from operator import add

matrix = {(0, 0): 1, (0, 1): 1}
# right, up, left, down
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# want to go left
currentDirectionIndex = 1
currentPosition = (0, 1)

def addTuple(x, y):
    return tuple(map(add, x, y))

xs = [-1, 0, 1] * 3
ys = [-1] * 3 + [0] * 3 + [1] * 3
ranges = list(zip(xs, ys))

while True:
    currentDirection = directions[currentDirectionIndex]
    nextDirection = directions[(currentDirectionIndex + 1) % 4]

    if addTuple(currentPosition, nextDirection) not in matrix:
        currentDirectionIndex = (currentDirectionIndex + 1) % 4
        currentDirection = nextDirection
    currentPosition = addTuple(currentPosition, currentDirection)

    value = 0
    for coordinate in ranges:
        index = addTuple(currentPosition, coordinate)
        value += matrix.get(index, 0)
    matrix[currentPosition] = value

    if value > input:
        print("Part 2 result:", value)
        break
