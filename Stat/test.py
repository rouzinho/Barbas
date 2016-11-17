
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update_line(num, data, line):
    line.set_data(data[...,:num])
    return line,

fig1 = plt.figure()

data = np.random.rand(2, 25)
l, = plt.plot([], [], 'r-')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('x')
plt.title('test')
line_ani = animation.FuncAnimation(fig1, update_line, 25, fargs=(data, l),
    interval=50, blit=True)
plt.show()
#line_ani.save('lines.mp4')

fig2 = plt.figure()

x = np.arange(-9, 10)
y = np.arange(-9, 10).reshape(-1, 1)
base = np.hypot(x, y)
ims = []
for add in np.arange(15):
    ims.append((plt.pcolor(x, y, base + add, norm=plt.Normalize(0, 30)),))

im_ani = animation.ArtistAnimation(fig2, ims, interval=50, repeat_delay=3000,
    blit=True)
#im_ani.save('im.mp4', metadata={'artist':'Guido'})

plt.show()
"""
#---------Imports
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#---------End of imports

fig = plt.Figure()

x = np.arange(0, 2*np.pi, 0.01)        # x-array

def animate(i):
    line.set_ydata(np.sin(x+i/10.0))  # update the data
    return line,

root = Tk.Tk()

label = Tk.Label(root,text="SHM Simulation").grid(column=0, row=0)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(column=0,row=1)

ax = fig.add_subplot(111)
line, = ax.plot(x, np.sin(x))
ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=False)

Tk.mainloop()"""