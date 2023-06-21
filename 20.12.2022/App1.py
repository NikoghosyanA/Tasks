n, k = map(int, input().split())
lst = list(map(int, input().split()))
q = int(input())
for i in range(q):
    li, ri = map(int, input().split())
    lst = lst[:li-1] + lst[li-1:ri][::-1] + lst[ri:]
print(lst[k-1])
