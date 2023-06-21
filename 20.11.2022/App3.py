with open('the_calls.txt', 'a') as f:
    the_calls_txt = f.readlines()
the_calls_lst = sorted([x.split('\t') for x in filter(lambda x: len(x), the_calls_txt)],
                       key=lambda x: (-ord(x[2]), int(x[1])), reverse=True)
calls_txt = '\n'.join('\t'.join(x) for x in the_calls_lst)
print(calls_txt)
with open('calls.txt', 'a') as f:
    f.write(calls_txt)
