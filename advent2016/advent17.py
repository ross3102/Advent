rows = [".^^..^...^..^^.^^^.^^^.^^^^^^.^.^^^^.^^.^^^^^^.^...^......^...^^^..^^^.....^^^^^^^^^....^^...^^^^..^"]

def check(left, center, right):
    return left and center and not right or \
           not left and center and right or \
           left and not center and not right or \
           not left and not center and right


for i in range(400000 - 1):
    prev = rows[-1]
    new = ""
    for j in range(len(prev)):
        if j == 0:
            left = False
        else:
            left = prev[j - 1] == "^"
        center = prev[j] == "^"
        if j == len(prev) - 1:
            right = False
        else:
            right = prev[j + 1] == "^"

        new += "^" if check(left, center, right) else "."
    rows.append(new)

print(sum([row.count(".") for row in rows]))