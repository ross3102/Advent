file = open('f', 'r')
total = 0
split_file = []
newfile = []
for line in file:
    split_file.append(line.split())
for x in range(0, len(split_file), 3):
    for y in range(3):
        if ' ' not in split_file[x][y]:
            newfile.append([split_file[x][y], split_file[x+1][y], split_file[x+2][y]])
for line in newfile:
    side1 = int(line[0])
    side2 = int(line[1])
    side3 = int(line[2])
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        total += 1
print(total)