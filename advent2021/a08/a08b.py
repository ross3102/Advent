with open("i08.txt", "r") as file:
    total = 0
    for line in file:
        inp, out = [side.split() for side in line.strip().split(" | ")]
        
        decoded = [""] * 10
        
        for i in inp:
          if len(i) == 2:
            decoded[1] = i
          elif len(i) == 3:
            decoded[7] = i
          elif len(i) == 4:
            decoded[4] = i
          elif len(i) == 7:
            decoded[8] = i

        for i in inp:
          if len(i) == 5:
            if all(c in i for c in decoded[1]):
              decoded[3] = i
            elif len([c for c in i if c in decoded[4]]) == 3:
              decoded[5] = i
            else:
              decoded[2] = i
          elif len(i) == 6:
            if any(c not in i for c in decoded[7]):
              decoded[6] = i
            elif all(c in i for c in decoded[4]):
              decoded[9] = i
            else:
              decoded[0] = i
        
        ans = 0

        for i in out:
          for n in range(10):
            d = decoded[n]
            if len(i) == len(d) and all(c in d for c in i):
              ans = ans*10+n
        total += ans
        
    print(total)
