import ast


class Num:
    def __init__(self, n):
        self.n = n

    def reduce(self):
        pass

    def explodeHelp(self, depth, addTo, addIn):
        if addIn == -1:
            return [0, self]
        else:
            self.n += addIn
            return [2, None]

    def split(self):
        return False

    def mag(self):
        return self.n

    def __str__(self):
        return str(self.n)


class Pair:
    def __init__(self, l):
        if type(l[0]) == int:
            self.l = Num(l[0])
        elif type(l[0]) == list:
            self.l = Pair(l[0])
        else:
            self.l = l[0]

        if type(l[1]) == int:
            self.r = Num(l[1])
        elif type(l[1]) == list:
            self.r = Pair(l[1])
        else:
            self.r = l[1]

    def add(self, other):
        return Pair(self, other).reduce()

    def reduce(self):
        while True:
            e = self.explode()[0]
            if e == 0:
                s = self.split()
                if not s:
                    return

    # return: [0, Num] if searching, [1, int] if found, [2, None] if done
    def explodeHelp(self, depth: int, addTo: Num, addIn: int):
        if depth == 3 and addIn == -1:
            if type(self.l) == Num and type(self.r) == Pair:
                self.l.n += self.r.l.n
                ret = self.r.r.n
                self.r = Num(0)
                return [1, ret]
            elif type(self.l) == Pair:
                addTo.n += self.l.l.n
                tmp = self.r
                while type(tmp) == Pair:
                    tmp = tmp.l
                tmp.n += self.l.r.n
                ret = self.l.r.n
                self.l = Num(0)
                return [2, None]
            else:
                return [0, self.r]
        res_l = self.l.explodeHelp(depth + 1, addTo, addIn)
        if res_l[0] == 2:
            return [2, None]
        elif res_l[0] == 0:
            return self.r.explodeHelp(depth + 1, res_l[1], addIn)
        else:
            return self.r.explodeHelp(depth + 1, addTo, res_l[1])

    def explode(self):
        return self.explodeHelp(0, Num(0), -1)

    def split(self):
        if type(self.l) == Num and self.l.n >= 10:
            self.l = Pair([self.l.n // 2, self.l.n // 2 + self.l.n % 2])
            return True
        elif self.l.split():
            return True
        elif type(self.r) == Num and self.r.n >= 10:
            self.r = Pair([self.r.n // 2, self.r.n // 2 + self.r.n % 2])
            return True
        else:
            return self.r.split()

    def mag(self):
        return 3 * self.l.mag() + 2 * self.r.mag()

    def __str__(self):
        return "[" + str(self.l) + "," + str(self.r) + "]"


nums = []

with open("in.txt", "r") as file:
    for line in file:
        nums.append(Pair(ast.literal_eval(line.strip())))

curnum = nums[0]
curnum.reduce()

for n in range(1, len(nums)):
    nums[n].reduce()
    curnum = Pair([curnum, nums[n]])
    curnum.reduce()

print(curnum.mag())
