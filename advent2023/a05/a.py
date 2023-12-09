from os import path
file = open(path.dirname(__file__) + "/i", "r")

class Range:
    def __init__(self, ds, ss, length):
        self.ds = ds
        self.ss = ss
        self.length = length

    def contains(self, i):
        return self.ss <= i < self.ss + self.length
    
    def mapped(self, i):
        return i - self.ss + self.ds

def solve():
    seeds = map(int, file.readline().strip().split(": ")[1].split())
    maps = []
    file.readline()
    line = file.readline()
    while line:
        line = file.readline()
        newmap = []
        while len(line) > 1:
            a, b, c = map(int, line.strip().split())
            newmap.append(Range(a, b, c))
            line = file.readline()
        line = file.readline()
        maps.append(newmap)
    answers = []

    for s in seeds:
        cur = s
        for m in maps:
            for r in m:
                if r.contains(cur):
                    cur = r.mapped(cur)
                    break
        answers.append(cur)
    
    return min(answers)

ans = solve()
print(ans)

file.close()