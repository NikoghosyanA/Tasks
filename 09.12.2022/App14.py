n_finish = 73
S_min = 1
S_max = 23
move_vals = [3, 13, 23]
move_val_min = move_vals[0]  # 3
move_val_max = move_vals[-1]  # 23
move_val_min_max = move_val_min + move_val_max  # 26


def Petya_purposely_loses_on_2_move(S):
    n = S * 3 + 2
    rem = n_finish - n
    return move_val_min + 1 <= rem <= move_val_max * 2


def Petya_purposely_loses_on_4_move(S):
    n = S * 3 + 2
    rem = n_finish - n
    return move_val_max + move_val_min * 2 + 1 <= rem <= move_val_max * 4


def Petya_purposely_loses_on_2_and_4_move(S):
    return Petya_purposely_loses_on_2_move(S) \
           and Petya_purposely_loses_on_4_move(S)


def Petya_is_guaranteed_win_on_second_move(S):
    n = S * 3 + 2
    rem = n_finish - n
    rem -= move_val_min_max
    return 0 < rem <= move_val_max


S_values = [x for x in range(S_min, S_max + 1)]
S_P_g_win = list(filter(Petya_is_guaranteed_win_on_second_move, S_values))
print('Значения S, при которых Петя выигрывает вторым ходом при любом ходе Вани:')
print(S_P_g_win)
print()
S_P_loses_2_4 = list(filter(Petya_purposely_loses_on_2_and_4_move, S_values))
print('Значения S, при которых Петя может намеренно проиграть Ване, при этом выбрав,')
print('сделать это на втором или четвертом ходу:')
print(S_P_loses_2_4)
