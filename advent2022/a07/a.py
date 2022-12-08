file = open("i", "r")

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

    def calcsize(self, small):
        tot = 0
        for item in self.contents:
            tot += item.calcsize(small)
        if tot <= 100000:
            small.append([self.name, tot])
        return tot

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def calcsize(self, small):
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
    small = []
    root.calcsize(small)
    return sum(p[1] for p in small)

ans = solve()
print(ans)

file.close()