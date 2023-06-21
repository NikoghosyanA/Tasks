lst = []
lst.append('a')
lst.append('b')
lst.extend(['c', 'e'])
lst = lst[:-1] + ['d'] + ['e']
print(lst)
