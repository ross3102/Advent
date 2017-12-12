file = open('f','r')
total = 0
newfile = []
asd = 0
for line in file:
    line = line.strip()
    newfile.append(line)
    chars = {}
    for char in line[:-11]:
        if char != '-':
            chars[char] = line[:-11].count(char)
    maximums = ["wao;eifjaw;ofjfijwfoij"]
    for x in chars:
        maxchars = []
        for g in maximums:
            maxchars.append(chars.get(g, 0))
            if 0 in maximums:
                maximums = []
        if chars[x] > min(maxchars):
            tobeadded = []
            for y in chars:
                if chars[x] == chars[y] and x != y:
                    tobeadded.append(y)
            tobeadded.append(x)
            tobeadded.sort()
            for y in range(len(maximums)):
                if chars.get(tobeadded[0]) >= chars.get(maximums[y],0):
                    position = y
                    break
            tobeadded = tobeadded[::-1]
            for x in tobeadded:
                if x not in maximums:
                    maximums.insert(position,x)
    while len(maximums) > 5:
        del maximums[-1]
    if "".join(maximums) == line[-6:-1]:
        total += int(line[-10:-7])
    else:
        line = "".join(line)
        newfile.remove(line)
for line in newfile:
    temptot = int(line[-10:-7])
    newword = []
    forward = temptot % 26
    for i in line[:-7]:
        if i not in '-0123456789':
            new = ord(i) + forward
            if new > 122:
                new -= 26
            newword.append(chr(new))
        elif i == "-":
            newword.append(" ")
        elif i in "0123456789":
            newword.append(i)
    newword = "".join(newword)
    if 261 <= temptot <= 599:
        print("".join(newword))