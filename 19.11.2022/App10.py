import pandas as pd

board_df = pd.read_csv('game_board.csv')
print(board_df.loc[board_df == 1, 'J'])
print(board_df['J'])
