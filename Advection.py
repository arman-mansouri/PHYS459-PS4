# -*- coding: utf-8 -*-
"""
Advection equation: FTCS and Lax-Friedrich

@author: Arman Mansouri
"""
import numpy as np
import matplotlib.pyplot as plt


# Time-step, grid spacing, and grid size
delta_t = 0.1
delta_x = 0.05 
gridsize = 5
gridN = int(gridsize/delta_x)

# Arrays representing the quantity f. Initialized so that f(x,0) = g(x,0) = x
f = np.linspace(0, gridsize, gridN)
g = np.linspace(0, gridsize, gridN)

u = -0.1

# Constant that will be used in implementing the advection equation
alpha = (u * delta_t)/delta_x

# Grid
xvals = np.linspace(0, gridsize, gridN)

# Setting up the plots as subplots in one window
plt.ion()
fig, (ax1, ax2) = plt.subplots(1,2, figsize = (8, 4))

x1, = ax1.plot(xvals, f, 'ro', color = "blue")
ax1.set_xlim([-0.5, gridsize +0.5])
ax1.set_ylim([-5, 10])
ax1.grid()
ax1.set_title("Forward-Time Central-Space")
ax1.set_xlabel("x")
ax1.set_ylabel("f")

x2, = ax2.plot(xvals, f, 'ro', color = "blue")
ax1.set_xlim([-0.5, gridsize + 0.5])
ax2.set_ylim([-5, 10])
ax2.grid()
ax2.set_title("Lax-Friedrich")
ax2.set_xlabel("x")

fig.canvas.draw()

# Iterating
for n in range(800):
    # Updating the value using FTCS for the advection equation
    f[1:-1] += -0.5 * alpha * (f[2:] - f[:-2])
    
    # Updating the value using Lax-Friedrich for the advection equation
    g[1:-1] = 0.5 * (g[2:] + g[:-2]) - 0.5 * alpha * (g[2:]-g[:-2])
    
    # Plotting
    x1.set_ydata(f)
    x2.set_ydata(g)
    fig.canvas.draw()
    plt.pause(0.001)