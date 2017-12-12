import hashlib

class Point:
    def __init__(self, x, y, path):
        self.x = x
        self.y = y
        self.path = path

    def branch(self):
        newpoints = []
        hash = hashlib.md5((PASSWORD + self.path).encode()).hexdigest()
        up = hash[0] in OPENS and self.y > 0
        down = hash[1] in OPENS and self.y < 3
        left = hash[2] in OPENS and self.x > 0
        right = hash[3] in OPENS and self.x < 3
        if up:
            newpoints.append(Point(self.x, self.y - 1, self.path + "U"))
        if down:
            newpoints.append(Point(self.x, self.y + 1, self.path + "D"))
        if left:
            newpoints.append(Point(self.x - 1, self.y, self.path + "L"))
        if right:
            newpoints.append(Point(self.x + 1, self.y, self.path + "R"))
        return newpoints




PASSWORD = "awrkjxxr"

OPENS = "bcdef"

tips = [Point(0, 0, "")]

done = False

answers = []

while not done:
    done = True
    newpoints = []
    availables = hashlib
    for point in tips:
        ps = point.branch()
        if len(ps) > 0: done = False
        for p in ps:
            if p.x == 3 and p.y == 3:
                answers.append(len(p.path))
                answer = p.path
            else:
                newpoints.append(p)
    tips = newpoints

print(max(answers))