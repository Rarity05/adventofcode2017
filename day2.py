# input
file = open("inputs/day2.txt")
input = []
for line in file:
    numbers = line.split()
    numbers = list(map(int, numbers))
    input.append(sorted(numbers, reverse = True))

# part 1
result = sum(list(map(lambda x: max(x) - min(x), input)))
print(result)

# part 2
def genRange(max):
    return [(i, j) for i in range(max) for j in range(i, max) if i != j]

result = sum(list(map(lambda x: [x[i] // x[j] for i, j in genRange(len(x)) if x[i] % x[j] == 0][0], input)))
print(result)
