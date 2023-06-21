f = open('f.txt', 'r')
g = open('g.txt', 'a')
for line in f:
    lne = line.replace('!', '.')
    g.write(lne)
f.close()
g.close()
