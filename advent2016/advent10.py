origfile = open('f','r')
file = []
found = False
held_chips = {}
outputs = {}
for x in range(21):
    outputs[str(x)] = []
print(outputs)
for x in range(210):
    held_chips[str(x)] = []
for line in origfile:
    file.append(line)

while not found:
    for line in file:
        line = line.split()
        # print(line)
        if line[0] == "value":
            if line[1] not in held_chips[line[-1]] and "string" not in held_chips[line[-1]]:
                held_chips[line[-1]].append(line[1])
        else:
            if len(held_chips[line[1]]) == 2:
                if '61' in held_chips[line[1]] and '17' in held_chips[line[1]]:
                    print(line[1])
                if "string" not in held_chips[line[1]]:
                    teest = []
                    for stringnum in held_chips[line[1]]:
                        teest.append(int(stringnum))
                    print(line[5])
                    print(line[10])
                    if line[5] == "bot":
                        held_chips[line[6]].append(str(min(teest)))
                    else:
                        print(outputs)
                        print("cool")
                        outputs[line[6]].append(str(min(teest)))
                    if line[10] == "bot":
                        held_chips[line[11]].append(str(max(teest)))
                    else:
                        print(outputs)
                        print("cool")
                        outputs[str(line[11])].append(str(max(teest)))
                    held_chips[line[1]] = ["string"]
    tot = 0
    for g in held_chips:
        if "string" not in held_chips[g]:
            tot += 1
    if tot == 0:
        found = True
print(int(outputs['0'][0])*int(outputs['1'][0])*int(outputs['2'][0]))