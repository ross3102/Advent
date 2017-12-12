num = 3001330

b = bin(num)

flip = {
    "0": "1",
    "1": "0"
}

flipped = int("".join([flip[bit] for bit in str(b)[2:]]), 2)

print(num - flipped)