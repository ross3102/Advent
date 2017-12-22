class Particle:
    def __init__(self, num, p, v, a):
        self.num = num
        self.p = p
        self.v = v
        self.a = a

    def getDistance(self):
        return abs(self.p[0]) + abs(self.p[1]) + abs(self.p[2])

    def move(self):
        for i in range(3):
            self.v[i] += self.a[i]
            self.p[i] += self.v[i]

def p2(file):
    particles = []
    for lineNum in range(len(file)):
        line = file[lineNum]
        line = line.strip().split(", ")
        p = [int(i) for i in line[0][3:-1].split(",")]
        v = [int(i) for i in line[1][3:-1].split(",")]
        a = [int(i) for i in line[2][3:-1].split(",")]
        particles.append(Particle(lineNum, p, v, a))
    for i in range(100):
        [i.move() for i in particles]
        toRemove = []
        for i in particles:
            for j in particles:
                if j != i:
                    if i.p == j.p:
                        if i not in toRemove:
                            toRemove.append(i)
                        if j not in toRemove:
                            toRemove.append(j)
        for i in toRemove:
            particles.remove(i)
    return len(particles)

def p1(file):
    particles = []
    for lineNum in range(len(file)):
        line = file[lineNum]
        line = line.strip().split(", ")
        p = [int(i) for i in line[0][3:-1].split(",")]
        v = [int(i) for i in line[1][3:-1].split(",")]
        a = [int(i) for i in line[2][3:-1].split(",")]
        particles.append(Particle(lineNum, p, v, a))
    for i in range(1000):
        [i.move() for i in particles]
    minDistance = min([i.getDistance() for i in particles])
    minID = [i.num for i in particles if i.getDistance() == minDistance]
    return minID


file = list(open("f.txt", "r"))
print(p2(file))