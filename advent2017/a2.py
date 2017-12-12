file = open("f.txt", 'r')

total = 0

for line in file:
    c = False
    line = line.strip().split("\t")
    for num in line:
        if not c:
            num = int(num)
            for num2 in line:
                num2 = int(num2)
                if num != num2:
                    if num / num2 == num // num2:
                        total += num // num2
                        c = True
                        break
                    if num2 / num == num2 // num:
                        total += num2 // num
                        c = True
                        break

print(total)