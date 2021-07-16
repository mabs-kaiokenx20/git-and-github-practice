import math as m
import random as rn
import matplotlib.pyplot as plt
import numpy as np


def cos_plot():
    x = np.linspace(-150 , 150, num=1000)
    y = np.cos(x)
    ax = plt.subplot()
    plt.ylim(-2,2)
    plt.xlim(-150,150)
    ax.plot (x,y)
    ax.axhline(color='r')
    ax.axvline(color='r')
    ax.grid()
    plt.show()
    
def seno(x):
    return m.sin(x)

def coseno(x):
    return m.cos(x)

def list_random():
    x = rn.randint(1, 1264724)
    return x 
