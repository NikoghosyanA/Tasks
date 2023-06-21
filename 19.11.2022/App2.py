from math import cos, sin

answer1 = 0
while len(str((number := int(input())))) == 5:
    answer1 = answer1 + sin(number) if answer1 else sin(number)
print(answer1)

count = 0
mx = -1
while cos(number := int(input())) > 0:
    count += 1
    if cos(number) > mx:
        mx = cos(number)
print(count, mx)

psum, osum = 0, 0
while len(str((number := int(input())))) == 2:
    if number > 0:
        psum += number
    else:
        osum += number
print(psum, osum)

mn = []
while (number := int(input())) > 0:
    mn.append(number)
mn = sorted(mn)
print(mn[0], mn[1])
