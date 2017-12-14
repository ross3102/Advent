class Program:
    def __init__(self, number, attachments):
        self.number = number
        self.attachments = [i for i in attachments]

    def getGroup(self, seen):
        for a in self.attachments:
            if a not in seen:
                seen.append(a)
                seen = a.getGroup(seen)
        return seen


def getProgByNum(number, programs):
    found = [i for i in programs if i.number == number]
    if len(found) > 0:
        return found[0]
    else:
        return -1


def p1(file):
    programs = []
    for line in file:
        line = line.strip().split(" <-> ")
        number = int(line[0])
        newP = getProgByNum(number, programs)
        if newP == -1:
            newP = Program(number, [])
            programs.append(newP)
        attachments = [int(i) for i in line[1].split(", ")]
        for num in attachments:
            tempP = getProgByNum(num, programs)
            if tempP == -1:
                tempP = Program(num, [])
                programs.append(tempP)
            newP.attachments.append(tempP)
    zero = getProgByNum(0, programs)
    return len([i.number for i in zero.getGroup([zero])])

def p2(file):
    programs = []
    for line in file:
        line = line.strip().split(" <-> ")
        number = int(line[0])
        newP = getProgByNum(number, programs)
        if newP == -1:
            newP = Program(number, [])
            programs.append(newP)
        attachments = [int(i) for i in line[1].split(", ")]
        for num in attachments:
            tempP = getProgByNum(num, programs)
            if tempP == -1:
                tempP = Program(num, [])
                programs.append(tempP)
            newP.attachments.append(tempP)
    total = 0
    while len(programs) > 0:
        prog = programs[0]
        group = prog.getGroup([prog])
        for p in group:
            programs.remove(p)
        total += 1
    return total


file = list(open("f.txt", "r"))
print(p2(file))