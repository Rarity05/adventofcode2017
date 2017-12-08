from functools import reduce
from collections import Counter
from operator import itemgetter

input = open("inputs/day7.txt")
nodes = []

class Node:
    def __init__(self, name, weight, children = []):
        self.name = name
        self.weight = weight
        self.nodes = children

    def __str__(self):
        return "{} ({}), children: {}".format(self.name, self.weight, self.nodes)
    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.name == other.name
    def __hash__(self):
        return hash(self.name)

def nodeForName(name):
    for node in nodes:
        if node.name == name:
            return node



for line in input:
    line = line.split()
    name = line[0]
    weight = int(line[1][1:-1])
    if len(line) > 2:
        children = "".join(line[3:]).split(",")
    else:
        children = []
    nodes.append(Node(name, weight, children))
for node in nodes:
    node.nodes = list(map(nodeForName, node.nodes))

# part 1
parents = set(filter(lambda x: len(x.nodes) > 0, nodes))
children = set(reduce(lambda x, y: x + y.nodes, nodes, []))
parent = (parents - children).pop()
print("Part 1 result:", parent.name)

# part 2
def sumWeights(node):
    result = node.weight
    result += sum(list(map(sumWeights, node.nodes)))
    return result


currentNode = parent
# while True:
subWeights = []
for child in currentNode.nodes:
    subWeights.append((child, sumWeights(child)))

tmpWeigt = subWeights[]

if len(set(map(lambda x: sumWeights(x[0]), subWeights))) == 1:
    pass

for s in subWeights:
    print(s[0].name, s[0].weight, s[1])
#
# tmp = list(subWeights)
# leastCommonNode, leastCommonWeight = min(Counter(tmp).most_common(2), key = itemgetter(1))[0]
# tmp = list(subWeights)
# mostCommonNode, mostCommonWeight = max(Counter(tmp).most_common(5), key = itemgetter(1))[0]
# # node = diff[0]
# # weight = diff[1]
# print(leastCommonNode.name, leastCommonNode.weight, leastCommonWeight)
# print(mostCommonNode.name, mostCommonNode.weight, mostCommonWeight)
