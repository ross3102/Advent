file = open('advent2dirs','r')
dirs = []
keypad = [[0,0,5,0,0],[0,2,6,'A',0],[1,3,7,'B','D'],[0,4,8,'C',0],[0,0,9,0,0]]
code = []
pos = [0,2]
for line in file:
    dirs.append(line)
for line in dirs:
    for char in line:
        if char == 'R':
            try:
                if keypad[pos[0] + 1][pos[1]] != 0:
                    pos[0] += 1
            except:
                pass
        elif char == "L":
            try:
                if pos[0] == 0:
                    raise SyntaxError
                if keypad[pos[0] - 1][pos[1]] != 0:
                    pos[0] -= 1
            except:
                pass
        elif char == "U":
            try:
                if pos[1] == 0:
                    raise SyntaxError
                if keypad[pos[1] - 1][pos[0]] != 0:
                    pos[1] -= 1
            except:
                pass
        elif char == "D":
            try:
                if keypad[pos[1] + 1][pos[0]] != 0:
                    pos[1] += 1
            except:
                pass
    spot = keypad[pos[0]][pos[1]]
    code.append(str(spot))
    print(spot)
print("Code:", "".join(code))