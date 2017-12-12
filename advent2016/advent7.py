file = open('f', 'r')
total = 0


def is_aba(string):
    in_brackets = False
    outside = []
    inside = []
    for char in range(len(string) - 3):
        if string[char] == "[":
            in_brackets = True
        a = string[char]
        b = string[char+1]
        if string[char+2] == a and b != a:
            if in_brackets:
                inside.append([b,a,b])
            else:
                outside.append([a,b,a])
        if string[char] == "]":
            in_brackets = False
    for x in outside:
        for y in inside:
            if x == y:
                return True
    return False

for line in file:
    if is_aba(line):
        total += 1
print(total)