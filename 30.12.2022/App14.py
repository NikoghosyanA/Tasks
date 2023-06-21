from collections import Counter

with open('input.txt') as fin, open('output.txt', 'w', encoding='utf-8') as fout:
    for seq in fin:
        cntr = Counter(seq)

        if sum(cnt % 2 for cnt in cntr.values()) <= len(seq) % 2:
            odd = next((k for k, v in cntr.items() if v % 2), '')
            pat = ''.join(k * (cntr[k] // 2) for k in '9876543210')
            res = 'ДА\n{}\n'.format(pat + odd + pat[::-1])
        else:
            res = 'НЕТ\n'

        fout.write(res)
