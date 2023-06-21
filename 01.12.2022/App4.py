s = input()
q = int(input())
for _ in range(q):
    i, j, k = map(int, input().split())
    ss = s[i:j+1]
    s = s[:i] + s[j+1:]
    s = s[:k] + ss + s[k:]
print(s)
