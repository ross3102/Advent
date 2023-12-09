from os import path
file = open(path.dirname(__file__) + "/i", "r")

class Range:
    def __init__(self, l, h):
        self.l = l
        self.h = h

    def __str__(self):
        return "[%d, %d]" % (self.l, self.h)

class MapRange:
    def __init__(self, ds, ss, length):
        self.ds = ds
        self.ss = ss
        self.length = length

    def contains(self, i):
        return self.ss <= i < self.ss + self.length
    
    def t(self, i):
        return i - self.ss + self.ds
    
    def overlap(self, r: Range):
        if r.l <= self.ss and r.h >= self.ss + self.length - 1:
            return Range(self.ds, self.ds + self.length - 1)
        elif r.l <= self.ss and self.contains(r.h):
            return Range(self.ds, self.t(r.h))
        elif self.contains(r.l) and r.h >= self.ss + self.length - 1:
            return Range(self.t(r.l), self.ds + self.length - 1)
        elif self.contains(r.l) and self.contains(r.h):
            return Range(self.t(r.l), self.t(r.h))
        else:
            return None

def solve():
    seeds = list(map(int, file.readline().strip().split(": ")[1].split()))
    ranges = [Range(seeds[i], seeds[i]+seeds[i+1]-1) for i in range(0, len(seeds), 2)]
    maps = []
    file.readline()
    line = file.readline()
    while line:
        line = file.readline()
        newmap = []
        while len(line) > 1:
            a, b, c = map(int, line.strip().split())
            newmap.append(MapRange(a, b, c))
            line = file.readline()
        line = file.readline()
        maps.append(sorted(newmap, key=lambda x: x.ss))

    for m in maps:
        newranges = []
        for r in ranges:
            maxval = r.l
            for mr in m:
                o = mr.overlap(r)
                if o is not None:
                    newranges.append(o)
                    if mr.ss > maxval:
                        newranges.append(Range(maxval, mr.ss-1))
                    maxval = max(maxval, mr.ss + mr.length)
            if maxval <= r.h:
                newranges.append(Range(maxval, r.h))
        ranges = newranges
    return min(r.l for r in ranges)
    

ans = solve()
print(ans)

file.close()