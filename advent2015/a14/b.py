class RunningReindeer:
    def __init__(self, name, speed, seconds, rest):
        self.name = name
        self.speed = speed
        self.seconds = seconds
        self.rest = rest
        self.sleeping = False
        self.curPos = 0
        self.points = 0


deers = []

total_seconds = 2503

with open("in.txt", "r") as file:
    for line in file:
        line = line.strip().split()
        r1 = line[0]
        speed = int(line[3])
        seconds = int(line[6])
        rest = int(line[-2])
        deers.append(RunningReindeer(r1, speed, seconds, rest))

    for s in range(1, total_seconds+1):
        furthest = deers[0]
        for r in deers:
            if r.sleeping:
                if s % (r.seconds + r.rest) == 0:
                    r.sleeping = False
            else:
                r.curPos += r.speed
                if s % (r.seconds + r.rest) == r.seconds:
                    r.sleeping = True
            if r.curPos > furthest.curPos:
                furthest = r
        furthest.points += 1

    print(max(d.points for d in deers))
