import numpy as np
from math import pi


a = np.array([[1,23,-5],[32,0.45,-90],[45,89,pi]])

b = np.array([pi, 34 * pi, -90])


solution = np.linalg.solve( a , b )

print(solution)