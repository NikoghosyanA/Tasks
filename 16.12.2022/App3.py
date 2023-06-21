import pandas as pd
import numpy as np

df = pd.read_csv('input.csv')
ndf = df.to_numpy()
print(ndf)
lst = np.mean(ndf, axis=0)
lst = [float(i) for i in lst]
print(lst.index(min(lst)) + 1)
