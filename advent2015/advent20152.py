file = open('f','r')
total = 0
for line in file:
    line = line.split("x")
    length = int(line[0])
    width = int(line[1])
    height = int(line[2])
    sides = [(length,width), (width,height), (length,height)]
    newl = []
    for x in sides:
        newl.append(2*x[0] + 2*x[1])
    smallest= min(newl)
    total += smallest + length * width * height
    # sides = [2*length*width, 2*length*height, 2*width*height]
    # smallest = min(sides)
    # total += (sum(sides) + .5*smallest)

print("The elves will need %d square feet of ribbon" % total)