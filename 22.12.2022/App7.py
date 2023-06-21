def ordinaldate(d, m, y):
    y_is_leap = y % 400 == 0 or y % 4 == 0 and y % 100 != 0
    month_days = [31, 28 + y_is_leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    md = 0
    for i in range(m - 1):
        md += month_days[i]
    return md + d


d, m, y = list(map(int, input('день, месяц, год: ').split()))
print(f'Порядковый номер дня в году: {ordinaldate(d, m, y)}\n')
