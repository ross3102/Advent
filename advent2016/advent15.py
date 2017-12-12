bits = "11101000110010100"

DRIVE_SIZE = 35651584

FLIP = {
    "0": "1",
    "1": "0"
}

def dragon(a):
    b = [bit for bit in a[::-1]]
    for bit in range(len(b)):
        b[bit] = FLIP[b[bit]]
    return a + "0" + "".join(b)

def checksum(b):
    new = ""
    for bit in range(0, len(b), 2):
        if b[bit] == b[bit + 1]:
            new += "1"
        else:
            new += "0"
    return new

while len(bits) < DRIVE_SIZE:
    bits = dragon(bits)
bits = bits[:DRIVE_SIZE]

while len(bits) % 2 == 0:
    bits = checksum(bits)
print(bits)