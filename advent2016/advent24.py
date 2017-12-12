def allUnique(x):
    seen = list()
    return not any(i in seen or seen.append(i) for i in x)


class Path:
    def __init__(self, steps, found, x, y, hist):
        self.steps = steps
        self.found = [i for i in found]
        self.history = [i for i in hist]
        self.x = x
        self.y = y

    def reproduce(self):
        possibilities = []

        if self.y < len(file) - 2:
            self.check(self.x, self.y + 1, possibilities)

        if self.x < len(file[self.y]) - 2:
            self.check(self.x + 1, self.y, possibilities)
        if self.y > 0:
            self.check(self.x, self.y - 1, possibilities)

        if self.x > 0:
            self.check(self.x - 1, self.y, possibilities)

        self.found.sort()

        return possibilities

    def check(self, x, y, possibilities):
        if file[y][x] != "#":
            f = [i for i in self.found]
            h = [i for i in self.history]
            if file[y][x] in nums:
                if file[y][x] not in self.found:
                    f.append(file[y][x])
                    h = []
            h.append([x, y])
            possibilities.append(Path(self.steps + 1, f, x, y, h))


file = list(open("f", "r"))

done = False

zero = file[1].index("0")

paths = [Path(0, [], zero, 1, [[zero, 1]])]

nums = "1,2,3,4,5,6,7".split(",")

i = 0

while not done:
    newpaths = []
    for p in paths:
        new = p.reproduce()

        if p.found == nums:
            print(p.steps)
            done = True
            break
        for newpath in new:
            if allUnique(newpath.history):
                newpaths.append(newpath)
    print(i)
    i += 1
    paths = newpaths
