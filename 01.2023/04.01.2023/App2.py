import re
import itertools as i_
import operator as o_

CO = {'*': [o_.mul, 3], '+': [o_.add, 2], '-': [o_.sub, 2], '>': [o_.gt, 1]}


def toRPN(IFN):
    # - input|output: str w/o spaces | str with spaces

    stck = []
    RPN = []
    o1_ = ''

    for o1 in IFN:
        if o1.isdigit() or o1 == 'd':
            if o1_.isdigit() or o1_ == 'd':
                RPN[-1] += o1
            else:
                RPN.append(o1)
        elif o1 in CO:
            while len(stck) > 0 and (o2 := stck[-1]) != '(' and CO[o2][1] >= CO[o1][1]:
                RPN.append(stck.pop())
            stck.append(o1)
        elif o1 == '(':
            stck.append(o1)
        elif o1 == ')':
            while True:
                temp = stck.pop()
                if temp == '(': break
                RPN.append(temp)

        o1_ = o1

    if len(stck) > 0:
        RPN = RPN + stck[::-1]

    return ' '.join(RPN)


def RPNcalc(RPN):
    # - input|output: str with spaces | int
    stck = []
    RPNlst = RPN.split()

    for _ in RPNlst:
        if _ in CO:

            b, a = stck.pop(), stck.pop()
            stck.append(int(CO[_][0](a, b)))
        else:
            stck.append(int(_))

    return stck[0]


inp = input()
inpRPN = toRPN(inp)

dlim = (int(i[1:]) for i in re.findall(r'd\d+', inpRPN))
drng = tuple((*range(1, i + 1),) for i in dlim)
dgen = i_.product(*drng)
mask = re.sub(r'd\d+', '%s', inpRPN)

res0 = {}
for i in dgen:
    temp = RPNcalc(mask % i)
    res0[temp] = res0.get(temp, 0) + 1
ttlp = sum(res0.values())
resf = "\n".join((str(k) + ' {:.2f}'.format(round(v / ttlp * 100, 2)) for k, v in sorted(res0.items())))

print(resf)
