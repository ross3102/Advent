with open("in.txt", "r") as file:
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in file.readline().split(","):
        i = int(i)
        counts[i] += 1

    for day in range(256):
        zeros = counts[0]
        for i in range(8):
            counts[i] = counts[i+1]
        counts[8] = zeros
        counts[6] += zeros

    print(sum(counts))
