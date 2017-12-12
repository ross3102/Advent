orig = open("f", "r")
file = []
for i in orig:
    file.append(i)

var = {}

l = 0

while l < len(file):
    line = file[l].split()
    method = line[0]
    if method == "cpy":
        toCopy = 0
        try:
            toCopy = int(line[1])
        except:
            toCopy = var[line[1]]
        var[line[2]] = toCopy
    elif method == "inc":
        var[line[1]] += 1
    elif method == "dec":
        var[line[1]] -= 1
    if method == "jnz":
        toJump = 0
        try:
            toJump = int(line[1])
        except:
            toJump = var.get(line[1], 0)
        if toJump != 0:
            l += int(line[2])
        else:
            l += 1
    else:
        l += 1
print(var.get("a"))