n, m, k = map(int, input().split())
lst = list(map(int, input().split()))
kls = list(map(int, input().split()))
lst1 = lst.copy()
ans = []
for k in kls:
    a = []
    for i in range(n):
        for j in range(n+1):
            if j - i == m:
                s = sorted(lst[i:j])
                a.append(s[k-1])
    ans.append(a)
for i in ans:
    print(max(i), end=' ')
