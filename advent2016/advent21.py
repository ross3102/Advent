from itertools import permutations

instructions = open("f", "r")

insts = []

for line in instructions:
    insts.append(line.split())

def combinations(string):
    perms = [list(i) for i in permutations(string)]
    return perms

combos = combinations("abcdefgh")

for s in combos:

    string = [i for i in s]

    orig = "".join(s)

    for line in insts:
        if line[0] == "swap":
            if line[1] == "position":

                index1 = int(line[2])
                index2 = int(line[5])

                letter1 = string[index1]

                string[index1] = string[index2]
                string[index2] = letter1

            elif line[1] == "letter":

                letter1 = line[2]
                index1 = string.index(letter1)

                letter2 = line[5]
                index2 = string.index(letter2)

                string[index1] = letter2
                string[index2] = letter1

        elif line[0] == "rotate":
            if line[1] == "based":
                letter = line[6]
                index = string.index(letter)

                num = 1 + index + (1 if index >= 4 else 0)

                line = ("rotate right %d steps" % num).split()
            steps = int(line[2])
            if line[1] == "left":
                string = string[steps:] + string[:steps]
            else:
                string = string[len(string)-steps:] + string[:len(string)-steps]

        elif line[0] == "reverse":
            pos1 = int(line[2])
            pos2 = int(line[4]) + 1

            string = string[:pos1] + list(reversed(string[pos1:pos2])) + string[pos2:]

        elif line[0] == "move":
            letter = string[int(line[2])]
            index = int(line[5])

            string.remove(letter)
            string = string[:index] + [letter] + string[index:]

    string = "".join(string)

    if string == "fbgdceah":
        print(orig)