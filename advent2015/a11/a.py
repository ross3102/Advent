def increment(pw):
    for i in range(len(pw) - 1, -1, -1):
        if pw[i] == "z":
            pw[i] = "a"
        else:
            pw[i] = chr(ord(pw[i]) + 1)
            if pw[i] in "oil":
                pw[i] = chr(ord(pw[i]) + 1)
            return pw


def valid(pw):
    hasIncr = False
    for i in range(len(pw) - 2):
        if ord(pw[i+2]) == 1+ord(pw[i+1]) and ord(pw[i+1]) == 1+ord(pw[i]):
            hasIncr = True
            break
    if not hasIncr:
        return False

    for i in range(len(pw) - 1):
        if pw[i] == pw[i+1]:
            for j in range(i+2, len(pw) - 1):
                if pw[j] == pw[j+1]:
                    return True
    return False


with open("b.txt", "r") as file:
    pw = list(file.readline())

while not valid(pw):
    pw = increment(pw)

print("".join(pw))
