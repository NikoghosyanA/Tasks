region = input()
c1, c2 = 0, 0
with open('olymp.csv', 'r', encoding='utf-8') as file:
    for line in file:
        if region in line:
            c1 += 1
            if 'Победитель' in line:
                c2 += 1
print(round((c1/c2) * 100))
