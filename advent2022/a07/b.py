file = open("i", "r")

sizes = []

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.contents = []
    
    def addSubDir(self, name):
        nd = Directory(name, self)
        self.contents.append(nd)
        return nd

    def getSubDir(self, name):
        for item in self.contents:
            if type(item) == Directory and item.name == name:
                return item
        return None

    def calcsize(self):
        tot = 0
        for item in self.contents:
            tot += item.calcsize()
        sizes.append((self.name, tot))
        return tot

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def calcsize(self):
        return self.size

def solve():
    root = Directory("/", None)
    curdir = root
    line = file.readline()
    while line:
        line = line.strip().split()
        if line[1] == "cd":
            if line[2] == "/":
                curdir = root
            elif line[2] == "..":
                curdir = curdir.parent
            else:
                newDir = curdir.getSubDir(line[2])
                if newDir is None:
                    curdir = curdir.addSubDir(line[2])
                else:
                    curdir = newDir
            line = file.readline()
        elif line[1] == "ls":
            isNew = len(curdir.contents) == 0
            line = file.readline()
            while line and line[0] != "$":
                if isNew:
                    line = line.strip().split()
                    if line[0] == "dir":
                        curdir.addSubDir(line[1])
                    else:
                        curdir.contents.append(File(line[1], int(line[0])))
                line = file.readline()
    root.calcsize()
    sizes.sort(key=lambda p: p[1])
    rem = 70000000 - sizes[-1][1]
    for p in sizes:
        if p[1] + rem >= 30000000:
            return p[1]

ans = solve()
print(ans)

file.close()