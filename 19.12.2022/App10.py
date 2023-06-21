import numpy as np

data = np.loadtxt('input.csv', delimiter=',')
print(data)
avg_wins = np.mean(data, axis=0)
print(avg_wins)
print(type(list(np.floor(avg_wins * 1.5))))
data[0] = list(np.floor(avg_wins * 1.5))
print(data)
np.savetxt('output.csv', data, delimiter=',')
