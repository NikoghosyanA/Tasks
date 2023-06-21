def middle_result(dct, base, arg=1):
    summ = 0
    for k, v in dct.items():
        summ += v
    mid = summ / len(dct.keys())
    if mid < 3.5:
        return 'Стипендия не выплачивается'
    elif 3.5 <= mid < 4.5:
        return base * arg
    elif 4.5 <= mid <= 5:
        return base * (1.5 * arg)
