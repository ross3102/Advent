def allSame(iterator):
   return len(set(iterator)) <= 1

def getNames():
    return [p.name for p in programs]

def getByName(name):
    try:
        return [p for p in programs if p.name == name][0]
    except:
        return -1

file = list(open("f.txt", "r"))

base = "vtzay"

class Program:
    def __init__(self, parent, weight, name):
        self.parent = parent
        self.weight = weight
        self.name = name

    def getChildren(self):
        return [p for p in programs[1:] if p.parent == self]

    def calcWeight(self):
        children = self.getChildren()
        weights = []
        if len(children) > 0:
            for p in self.getChildren():
                orig = p.weight
                w = p.calcWeight()
                if len(weights) > 0 and w not in weights:
                    print(orig - (p.weight - weights[0]))
                weights.append(w)
                self.weight += w
        return self.weight

programs = []

for line in file:
    l = line.strip().split(" -> ")
    parent = l[0].split(" ")[0]
    weight = int(l[0].split("(")[1][:-1])
    if len(l) > 1:
        if parent in getNames():
            getByName(parent).weight = weight
        else:
            programs.append(Program(None, weight, parent))
        children = l[1].split(", ")
        for child in children:
            if child in getNames():
                getByName(child).parent = parent
            else:
                programs.append(Program(parent, 0, child))
    else:
        if parent in getNames():
            getByName(parent).weight = weight
        else:
            programs.append(Program(None, weight, parent))

for prog in programs:
    prog.parent = getByName(prog.parent)

baseObj = getByName(base)

print([(p.name, p.weight) for p in programs])

print(baseObj.calcWeight())
print(sum([p.weight for p in programs]))
