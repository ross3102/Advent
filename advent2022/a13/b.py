from functools import cmp_to_key

file = open("i", "r")

def comp(left, right):
    if type(left) == list:
        if type(right) == list:
            ll = len(left)
            lr = len(right)
            i = 0
            while i < ll:
                if i >= lr:
                    return 1
                curisless = comp(left[i], right[i])
                if curisless != 0:
                    return curisless
                i += 1
            if i < lr:
                return -1
            return 0
        else:
            return comp(left, [right])
    else:
        if type(right) == list:
            return comp([left], right)
        else:
            if left == right:
                return 0
            return -1 if left < right else 1

def solve():
    lines = [[[2]],[[6]]]
    line = file.readline()
    while line:
        line = line.strip()
        lst1 = eval(line)
        line = file.readline().strip()
        lst2 = eval(line)
        file.readline()
        line = file.readline()
        lines.append(lst1)
        lines.append(lst2)

    keyfn = cmp_to_key(comp)
    sortedlist = sorted(lines, key=keyfn)
    ans = 1
    for i in range(len(sortedlist)):
        if sortedlist[i] == [[2]] or sortedlist[i] == [[6]]:
            ans *= i+1

    return ans

ans = solve()
print(ans)

file.close()