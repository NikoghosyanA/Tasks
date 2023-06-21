with open('__test_in.txt') as file:
    f, m = set(), set()
    for line in file.readlines():
        kind, gender, *_ = line.split()[1:]
        if gender == 'female':
            f.add(kind)
        if gender == 'male':
            m.add(kind)
    print(len(f.intersection(m)))
