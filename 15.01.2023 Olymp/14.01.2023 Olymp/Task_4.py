sit = list(map(int, input().split()))
bank1, bank2, hand1, hand2 = 0, 0, 0, 0
turn = 1
while sit != [0, 0, 0, 0, 0, 0, 0]:
    if turn == 1:
        a = int(input(f'Ход {turn}-го игрока\tВыберите позицию от 1 до 7: '))
        turn = 2
        i = a - 1
        while True:
            if i == a - 1:
                hand1 += sit[i]
                sit[i] = 0
            else:
                if hand1 > 1:
                    if sit[i] == 5:
                        bank1 += 1
                        sit[i] -= 1
                    elif sit[i] < 5:
                        sit[i] += 1
                        hand1 -= 1
                elif hand1 == 1:
                    if 1 <= sit[i] <= 4:
                        bank1 += sit[i] + 1
                        hand1 -= 1
                        sit[i] = 0
                    else:
                        bank2 += 1
                        hand1 -= 1
                elif hand1 == 0:
                    break
            i += 1
            if i == 7:
                i = 0
    elif turn == 2:
        a = int(input(f'Ход {turn}-го игрока\tВыберите позицию от 1 до 7: '))
        turn = 1
        i = a - 1
        while True:
            if i == a - 1:
                hand2 += sit[i]
                sit[i] = 0
            else:
                if hand2 > 1:
                    if sit[i] == 5:
                        bank2 += 1
                        sit[i] -= 1
                    elif sit[i] < 5:
                        sit[i] += 1
                        hand2 -= 1
                elif hand2 == 1:
                    if 1 <= sit[i] <= 4:
                        bank2 += sit[i] + 1
                        hand2 -= 1
                        sit[i] = 0
                    else:
                        bank1 += 1
                        hand2 -= 1
                elif hand2 == 0:
                    break
            i += 1
            if i == 7:
                i = 0
    print(*sit, f' Bank1: {bank1}   Bank2: {bank2}', sep=' ')




