with open('input.txt', 'r') as f:
    n = 0
    mn, mx = 1000000, -1000000
    for i, line in enumerate(f):
        if i == 0:
            n = int(line)
        else:
            mn, mx = float(min(line.split())), float(max(line.split()))
            for j in line.split():
                if float(j) < mn:
                    mn = float(j)
                if float(j) > mx:
                    mx = float(j)
            print(mn, mx)

