board = []
for i in range(8):
    board.append(input())


board = ''.join(board)  # to flat
squares = range(len(board))  # 64 squares
R = [divmod(i, 8) for i in squares if board[i] == 'R']
B = [divmod(i, 8) for i in squares if board[i] == 'B']


def under_attak(pos, R, B):
    attak = False
    for fig in R:
        if not (pos[0] - fig[0]) * (pos[1] - fig[1]):
            attak = True
            break
    for fig in B:
        if abs(pos[0] - fig[0]) == abs(pos[1] - fig[1]):
            attak = True
            break
    return attak


pos_under_attak = [under_attak(divmod(i, 8), R, B) for i in squares]
print(64 - sum(pos_under_attak))