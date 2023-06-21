def print_polynominal(A, n):
    string = " + ".join(f"{A[i]}x^{n - i}" for i in range(n+1) if A[i])
    return string.replace("x^0", "").replace("1x", "x").replace("+ -", "- ").replace("^1", "")


n = int(input())
lst = []
for i in range(n+1):
    lst.append(int(input()))
print(print_polynominal(lst, n))
