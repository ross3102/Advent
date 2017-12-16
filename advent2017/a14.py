class One:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.adjacent = []

    def getAdjacent(self, ones):
        for one in ones:
            if (abs(self.x - one.x) == 1 and self.y == one.y) or (abs(self.y - one.y) == 1 and self.x == one.x):
                self.adjacent.append(one)

    def getGroup(self, seen, ones):
        for a in self.adjacent:
            if a not in seen:
                seen.append(a)
                seen = a.getGroup(seen, ones)
        return seen


def p1(orig):
    tot = 0
    for row in range(128):
        string = orig + "-" + str(row)
        pos, skip = 0, 0

        nums = list(range(256))
        lengths = [ord(l) for l in string]
        for i in "17,31,73,47,23".split(","):
            lengths.append(int(i))

        for it in range(64):
            for l in lengths:
                temp = [i for i in nums]
                for i in range(l):
                    temp[(pos + i) % 256] = nums[(pos + l - 1 - i) % 256]
                pos += l + skip
                skip += 1
                nums = temp

        ans = []

        for i in range(16):
            total = 0
            pos = i * 16
            for j in range(pos, pos + 16):
                total ^= nums[j]
            ans.append(total)

        ans = ["{:02x}".format(a) for a in ans]

        ans = [i for i in "".join(ans)]
        hx = {
            "0":"0000",
            "1":"0001",
            "2":"0010",
            "3":"0011",
            "4":"0100",
            "5":"0101",
            "6":"0110",
            "7":"0111",
            "8":"1000",
            "9":"1001",
            "a":"1010",
            "b":"1011",
            "c":"1100",
            "d":"1101",
            "e":"1110",
            "f":"1111"
        }
        tot += ("".join([hx[i] for i in ans])).count("1")
    return tot

def p2(orig):
    grid = []
    for row in range(128):
        string = orig + "-" + str(row)
        pos, skip = 0, 0

        nums = list(range(256))
        lengths = [ord(l) for l in string]
        for i in "17,31,73,47,23".split(","):
            lengths.append(int(i))

        for it in range(64):
            for l in lengths:
                temp = [i for i in nums]
                for i in range(l):
                    temp[(pos + i) % 256] = nums[(pos + l - 1 - i) % 256]
                pos += l + skip
                skip += 1
                nums = temp

        ans = []

        for i in range(16):
            total = 0
            pos = i * 16
            for j in range(pos, pos + 16):
                total ^= nums[j]
            ans.append(total)

        ans = ["{:02x}".format(a) for a in ans]

        ans = [i for i in "".join(ans)]
        hx = {
            "0": "0000",
            "1": "0001",
            "2": "0010",
            "3": "0011",
            "4": "0100",
            "5": "0101",
            "6": "0110",
            "7": "0111",
            "8": "1000",
            "9": "1001",
            "a": "1010",
            "b": "1011",
            "c": "1100",
            "d": "1101",
            "e": "1110",
            "f": "1111"
        }
        grid.append("".join([hx[i] for i in ans]))

    ones = []

    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == "1":
                ones.append(One(row, column))

    for one in ones:
        one.getAdjacent(ones)

    total = 0
    while len(ones) > 0:
        one = ones[0]
        group = one.getGroup([one], ones)
        for o in group:
            ones.remove(o)
        total += 1
    return total

string = "ljoxqyyw"
print(p2(string))