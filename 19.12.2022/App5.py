n = input()
k = int(input())
with open('input.csv', 'r') as f1:
    with open('output.txt', 'a') as f2:
        for i in f1:
            if k == 0:
                f2.write(n + '\n')
            k -= 1
            f2.write(i+'\n')
