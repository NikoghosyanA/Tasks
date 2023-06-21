n = int(input())
lst = list(map(int, input().split()))
for i in range(n-1):
    for j in range(n):
        if j > i:
            if sum(lst[i:j]) % n == 0:
                print(i+1, j)
