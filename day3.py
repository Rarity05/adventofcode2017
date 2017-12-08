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

while matrix[currentPosition] < input:
    currentDirection = directions[currentDirectionIndex]
    nextDirectionIndex = (currentDirectionIndex + 1) % 4
    nextDirection = directions[nextDirectionIndex]

    if addTuple(currentPosition, nextDirection) not in matrix:
        currentDirectionIndex = nextDirectionIndex
        currentDirection = nextDirection
    currentPosition = addTuple(currentPosition, currentDirection)

    indicies = [addTuple(currentPosition, coordinate) for coordinate in ranges]
    values = list(map(lambda x: matrix.get(x, 0), indicies))

    value = sum(values)
    matrix[currentPosition] = value

print("Part 2 result:", matrix[currentPosition])
