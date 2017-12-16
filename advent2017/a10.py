def p1(lengths, n):
    lengths = lengths.split(",")
    nums = list(range(n))
    pos = 0
    skip = 0
    for l in lengths:
        temp = [i for i in nums]
        l = int(l)
        for i in range(l):
            temp[(pos+i) % n] = nums[(pos+l-1-i) % n]

        pos += l + skip
        skip += 1
        nums = temp

    return nums[0] * nums[1]


def p2(lengths, n):
    pos, skip = 0, 0

    nums = list(range(n))
    lengths = [ord(l) for l in lengths]
    for i in "17,31,73,47,23".split(","):
        lengths.append(int(i))

    for it in range(64):
        for l in lengths:
            temp = [i for i in nums]
            for i in range(l):
                temp[(pos + i) % n] = nums[(pos + l - 1 - i) % n]
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

    return "".join(ans)

file = list(open("f.txt", "r"))[0]

print(p2(file, 256))

