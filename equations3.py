import numpy as np
A = np.array([[3, -9], [2, 4]])   #3y -9x = -42     2y - 4x= 2
b = np.array([-42, 2])
solution = np.linalg.solve(A, b)
print(solution)

B = np.array([[3, -9, -2], [2, 4, 1], [3, 4, 6]])   # 3 ecuaciones 3 incognitas
c = np.array([-42, 2, 5])
solutionb = np.linalg.solve(B, c)
print(solutionb)