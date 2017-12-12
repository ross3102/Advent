file = open("f.txt", "r")

total = 0

variables = {}


def greater(a, b): return a > b


def less(a, b): return a < b


def greateq(a, b): return a >= b


def lesseq(a, b): return a <= b


def eq(a, b): return a == b


def neq(a, b): return a != b


def inc(a,b): return a + b


def dec(a,b): return a - b

funcs = {
    ">": greater,
    ">=": greateq,
    "<": less,
    "<=": lesseq,
    "==": eq,
    "!=": neq,
    "inc": inc,
    "dec": dec
}

mx = 0

for line in file:
    line = line.strip().split(" ")
    varName = line[0]
    incDec = funcs[line[1]]
    num = int(line[2])
    varCond = line[4]
    func = funcs[line[5]]
    numCond = int(line[6])
    if varName not in variables.keys():
        variables[varName] = 0
    if varCond not in variables.keys():
        variables[varCond] = 0
    if func(variables[varCond], numCond):
        variables[varName] = incDec(variables[varName], num)
    if variables[varName] > mx:
        mx = variables[varName]

print(mx)