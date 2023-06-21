n = int(input())
lst = list(map(int, input().split()))
lst1 = [0 for i in range(n)]
c = 0
for i in range(n):
    ln1, ln2 = False, False
    for j in range(1, n):
        if lst[i] == max(lst):
            lst1[i] = i+1
            break
        else:
            if not ln1:
                if i + j <= n - 1:
                    if lst[i] < lst[i+j]:
                        ln1 = j
                else:
                    ln1 = n
            if not ln2:
                if i - j >= 0:
                    if lst[i] < lst[i-j]:
                        ln2 = j
                else:
                    ln2 = n
        if ln1 and ln2:
            if ln1 > ln2:
                lst1[i] = i - ln2 + 1
                break
            elif ln1 < ln2:
                lst1[i] = i + ln1 + 1
                break
            else:
                lst1[i] = i + j + 1
                break
print(*lst1)
