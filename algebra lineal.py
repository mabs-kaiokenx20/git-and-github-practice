import numpy as np
from math import pi
import sys

sys.path.append('/home/mabs-trc/proyecto/moddules')

from moddules import funtionmath as fm

x = fm.coseno(23)

print(x + 34)

y = fm.seno(23)

print(y + 2)

a = np.array([[1,23,-5],[32,0.45,-90],[45,89,pi]])

b = np.array([pi, 34 * pi, -90])


solutio = np.linalg.solve( a , b )

print(solutio)