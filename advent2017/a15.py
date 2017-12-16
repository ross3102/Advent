def p1(a, b):
    af = 16807
    bf = 48271
    mod = 2147483647
    total = 0
    for i in range(40000000):
        a = a * af % mod
        b = b * bf % mod
        if str(bin(a))[-16:] == str(bin(b))[-16:]:
            total += 1
    return total


def p2(a, b):
    bitmod = 2**16
    af = 16807
    bf = 48271
    mod = 2147483647
    ac = 4
    bc = 8
    ra = []
    rb = []
    total = 0
    i = 1
    while i < 5000000:
        a = a * af % mod
        if a % ac == 0:
            ra.append(a)
        b = b * bf % mod
        if b % bc == 0:
            rb.append(b)
        if len(ra) > i and len(rb) > i:
            if ra[i] % bitmod == rb[i] % bitmod:
                total += 1
                print(i)
            i += 1
    return total


a = 65
b = 8921
print(p2(a, b))
