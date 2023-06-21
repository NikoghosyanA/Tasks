a = ''
with open('input.txt', 'r') as f:
    for i, line in enumerate(f):
        if i == 0:
            continue
        else:
            a = line
with open('output.txt', 'w') as f:
    f.write(str(bin(int(a, base=16))[2:].count('0')))
