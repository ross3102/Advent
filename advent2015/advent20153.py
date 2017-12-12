file = open('f', 'r')
sx = 0
sy = 0
rsx = 0
rsy = 0
history = [(0,0)]
s = 0
for line in file:
    for char in line:
        if s == 0:
            x = sx
            y = sy
        else:
            x = rsx
            y = rsy
        if char == "^":
            y += 1
        elif char == ">":
            x += 1
        elif char == "v":
            y -= 1
        elif char == "<":
            x -= 1
        if (x,y) not in history:
            history.append((x,y))
        if s == 0:
            s = 1
            sx = x
            sy = y
        else:
            rsx = x
            rsy = y
            s = 0
print("Santas left presents at %d houses" % len(history))