# -*- coding: utf-8 -*-
"""
Advection-Diffusion equation

@author: Arman Mansouri
"""

import numpy as np
import matplotlib.pyplot as plt

# Time-step, grid spacing, and grid size
delta_t = 0.02
delta_x = 0.05 
gridsize = 5
gridN = int(gridsize/delta_x)

# Arrays representing the quantity f. Initialized so that f(x,0) = g(x,0) = x
f = np.linspace(0, gridsize, gridN)
g = np.linspace(0, gridsize, gridN)

u = -0.1
D1 = 1 
D2 = 10 #Diffusion coefficients

# Constants that will be used in implementing the advection-diffusion equation
alpha = (u * delta_t)/delta_x
beta1 = (D1 * delta_t)/(delta_x)**2
beta2 = (D2 * delta_t)/(delta_x)**2

# Grid
xvals = np.linspace(0, gridsize, gridN)

# Setting up the plots as subplots in one window
plt.ion()
fig, (ax1, ax2) = plt.subplots(1,2, figsize = (8, 4))

x1, = ax1.plot(xvals, f, 'ro', color = "blue")
ax1.set_xlim([-0.5, gridsize +0.5])
ax1.set_ylim([-1, 5])
ax1.grid()
ax1.set_title("Advection-diffusion with D = 1")

x2, = ax2.plot(xvals, f, 'ro', color = "blue")
ax1.set_xlim([-0.5, gridsize + 0.5])
ax2.set_ylim([-1, 5])
ax2.grid()
ax2.set_title("Advection-diffusion with D = 10")

fig.canvas.draw()

# Iterating
for n in range(700):
    # Implicit implementation of diffusion
    A1 = np.eye(gridN) * (1 + 2 * beta1) + np.eye(gridN, k=1) * -beta1 + np.eye(gridN, k=-1) * -beta1 
    f = np.linalg.solve(A1, f) 
    
    A2 = np.eye(gridN) * (1 + 2 * beta2) + np.eye(gridN, k=1) * -beta2 + np.eye(gridN, k=-1) * -beta2 
    g = np.linalg.solve(A2, g) 
    
    # Advection using Lax-Friedrich
    f[1:-1] = 0.5 * (f[2:] + f[:-2]) - 0.5 * alpha * (f[2:]-f[:-2])
    g[1:-1] = 0.5 * (g[2:] + g[:-2]) - 0.5 * alpha * (g[2:]-g[:-2])
    
    # Plotting
    x1.set_ydata(f)
    x2.set_ydata(g)
    fig.canvas.draw()
    plt.pause(0.001)
