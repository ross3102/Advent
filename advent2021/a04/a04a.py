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

    for n in nums:
        for bNum in range(len(boards)):
            b = boards[bNum]
            for i in range(len(b)):
                for j in range(len(b[i])):
                    if b[i][j] == n:
                        b[i][j] = "X"
                        if all(b[i][x] == "X" for x in range(len(b[i]))) or all(b[x][j] == "X" for x in range(len(b))):
                            return sum(sum(num for num in row if num != "X") for row in b) * n

with open("i04.txt", "r") as file:
    n = findWinner(file)
    print(n)

    
