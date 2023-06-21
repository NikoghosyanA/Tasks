import calendar

cal = calendar.Calendar()
nums = list(map(int, input().split()))
y = int((input().split(','))[0])
k = int(input())
c = 0
for year in range(y, y * 2):
    for month in range(1, 13):
        for day in cal.itermonthdays(year, month):
            if day != 0:
                for i in nums:
                    if day % i != 0 and calendar.weekday(year, month, day) != 6 and calendar.weekday(year, month, day) + month % 10 != 0:
                        print(str(year) + ',' + str(day) + ',' + str(month))
                        c += 1
                    if c == k:
                        break
            if c == k:
                break
        if c == k:
            break
    if c == k:
        break
