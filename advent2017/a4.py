def allUnique(x):
    seen = []
    for i in x:
        i =[j for j in i]
        i.sort()
        if any(i == g for g in seen):
            return False
        else:
            seen.append(i)
    print(seen)
    return True

file = open("f.txt", "r")

total = 0

for line in file:
    line = line.strip().split(" ")
    if allUnique(line):
        total += 1

print(total)