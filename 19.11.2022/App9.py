from itertools import repeat, takewhile

astronauts = list(filter(lambda x: 150 <= x <= 190, takewhile(lambda x: x != "!", map(lambda x: x(), repeat(input)))))
print(len(astronauts))
print(min(astronauts), max(astronauts))
