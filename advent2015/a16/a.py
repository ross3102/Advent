present = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}


def isPossible(line):
    line = line.strip().split(", ")
    line[0] = line[0].split(": ")

    memories = {}
    memories[line[0][1]] = int(line[0][2])
    for i in range(1, len(line)):
        temp = line[i].split(": ")
        memories[temp[0]] = int(temp[1])

    for key in present:
        if present[key] != memories.get(key, present[key]):
            return False
    return True


with open("in.txt", "r") as file:
    sues = []
    for line in file:
        if isPossible(line):
            print(line.split()[1][:-1])