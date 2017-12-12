file = list(open("f.txt", "r"))[0]

total = 0

length = len(file)

wrap = length // 2

for char in range(length):
    if file[char] == file[(char+wrap) % length]:
        total += int(file[char])

print(total)

# One-liner replaces for loop
print(sum([int(file[char]) for char in range(length) if file[char] == file[(char+wrap) % length]]))