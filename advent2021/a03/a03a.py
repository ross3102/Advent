with open("i03.txt", "r") as file:
    total = 0
    line = file.readline().strip()
    ones = [0] * len(line)
    while line:
        total += 1
        for i in range(len(line.strip())):
            if line[i] == "1":
                ones[i] += 1
        line = file.readline().strip()
    
    gamma = "".join("1" if n > total//2 else "0" for n in ones)
    epsilon = "".join("0" if i == "1" else "1" for i in gamma)

    print(int(gamma, 2) * int(epsilon, 2))
    
