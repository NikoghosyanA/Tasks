n = input()
nums = list(map(int, input().split()))
s = 0
for i in nums:
    if i % 2 == 0:
        s += i
print(s)
