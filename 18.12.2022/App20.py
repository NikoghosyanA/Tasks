lst = list(map(int, input().split()))
k = int(input())
mx = 0
for i in range(len(lst)):
    for j in range(len(lst)+1):
        if j - i == k:
            if sum(lst[i:j]) > mx:
                mx = sum(lst[i:j])
print(mx)
