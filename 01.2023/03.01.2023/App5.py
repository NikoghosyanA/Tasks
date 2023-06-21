h, m, p, u, k = 8, 0, 5, 45, int(input())
mm = k * u + (k - 1) * p
dh, dm = divmod(mm, 60)
print(h + dh, m + dm)
