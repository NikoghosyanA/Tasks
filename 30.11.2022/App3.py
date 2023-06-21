lst = list(map(int, input().split()))
q = 0
while q < 2:
    for i in range(3):
        if lst[i] == lst[i+1] and lst[i] != 0:
            lst = [0] + lst[:i] + [lst[i] * 2] + lst[i+2:]
    q += 1
print(*lst)
