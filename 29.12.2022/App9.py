a, b, c = input(), input(), input()
lst1 = [a, b, c]
lst2 = [len(a), len(b), len(c)]
ans = ''
for i in range(3):
    if lst2[i] == max(lst2):
        if lst1[i] > ans:
            ans = lst1[i]
print(ans, len(ans))
