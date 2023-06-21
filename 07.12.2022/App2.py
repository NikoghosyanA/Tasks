pens = round(float(input()) * 240)
funt = pens // 240
shil = (pens - (funt * 240)) // 12
pens = (pens - (funt * 240) - (shil * 12)) % 20
print('£' + str(funt) + '.' + str(shil) + '.' + str(pens))
