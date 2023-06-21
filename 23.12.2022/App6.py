sname, name, grade = [], [], []
with open('input.txt', 'r') as file:
    k = 0
    for i, line in enumerate(file):
        if i == 0:
            k = int(line)
        else:
            a, b, c = map(str, line.split())
            if int(c) > k:
                sname.append(a)
                name.append(b)
                grade.append(int(c))
with open('output.txt', 'a') as wfile:
    for i in range(len(grade)+1):
        if i != len(grade):
            wfile.write(f'{i+1}) {name[i][0]}. {sname[i]}\n')
        else:
            wfile.write(str(len(grade)))
