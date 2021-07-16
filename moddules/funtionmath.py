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

def to_print():
    print('''
        Under the arc of a weather stain boards
        Ancient goblins, and warlords
        Come out the ground, not making a sound
        The smell of death is all around
        And at night when the cold wind blows
        No one cares, nobody knows
        I don't wanna be buried in a pet cemetery
        I don't want to live my life again
        I don't wanna be buried in a pet cemetery
        I don't want to live my life again
        Follow Victor to the sacred place
        This ain't a dream, I can't escape
        Molars and fangs, the clicking of bones
        Spirits moaning among the tombstones
        And at night, when the moon is bright
        Someone cries, something ain't right
        I don't wanna be buried in a pet cemetery
        I don't want to live my life again
        I don't wanna be buried in a pet cemetery
        I don't want to live my life again
        The moon is full, the air is still
        All of the sudden I feel a chill
        Victor is grinning, flesh is rotting away
        Skeletons dance, I curse this day
        And at night when the wolves cry out
        Listen close and you can hear me shout
        I don't wanna be buried in a pet cemetery
        I don't want to live my life again
        I don't wanna be buried in a pet cemetery
        I don't want to live my life again
        Oh, no, oh, no
        I don't want to live my life, not again
        Oh, no, oh, oh
        I don't want to live my life, not again
        Oh, no, no, no
        Don't want to live my life, not again
            
    ''')