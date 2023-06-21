lst = [1, 2, 3, 4, 5]
lst[0], lst[1], lst[2] = sum(lst[0:3]), sum(lst[0:3]), sum(lst[0:3])
lst.append(7)
lst = lst[1:-1] + [lst[0]] + [lst[-1]]
print(lst)
