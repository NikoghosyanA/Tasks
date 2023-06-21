def common_suffix_length(str1, str2):
    i, j, length = -1, -min(len(str1), len(str2)), 0
    while i >= j and str1[i] == str2[i]:
        length += 1
        i -= 1
    return length


lst = [input() for _ in range(4)]
print(max(common_suffix_length(lst[0], lst[2]), common_suffix_length(lst[1], lst[3])))
