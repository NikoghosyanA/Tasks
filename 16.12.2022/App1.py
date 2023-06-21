import pandas as pd

df = pd.read_csv('input.csv', sep=',')
lst = []
for i in df['temperature_c']:
    lst.append(round(((9 / 5) * i) + 32))
df['temperature_f'] = lst
df.to_csv('output.csv', index=False)
