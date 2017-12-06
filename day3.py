input = 347991
input = 347991

sector = 0
square = 1
while square**2 < input:
    sector += 1
    square += 2

max = square**2
target = max - square + 1
print(target, max, square)

while target > input:
    target -= (square - 1)
    max -= (square - 1)
print(target, "...", input, "...", max)

halfpoint = (max + target) // 2
print(halfpoint)

result = abs(input - halfpoint) + sector
print(result)
