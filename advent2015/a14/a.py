class Reindeer:
    def __init__(self, name, speed, seconds, rest):
        self.name = name
        self.speed = speed
        self.seconds = seconds
        self.rest = rest


deers = []

total_seconds = 2503

with open("in.txt", "r") as file:
    for line in file:
        line = line.strip().split()
        r1 = line[0]
        speed = int(line[3])
        seconds = int(line[6])
        rest = int(line[-2])
        deers.append(Reindeer(r1, speed, seconds, rest))

    maxdist = 0

    for r in deers:
        dist = (total_seconds//(r.seconds+r.rest))*r.speed*r.seconds
        extra_secs = total_seconds % (r.seconds+r.rest)
        dist += r.speed*min(extra_secs, r.seconds)
        if dist > maxdist:
            maxdist = dist

    print(maxdist)
