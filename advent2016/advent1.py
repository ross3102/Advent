directions = "R1, R1, R3, R1, R1, L2, R5, L2, R5, R1, R4, L2, R3, L3, R4, L5, R4, R4, R1, L5, L4, R5, R3, L1, R4, R3, L2, L1, R3, L4, R3, L2, R5, R190, R3, R5, L5, L1, R54, L3, L4, L1, R4, R1, R3, L1, L1, R2, L2, R2, R5, L3, R4, R76, L3, R4, R191, R5, R5, L5, L4, L5, L3, R1, R3, R2, L2, L2, L4, L5, L4, R5, R4, R4, R2, R3, R4, L3, L2, R5, R3, L2, L1, R2, L3, R2, L1, L1, R1, L3, R5, L5, L1, L2, R5, R3, L3, R3, R5, R2, R5, R5, L5, L5, R2, L3, L5, L2, L1, R2, R2, L2, R2, L3, L2, R3, L5, R4, L4, L5, R3, L4, R1, R3, R2, R4, L2, L3, R2, L5, R5, R4, L2, R4, L1, L3, L1, L3, R1, R2, R1, L5, R5, R3, L3, L3, L2, R4, R2, L5, L1, L1, L5, L4, L1, L1, R1"

dirs = directions.split(", ")
history = []
x = 0
y = 0
coord = (x,y)
direction = 1
for i in dirs:
    if i[0] == "R":
        if direction in (1,2,3):
            direction += 1
        elif direction == 4:
            direction = 1
    elif i[0] == "L":
        if direction in (2,3,4):
            direction -= 1
        elif direction == 1:
            direction = 4
    if direction == 1:
        for i in range(int(i[1:])):
            y += 1
            coord = (x, y)
            if coord in history:
                print(coord)
            else:
                history.append(coord)
    elif direction == 2:
        for i in range(int(i[1:])):
            x += 1
            coord = (x, y)
            if coord in history:
                print(coord)
            else:
                history.append(coord)
    elif direction == 3:
        for i in range(int(i[1:])):
            y -= 1
            coord = (x, y)
            if coord in history:
                print(coord)
            else:
                history.append(coord)
    elif direction == 4:
        for i in range(int(i[1:])):
            x -= 1
            coord = (x, y)
            if coord in history:
                print(coord)
            else:
                history.append(coord)