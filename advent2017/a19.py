def p2(file):
    y = 0
    x = file[0].index("|")

    width = max([len(i) for i in file])
    height = len(file)

    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4
    direction = DOWN

    letters = ""
    steps = 0

    while 0 <= x < width and 0 <= y < height and file[y][x] != " ":
        if file[y][x] == "+":
            if direction == UP or direction == DOWN:
                try:
                    if file[y][x - 1] not in ("|", " "):
                        direction = LEFT
                    else:
                        direction = RIGHT
                except:
                    direction = RIGHT
            else:
                try:
                    if file[y - 1][x] not in ("-", " "):
                        direction = UP
                    else:
                        direction = DOWN
                except:
                    direction = DOWN
        elif file[y][x] not in ("|", "-"):
            letters += file[y][x]
        if direction == UP:
            y -= 1
        elif direction == RIGHT:
            x += 1
        elif direction == DOWN:
            y += 1
        elif direction == LEFT:
            x -= 1
        steps += 1
    return steps

def p1(file):
    y = 0
    x = file[0].index("|")

    width = max([len(i) for i in file])
    height = len(file)

    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4
    direction = DOWN

    letters = ""

    while 0 <= x < width and 0 <= y < height and file[y][x] != " ":
        if file[y][x] == "+":
            if direction == UP or direction == DOWN:
                try:
                    if file[y][x-1] not in ("|", " "):
                        direction = LEFT
                    else:
                        direction = RIGHT
                except:
                    direction = RIGHT
            else:
                try:
                    if file[y-1][x] not in ("-", " "):
                        direction = UP
                    else:
                        direction = DOWN
                except:
                    direction = DOWN
        elif file[y][x] not in ("|", "-"):
            letters += file[y][x]
        if direction == UP:
            y -= 1
        elif direction == RIGHT:
            x += 1
        elif direction == DOWN:
            y += 1
        elif direction == LEFT:
            x -= 1
    return letters


file = list(open("f.txt", "r"))
print(p2(file))