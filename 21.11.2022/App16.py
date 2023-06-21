N = int(input())

csv = []
alphabet = '0abcdefghijklmnopqrstuvwxyz'

for i in range(N):
    f = list(map(str, input().split()))
    csv += f

for i in csv:
    full_name_date = i.split(',')
    full_name = full_name_date[0] + full_name_date[1] + full_name_date[2]
    len_full_name = len(set([char for char in full_name]))

    d_m = full_name_date[3] + full_name_date[4]
    sum_d_m = sum([int(char) for char in d_m])

    index_first_char = alphabet.find(full_name[0].lower())

    result_decimal = len_full_name + sum_d_m * 64 + index_first_char * 256
    result_hexadecimal = hex(result_decimal)[2:].upper()

    if len(result_hexadecimal) >= 3:
        print(result_hexadecimal[-3:], end=' ')
    elif len(result_hexadecimal) < 3:
        while len(result_hexadecimal) < 3:
            result_hexadecimal = '0' + result_hexadecimal
        print(result_hexadecimal[-3:], end=' ')
