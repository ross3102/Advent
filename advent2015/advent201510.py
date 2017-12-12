num = "1113222113"

iterations = 50

for i in range(iterations):
    new = ""
    prev = num[0]
    amount = 1
    for n in num[1:]:
        if n == prev:
            amount += 1
        else:
            new += str(amount) + prev
            prev = n
            amount = 1
    new += str(amount) + prev
    num = new
print(len(num))