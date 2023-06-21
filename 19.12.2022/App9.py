p1, p2, p3 = float(input()), float(input()), float(input())
day, month = int(input('День: ')), int(input('Месяц: '))

if p1 <= p2 and p1 <= p3:
    if month != 1 and 4 >= month >= 11 and (month == 12 and day <= 25):
        print(p1)
    else:
        if p2 <= p3:
            if (month == 2 and day <= 15) or (month == 1 and day > 24):
                if month >= 10 or month <= 5:
                    print(p3)
                else:
                    print('No')
            elif month == 12 or month <= 3:
                print(p2)
            else:
                print('No')
        else:
            if month >= 10 or month <= 5:
                print(p3)
            else:
                if (month == 2 and day <= 15) or (month == 1 and day > 24):
                    print('No')
                else:
                    print(p2)
elif p2 <= p1 and p2 <= p3:
    if (month == 2 and day <= 15) or (month == 1 and day > 24):
        if p1 <= p3:
            if month != 1 and 4 >= month >= 11 and (month == 12 and day <= 25):
                print(p1)
            else:
                if month >= 10 or month <= 5:
                    print(p3)
                else:
                    print('No')
        else:
            if month >= 10 or month <= 5:
                print(p3)
            else:
                if month != 1 and 4 >= month >= 11 and (month == 12 and day <= 25):
                    print(p1)
                else:
                    print('No')
    else:
        print(p2)
elif p3 <= p1 and p3 <= p2:
    if month >= 10 or month <= 5:
        print(p3)
    else:
        if p1 <= p2:
            if month != 1 and 4 >= month >= 11 and (month == 12 and day <= 25):
                print(p1)
            else:
                if (month == 2 and day <= 15) or (month == 1 and day > 24):
                    print('No')
                else:
                    print(p2)
        else:
            if (month == 2 and day <= 15) or (month == 1 and day > 24):
                if month != 1 and 4 >= month >= 11 and (month == 12 and day <= 25):
                    print(p1)
                else:
                    print('No')
            else:
                print(p2)
