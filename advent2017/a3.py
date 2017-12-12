def p1(target):
    horizDist = 0
    vertDist = 0
    number = 1
    toMove = 1
    done = False

    while not done:
        for i in range(toMove):
            number += 1
            horizDist += 1
            if number == target:
                done = True
                break
        for i in range(toMove):
            number += 1
            vertDist += 1
            if number == target:
                done = True
                break
        toMove += 1
        for i in range(toMove):
            number += 1
            horizDist -= 1
            if number == target:
                done = True
                break
        for i in range(toMove):
            number += 1
            vertDist -= 1
            if number == target:
                done = True
                break
        toMove += 1
    print(abs(horizDist) + abs(vertDist))

class Number:
    def __init__(self, x, y, value=0):
        self.x = x
        self.y = y
        self.value = value

    def getValue(self, others):
        for num in others:
            if abs(num.x-self.x) <= 1 and abs(num.y-self.y) <= 1:
                self.value += num.value

def p2(target):
    x = 0
    y = 0
    value = 1
    numbers = [Number(x, y, value)]

    toMove = 1

    while True:
        for i in range(toMove):
            x += 1
            newNum = Number(x, y)
            newNum.getValue(numbers)
            numbers.append(newNum)
            if newNum.value >= target:
                return newNum.value
        for i in range(toMove):
            y += 1
            newNum = Number(x, y)
            newNum.getValue(numbers)
            numbers.append(newNum)
            if newNum.value >= target:
                return newNum.value
        toMove += 1
        for i in range(toMove):
            x -= 1
            newNum = Number(x, y)
            newNum.getValue(numbers)
            numbers.append(newNum)
            if newNum.value >= target:
                return newNum.value
        for i in range(toMove):
            y -= 1
            newNum = Number(x, y)
            newNum.getValue(numbers)
            numbers.append(newNum)
            if newNum.value >= target:
                return newNum.value
        toMove += 1


target = 1023
p1(target)
# print(p2(target))
