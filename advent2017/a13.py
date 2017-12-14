class WallList:
    def __init__(self):
        self.walls = []

    def get_wall(self, number):
        correct = [w for w in self.walls if w.depth == number]
        if len(correct) == 0:
            return -1
        return correct[0]

    def add(self, wall):
        self.walls.append(wall)

    def max_wall(self):
        return max([w.depth for w in self.walls])

    def move_all(self):
        for w in self.walls:
            w.move()

    def reset(self):
        for w in self.walls:
            w.pos = 0

    def printPos(self):
        print([str(i.pos) + ", " for i in self.walls])

class Wall:
    def __init__(self, depth, range):
        self.depth = depth
        self.range = range
        self.pos = 0
        self.direction = 1

    def move(self):
        if self.pos == self.range - 1:
            self.direction = -1
        elif self.pos == 0:
            self.direction = 1
        self.pos += self.direction

    def get_severity(self):
        return self.depth * self.range


def p1(file):
    walls = WallList()
    for line in file:
        line = line.strip().split(": ")
        walls.add(Wall(int(line[0]), int(line[1])))

    severity = 0
    packet = -1
    while packet != walls.max_wall():
        packet += 1
        cur = walls.get_wall(packet)
        if cur != -1:
            if cur.pos == 0:
                severity += cur.get_severity()
        walls.move_all()
    return severity

def p2(file):
    walls = []
    for line in file:
        line = line.strip().split(": ")
        walls.append(Wall(int(line[0]), int(line[1])))

    delay = -1
    done = False
    while not done:
        delay += 1
        done = True
        for wall in walls:
            if (delay + wall.depth) % (2*(wall.range - 1)) == 0:
                done = False
                break
    return delay

file = list(open("f.txt", "r"))
print(p2(file))
