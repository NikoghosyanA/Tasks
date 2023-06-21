n, k = map(int, input().split())
gentlemans = [0] * n
for _ in range(k):
    debtor, creditor, indebtedness = map(int, input().split())
    gentlemans[debtor - 1] -= indebtedness
    gentlemans[creditor - 1] += indebtedness
print(*gentlemans)
