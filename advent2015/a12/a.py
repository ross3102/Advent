with open("in.txt", "r") as file:
    json = file.readline()
    total = 0
    curNum = 0
    neg = 1
    for c in json:
        if c == "-":
            neg = -1
            continue
        try:
            i = int(c)
            curNum *= 10
            curNum += i
        except:
            total += curNum * neg
            curNum = 0
            neg = 1
    print(total)
