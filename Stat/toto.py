import numpy as np
from numpy.random import sample
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
 
""" Loi binomiale de parametres n et p """
n, p = 20, 0.5
y = np.zeros(n)
 
fig = plt.figure()
line, = plt.plot(np.arange(n), y, drawstyle='steps-post')
plt.ylim(0, 1)
 
def updatefig(*args):
    idx = np.sum(sample(n) <= p)
    y[idx] += 1
    line.set_ydata(y / y.sum())
 
ani = animation.FuncAnimation(fig, updatefig, interval=5)
plt.show()