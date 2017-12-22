from math import sqrt

class Enhancement:
    def __init__(self, before, after):
        self.before = before
        self.after = after

        self.permutations = []

        self.permutations.append(self.before)

        self.permutations.append(self.before[::-1])

        self.permutations.append([self.before[i][::-1] for i in range(len(self.before))])

        rotatedRight = []
        rotatedRightF = []
        rotatedLeft = []
        rotatedLeftF = []
        for i in range(len(self.before)):
            j = len(self.before) - 1 - i
            rotatedRight.append("".join([r[i] for r in self.before])[::-1])
            rotatedRightF.append("".join([r[i] for r in self.before]))
            rotatedLeft.append("".join([r[j] for r in self.before]))
            rotatedLeftF.append("".join([r[j] for r in self.before])[::-1])
        self.permutations.append(rotatedRight)
        self.permutations.append(rotatedLeft)
        self.permutations.append(rotatedRightF)
        self.permutations.append(rotatedLeftF)

        self.permutations.append([i[::-1] for i in self.before[::-1]])


def joinBlocks(splitImages, sliceWidth):
    rowLen = int(sqrt(len(splitImages)))
    newimage = []
    for row in range(rowLen):
        for column in range(sliceWidth):
            line = ""
            for r in range(rowLen):
                line += splitImages[row*rowLen+r][column]
            newimage.append(line)
    return newimage


def draw(file):
    enhancements = []
    for e in file:
        e = e.strip().split(" => ")
        b = e[0].split("/")
        a = e[1].split("/")
        enhancements.append(Enhancement(b, a))

    image = [
        ".#.",
        "..#",
        "###"
    ]

    for iteration in range(18):  # p1: 5
        sliceWidth = 2 if len(image) % 2 == 0 else 3
        splitImages = []
        for row in range(len(image) // sliceWidth):
            for column in range(len(image) // sliceWidth):
                currentImage = []
                for rowOffset in range(sliceWidth):
                    currentImage.append(image[sliceWidth*row+rowOffset][sliceWidth*column:sliceWidth*column+sliceWidth])
                splitImages.append(currentImage)
        for s in range(len(splitImages)):
            for e in enhancements:
                if splitImages[s] in e.permutations:
                    splitImages[s] = e.after
                    break
        image = joinBlocks(splitImages, sliceWidth + 1)

    return sum([i.count("#") for i in image])


file = list(open("f.txt", "r"))
print(draw(file))