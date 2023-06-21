def f(s):
    ss = 'qwertyuiopasdfghjklzxcvbnm'
    if s in ss:
        return True
    else:
        return False


print(f(input().lower()))

