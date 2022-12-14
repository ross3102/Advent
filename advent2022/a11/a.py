file = open("i", "r")

class Op:
    def __init__(self, rhs):
        self.f = lambda old: eval(rhs.replace("old", str(old)))

class Test:
    def __init__(self, div, tm, fm):
        self.div = div
        self.tm = tm
        self.fm = fm

    def apply(self, n):
        if n % self.div == 0:
            return self.tm
        else:
            return self.fm

class Monkey:
    def __init__(self, num, items, op, test):
        self.num = num
        self.items = items
        self.op = op
        self.test = test
        self.inspected = 0

def solve():
    monkeys = []
    line = file.readline()
    while line:
        line = line.strip()
        monkeynum = int(line.split()[1][:-1])
        items = list(map(int, file.readline().strip().split(": ")[1].split(", ")))
        op_rhs = file.readline().strip().split(" = ")[1]
        div = int(file.readline().strip().split()[-1])
        tm = int(file.readline().strip().split()[-1])
        fm = int(file.readline().strip().split()[-1])
        test = Test(div, tm, fm)
        op = Op(op_rhs)
        monkeys.append(Monkey(monkeynum, items, op, test))
        file.readline()
        line = file.readline()
    
    for round in range(20):
        for m in monkeys:
            for worry in m.items:
                worry = m.op.f(worry)
                worry //= 3
                monkeys[m.test.apply(worry)].items.append(worry)
                m.inspected += 1
            m.items = []
    
    monkeys.sort(key=lambda m: m.inspected)
    return monkeys[-1].inspected * monkeys[-2].inspected

ans = solve()
print(ans)

file.close()