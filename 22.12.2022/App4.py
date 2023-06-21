t = 0
for ch in input():
    t |= ch.isdigit() + 2 * ch.islower() + 4 * ch.isupper()
print('domestic' if t == 7 else 'wild', 'animal')
