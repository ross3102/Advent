class Box:
    def __init__(self, l, r, t, b):
        self.l = l
        self.r = r
        self.t = t
        self.b = b

    def in_box(self, x, y):
        return self.l <= x <= self.r and self.b <= y <= self.t


box = None
with open("in.txt", "r") as file:
    xstr, ystr = file.readline().strip().split()[2:]
    xl, xr = map(int, xstr.split("=")[1][:-1].split(".."))
    yb, yt = map(int, ystr.split("=")[1].split(".."))
    box = Box(xl, xr, yt, yb)


def possible(vx, vy, box):
    maxy = 0
    x = 0
    y = 0
    while True:
        if box.in_box(x, y):
            return maxy
        x += vx
        y += vy
        if y > maxy:
            maxy = y
        vx = max(vx-1, min(vx+1, 0))
        vy -= 1
        if y < box.b or x > box.r:
            return False


i = 0
maxy = 0

for vy in range(1000):
    for vx in range(200):
        my = possible(vx, vy, box)
        if my and my > maxy:
            maxy = my
            print(vx, vy, maxy)

print(maxy)
