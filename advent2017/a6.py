def p1(start):
    seen = [([int(i) for i in start.split("\t")], 0)]

    total = 0

    while True:
        cur = seen[-1][0]
        new = [i for i in cur]
        left = max(cur)
        i = new.index(left) + 1
        new[new.index(left)] = 0
        while left > 0:
            new[i % len(cur)] += 1
            i += 1
            left -= 1
        total += 1
        if new in [g[0] for g in seen]:
            print(new)
            return total - [g[1] for g in seen if g[0] == new][0]
        else:
            seen.append((new, total))

print(p1("0\t2\t7\t0"))
print(p1("4\t10\t4\t1\t8\t4\t9\t14\t5\t1\t14\t15\t0\t15\t3\t5"))
