with open('test.txt') as f:
    text = f.read()
prices = map(lambda x: int(x.split()[1]), text.splitlines())
print(min(prices))
