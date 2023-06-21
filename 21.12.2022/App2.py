def to_rescue(stroka, additional='-'):
    for i in range(len(need_help)):
        s = ''
        for j in need_help[i]:
            if j not in stroka:
                if j not in s:
                    s += j
        ls = sorted(list(s))
        s = ''.join(ls)
        if len(s) < len(stroka):
            s += (len(stroka) - len(s)) * additional
        need_help[i] = s
    return need_help


need_help = ['tears', 'flowed', 'from', 'the', 'owls', 'yellow', 'eyes']
to_rescue('large', additional='*')
print(need_help)
need_help = ['owl', 'was', 'crying', 'bitterly']
to_rescue('caliph')
print(need_help)
