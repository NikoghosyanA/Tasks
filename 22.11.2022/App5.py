def f(s):
    for i in range(0, len(s)):
        tmp = f'{s[:i]}{s[i:i + 2][::-1]}{s[i + 2:]}'
        if tmp == tmp[::-1]:
            return True
    return False


print(f(input()))
