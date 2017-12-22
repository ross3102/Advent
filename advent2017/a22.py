class Node:
    def __init__(self, x, y, infected):
        self.x = x
        self.y = y
        self.infected = infected


def getByLocation(nodes, x, y):
    nodes = [i for i in nodes if i.x == x and i.y == y]
    if len(nodes) == 1:
        return nodes[0]
    else:
        return False


def p2(file):
    infected = {
        "#": 2,
        ".": 0
    }

    nodes = {}

    for line in range(len(file)):
        file[line] = file[line].strip()
        for node in range(len(file[line])):
            x = node - 12
            y = 12 - line
            inf = infected[file[line][node]]
            if inf != 0:
                nodes[(x, y)] = inf
    x = 0
    y = 0

    direction = 0

    total = 0

    for burst in range(10000000):
        infected = nodes.get((x, y), False)

        if not infected:
            nodes[(x, y)] = 0

        if infected == 0:
            direction = (direction + 3) % 4
        elif infected == 1:
            total += 1
        elif infected == 2:
            direction = (direction + 1) % 4
        elif infected == 3:
            direction = (direction + 2) % 4

        nodes[(x, y)] = (infected + 1) % 4

        if direction == 0:
            y += 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y -= 1
        elif direction == 3:
            x -= 1
    return total


def p1(file):
    infected = {
        "#": True,
        ".": False
    }

    nodes = []
    for line in range(len(file)):
        file[line] = file[line].strip()
        for node in range(len(file[line])):
            x = node - 12
            y = 12 - line
            nodes.append(Node(x, y, infected[file[line][node]]))
    x = 0
    y = 0

    direction = 0

    total = 0

    for burst in range(10000):
        currentNode = getByLocation(nodes, x, y)
        if not currentNode:
            currentNode = Node(x, y, False)
            nodes.append(currentNode)
        if currentNode.infected:
            direction = (direction + 1) % 4
        else:
            direction = (direction + 3) % 4
            total += 1
        currentNode.infected = not currentNode.infected
        if direction == 0:
            y += 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y -= 1
        elif direction == 3:
            x -= 1
    return total


file = list(open("f.txt", "r"))
print(p2(file))