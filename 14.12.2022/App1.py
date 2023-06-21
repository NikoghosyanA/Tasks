import pandas as pd

df = pd.read_csv('input.csv')
ndf = df.dropna(subset=['name'])
mn = ndf.mean(axis='index', skipna=True, numeric_only=True)
ndf = ndf.fillna(mn[0])
ndf.to_csv('output.csv', sep=',')
