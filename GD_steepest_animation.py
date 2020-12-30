import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

from gradient import GD_steepest

f = lambda x: x*x

x, fx, search = GD_steepest(f, 10, 0.1, 1e-5)
d = pd.DataFrame(search, columns = ['x', 'fx'])
t = np.linspace(-12, 12, 100)
y = [f(s) for s in t]

fig = plt.figure(figsize=(10,6))
plt.xlim(-12, 12)
plt.ylim(-10, 110)
plt.xlabel('x', fontsize=20)
plt.ylabel('f(x)', fontsize=20)
plt.title('Steepest gradient descent',fontsize=20)
plt.plot(t, y, '-')

# points = [plt.plot(x[1]['x'], x[1]['fx'], marker='o', markersize=3, color='red') for x in d.iterrows()]

points = []

def animate(i):
    global points
    for p in points:
        r = p.pop(0)
        r.remove()
    
    points = []
    if i == (len(d)-1):
        c = 'green'
        plt.title(f'Steepest gradient descent (step {i+1}/{len(d)})\nmin at x = {round(x, 2)}, f(x) = {round(fx, 2)}',fontsize=20)
    else:
        c = 'red'
        plt.title(f'Steepest gradient descent (step {i+1}/{len(d)})',fontsize=20)
    points.append(plt.plot(d['x'][i], d['fx'][i], marker='o', markersize=3, color=c))

ani = matplotlib.animation.FuncAnimation(fig, animate, frames=len(d), repeat=False)
plt.show()