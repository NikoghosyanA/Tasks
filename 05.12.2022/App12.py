def integerSqrt(n):
    if n < 2:
        return n
    else:
        smallCandidate = integerSqrt(n >> 2) << 1
        largeCandidate = smallCandidate + 1
        if largeCandidate * largeCandidate > n:
            return smallCandidate
        else:
            return largeCandidate


n = int(input())
m = integerSqrt(n - 1)
k = (m * (m + 1) + 1)
if m % 2 == 1:
    if k < n:
        row = m + 1
        col = (m + 1) - (n - k)
    elif k == n:
        row = m + 1
        col = m + 1
    else:
        col = m + 1
        row = (m + 1) + (n - k)
else:
    if k < n:
        col = m + 1
        row = (m + 1) - (n - k)
    elif k == n:
        row = m + 1
        col = m + 1
    else:
        row = m + 1
        col = (m + 1) + (n - k)
print(row, col)
