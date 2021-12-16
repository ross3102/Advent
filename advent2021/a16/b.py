class BitStream:
    def __init__(self, bits):
        self.bits = bits
        self.ind = 0

    def read(self, numbits):
        ret = self.bits[self.ind:self.ind+numbits]
        self.ind += numbits
        return ret

    def empty(self):
        return self.ind == len(self.bits)


class Literal:
    def __init__(self, val, ver):
        self.val = val
        self.ver = ver

    def sumver(self):
        return self.ver

    def eval(self):
        return self.val


class Operation:
    def __init__(self, l, ver, typ):
        self.l = l
        self.ver = ver
        self.typ = typ

    def sumver(self):
        return self.ver + sum([p.sumver() for p in self.l])

    def eval(self):
        if self.typ == 0:
            return sum(p.eval() for p in self.l)
        elif self.typ == 1:
            ans = 1
            for p in self.l:
                ans *= p.eval()
            return ans
        elif self.typ == 2:
            return min(p.eval() for p in self.l)
        elif self.typ == 3:
            return max(p.eval() for p in self.l)
        elif self.typ == 5:
            return 1 if self.l[0].eval() > self.l[1].eval() else 0
        elif self.typ == 6:
            return 1 if self.l[0].eval() < self.l[1].eval() else 0
        elif self.typ == 7:
            return 1 if self.l[0].eval() == self.l[1].eval() else 0


def parse_packet(bits: BitStream):
    ver = int(bits.read(3), 2)
    typ = int(bits.read(3), 2)

    if typ == 4:
        lit = ""
        while bits.read(1) == "1":
            lit += bits.read(4)
        lit += bits.read(4)
        num = int(lit, 2)
        return Literal(num, ver)
    else:
        if bits.read(1) == "0":
            pktsize = int(bits.read(15), 2)
            newbits = BitStream(bits.read(pktsize))
            l = []
            while not newbits.empty():
                l.append(parse_packet(newbits))
            return Operation(l, ver, typ)
        else:
            numpkt = int(bits.read(11), 2)
            l = []
            for _ in range(numpkt):
                l.append(parse_packet(bits))
            return Operation(l, ver, typ)


s = ""
with open("in.txt", "r") as file:
    s = file.readline()

bits = str(bin(int(s, 16)))[2:]
bits = "0" * (4-((len(bits)-1) % 4+1)) + bits

p = parse_packet(BitStream(bits))
print(p.eval())
