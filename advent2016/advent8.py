file = open('f', 'r')
board = []
for b in range(50):
    board.append(['.', '.', '.', '.', '.', '.'])

for line in file:
    line = line.split()
    if line[0] == "rect":
        dimensions = line[1].split("x")
        for x in range(int(dimensions[0])):
            for y in range(int(dimensions[1])):
                board[x][y] = '#'
        total = 0
        zeros = 0
        for r in board:
            for light in r:
                if light == '#':
                    total += 1
                else:
                    zeros += 1
        print(total)
    else:
        count = int(line[4])
        templist = ["gop"] * count
        rownum = line[2]
        rownum = int(rownum[rownum.index("=") + 1:])
        if line[1] == "row":
            for l in board:
                templist.append(l[rownum])
            newlist = templist[50:] + templist[count:50]
        elif line[1] == "column":
            for l in board[rownum]:
                templist.append(l)
            newlist = templist[6:] + templist[count:6]
        if line[1] == "row":
            for x in range(50):
                board[x][rownum] = newlist[x]
        else:
            board[rownum] = newlist

total = 0
zeros = 0
for line in board:
    for light in line:
        if light == '#':
            total += 1
        else:
            zeros += 1
for i in range(6):
    for g in board:
        print(g[i], end=" ")
    print()
print()
print(total)
print(zeros)