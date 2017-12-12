file = open('f','r')

for line in file:
    print(line)
    skip = 0
    for char in range(len(line)):


        char += skip
        i