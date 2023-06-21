K1, M, K2, P2, N2 = int(input()), int(input()), int(input()), int(input()), int(input())
dann = [K1, M, K2, P2, N2]


def round_up(v, d):
    result = v // d + (1 if v % d else 0)
    return result


def find(room_1, max_level, room_old, p_old, level_old):
    count_room_for_level = 0
    # Определим количество квартир на этаже
    if max_level == 1 and p_old == 1:
        return 1, 1

    for count_room_for_level in range(40):
        if ((level_old - 1) * count_room_for_level) * p_old < room_old < (count_room_for_level * level_old) * p_old:
            print(count_room_for_level)
            break
    else:
        return -1

    # Определим возможный подъезд
    p_new = round_up(room_1, (max_level * count_room_for_level))
    # Этаж
    level_new = round_up(room_1, count_room_for_level) % max_level
    print(p_new, level_new)
    return p_new, level_new


print(list(find(*dann)))
