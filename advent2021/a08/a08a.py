with open("i08.txt", "r") as file:
    total = 0
    for line in file:
        line = [side.split() for side in line.strip().split(" | ")]
        out = line[1]
        total += len([i for i in out if len(i) in [2,3,4,7]])
    print(total)