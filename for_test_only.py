import numpy as np

a = np.array([[6, -6, -1], [4, 10, 0], [4, 4, -1]])
b = np.array([0, 10, 0])
print(np.linalg.solve(a, b))