n = int(input())
lst = list(map(int, input().split()))
s, s1, s2, answer = sum(lst), 0, 0, [0] * n
answer[0] = answer[-1] = str(s)
for i in range(1, (n + 1) // 2):
    tmp = lst[i - 1] + lst[-i]
    s1 += tmp
    s2 += tmp * i
    answer[i] = answer[-i - 1] = str((s - s1) * (i + 1) + s2)
print(' '.join(answer))
