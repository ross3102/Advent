import math

class Node:
    def __init__(self, loc, size, used, avail, percent):
        loc = loc.split("/")
        loc = loc[3].split("-")[1:]
        self.x = int(loc[0][1:])
        self.y = int(loc[1][1:])
        self.size = int(size[:-1])
        self.used = int(used[:-1])
        self.avail = int(avail[:-1])
        self.percent = int(percent[:-1])

    def numfit(self):
        total = 0
        for node in nodes:
            if self.used < node.size:
                total += 1
        return total

    def adjacentTo(self, node):
        return abs(self.x - node.x) == 1 and abs(self.y - node.y == 1)

file = list(open("f", "r"))[2:]

nodes = []

for node in file:
    split = node.strip().split(" ")
    data = []
    for i in split:
        if i != "":
            data.append(i)
    nodes.append(Node(data[0], data[1], data[2], data[3], data[4]))

height = max([node.y for node in nodes]) + 1
length = max([node.x for node in nodes]) + 1

viable = 0

for nodea in nodes:
    for nodeb in nodes:
        if nodea != nodeb and nodea.adjacentTo(nodeb) and nodea.used != 0 and nodea.used < nodeb.avail:
            viable += 1
print(viable)
for node in nodes:
    numfit = node.numfit()
    if numfit < len(nodes):
        print(node.x, node.y)

