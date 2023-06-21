s, k = input(), float(input())
if '55' in s:
    s1 = s.replace('55', str(55/k))
    print(s, s1)
else:
    print('55 not in S')
