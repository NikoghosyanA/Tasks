s = 'Человек в 21 веке, который не будет уметь пользоваться ЭВМ, будет подобен человеку двадцатого века, не ' \
    'умевшему ни читать, ни писать.'.split()
g = 'аяуюоеёэиы'
c = 0
for i in s[-3]:
    if i in g:
        c += 1
print(c)