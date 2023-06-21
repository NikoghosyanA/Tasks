s = input()
s1 = float(s)
if int(s1) % 10 != 9 and s1 - int(s1) < 0.5:
    print(int(s1))
elif int(s1) % 10 != 9 and s1 - int(s1) >= 0.5:
    print(int(s1) + 1)
elif int(s1) % 10 == 9 and s1 - int(s1) < 0.5:
    print('GOTO Vasilisa')
