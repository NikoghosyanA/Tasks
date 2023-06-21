import numpy as np
from scipy.optimize import linprog

c = [-30, -20, -70]
A_ub = np.array([[-20, -70, -180],
                 [-10, -6, -3],
                 [10, 6, 3]])
A_eq = np.array([[4, 3, 2]])
b_ub = np.array([-2000, -210, 235])
b_eq = np.array([87])
res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq)
print(*res['x'], sep='\n')
