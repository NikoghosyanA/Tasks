def func(years, names):
    for i in range(len(names)):
        if 1900 < years[i] < 1970:
            print(f'Книга {names[i]} вышла до 1970 года')
        elif 1970 <= years[i] <= 2000:
            if str(years[i] % 100)[0] == '7':
                print(f'Книга {names[i]} вышла в семидесятые годы')
            elif str(years[i] % 100)[0] == '8':
                print(f'Книга {names[i]} вышла в восьмидесятые годы')
            elif str(years[i] % 100)[0] == '9':
                print(f'Книга {names[i]} вышла в девяностые годы')
            elif str(years[i] % 100)[0] == '0':
                print(f'Книга {names[i]} вышла в двухтысячные годы')
        elif years[i] > 2000:
            print(f'Книга {names[i]} вышла после 2000 года')
        else:
            print(f'Десятилетие книги {names[i]} не определено')

