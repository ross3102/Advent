import hashlib

def toMD5(salt, index):
    string = salt + str(index)
    for i in range(2017):
        string = hashlib.md5(string.encode("utf-8")).hexdigest()
    return string

def repeat(string):
    for i in range(1, len(string) - 1):
        if string[i-1] == string[i] and string[i+1] == string[i]:
            return string[i]
    return False

def repeatChar(string, char):
    for i in range(2, len(string) - 2):
        if string[i] == char and string[i-1] == char and string[i-2] == char and string[i+1] == char and string[i+2] == char:
            return True
    return False

def checkNext(char, salt, index):
    for i in range(index, index + 1000):
        str = toMD5(salt, i)
        if repeatChar(str, char):
            return True
    return False

salt = "jlmsuwbz"

index = 0

found = 0

while found != 64:
    string = toMD5(salt, index)
    character = repeat(string)
    if character != False:
        if checkNext(character, salt, index + 1):
            found += 1
            print(found, ": \t", index)
    index += 1