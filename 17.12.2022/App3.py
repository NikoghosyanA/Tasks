n = int(input())
c = 0
k = 9
while True:
    if n % (10**k) == 0 and n % (10**(k+1)) != 0:
        c += k + 1
        k = 9
        n -= 1
        if n == 0:
            break
    else:
        k -= 1
print(c)
