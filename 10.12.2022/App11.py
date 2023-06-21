s = list(map(str, input().split()))
n = int(input())
if n <= len(s):
    print(s[n-1])
    for i in s:
        if len(i) == len(s[n-1]):
            print(i)
else:
    print('N больше кол-ва слов')
