s1 = ['МДММДМД',
      'МММММММДДДДДДДД',
      'ММММММММММДДДДДДДДДДММММММММММДДДДДДДДДДММММММММММДДДДДДДДДД',
      'МДММДДМММДДДММММДДДДМММММДДДДДММММММДДДДДД',
      'МДМДМДМДМДМДМДМДМДМДМДМДМДМДМДМДМДМДМДМДМДМДМДМДМДМДМДМДМДМДМДМДМДМДМДМДМДМДМДМД']


def bubblesort(arr, c=0):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                c += 1
        if not swapped:
            return
    print(c)


for i in s1:
    s = list(i)
    bubblesort(s)
    print(''.join(s))
    print()
