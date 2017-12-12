def p1(file):
    total = 0
    inGarbage = False
    char = 0
    layer = 0

    while char < len(file):
        if file[char] == "!":
            char += 1
        elif not inGarbage:
            if file[char] == "<":
                inGarbage = True
            elif file[char] == "{":
                layer += 1
            elif file[char] == "}":
                total += layer
                layer -= 1
        else:
            if file[char] == ">":
                inGarbage = False

        char += 1
    return total


def p2(file):
    total = 0
    inGarbage = False
    char = 0
    layer = 0
    p2tot = 0

    while char < len(file):
        if file[char] == "!":
            char += 1
        elif not inGarbage:
            if file[char] == "<":
                inGarbage = True
            elif file[char] == "{":
                layer += 1
            elif file[char] == "}":
                total += layer
                layer -= 1
        else:
            if file[char] == ">":
                inGarbage = False
            else:
                p2tot += 1

        char += 1
    return p2tot

file = list(open("f.txt", "r"))
print(p2(file[0]))