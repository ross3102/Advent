file = open("i", "r")

class Op:
    def __init__(self, num, timer):
        self.num = num
        self.timer = timer

    def sub(self):
        self.timer -= 1
        return self.timer == 0

def docycle(ops, x, cycle, ans):
    newops = []
    if cycle % 40 == 20:
        ans += cycle * x
    for op in ops:
        if op.sub():
            x += op.num
        else:
            newops.append(op)
    return newops, x, cycle + 1, ans

def solve():
    ans = 0
    ops = []
    x = 1
    cycle = 1
    for line in file:
        line = line.strip().split()
        cmd = line[0]
        if cmd == "noop":
            ops, x, cycle, ans = docycle(ops, x, cycle, ans)
        elif cmd == "addx":
            ops.append(Op(int(line[1]), 2))
            ops, x, cycle, ans = docycle(ops, x, cycle, ans)
            ops, x, cycle, ans = docycle(ops, x, cycle, ans)
    return ans

ans = solve()
print(ans)

file.close()