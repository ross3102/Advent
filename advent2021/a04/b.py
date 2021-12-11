def findWinner(file):
    line = file.readline()
    nums = [int(i) for i in line.split(",")]
    boards = []
    line = file.readline()
    while line:
        curBoard = []
        for i in range(5):
            line = file.readline()
            curBoard.append([int(i) for i in line.split()])
        boards.append(curBoard)
        line = file.readline()

    validBoards = [i for i in range(len(boards))]

    numWon = 0

    for n in nums:
        newValid = []
        for bNum in validBoards:
            b = boards[bNum]
            found = False
            for i in range(len(b)):
                for j in range(len(b[i])):
                    if b[i][j] == n:
                        found = True
                        b[i][j] = "X"
                        if any(b[i][x] != "X" for x in range(len(b[i]))) and any(b[x][j] != "X" for x in range(len(b))):
                            newValid.append(bNum)
                        else:
                            numWon += 1
                            if numWon == len(boards):
                                return sum(sum(num for num in row if num != "X") for row in b) * n
            if not found:
                newValid.append(bNum)
        validBoards = newValid


with open("in.txt", "r") as file:
    n = findWinner(file)
    print(n)
