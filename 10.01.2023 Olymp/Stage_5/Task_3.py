n, w = map(int, input().split())
weight = list(map(int, input().split()))
happiness = list(map(int, input().split()))

for i in range(n - 1):
    for j in range(n - i - 1):
        if happiness[j] < happiness[j + 1]:
            happiness[j], happiness[j + 1] = happiness[j + 1], happiness[j]
            weight[j], weight[j + 1] = weight[j + 1], weight[j]

sm = 0
for i in range(n):
    if weight[i] <= w:
        sm += happiness[i]
        w -= weight[i]
print(sm)
