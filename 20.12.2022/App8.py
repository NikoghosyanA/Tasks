def any_base_to_decimal(number, base):
    temp = int(number, base)
    return temp


n = input()
n1 = any_base_to_decimal(n, 6)
c = 0
for i in set(list(str(n1))):
    if i not in n:
        c += 1
print(c)
