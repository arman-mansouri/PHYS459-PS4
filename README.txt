Name: Arman Mansouri
Python version: 3.x

Python code files:

1. Advection.py : 

- Attempts to numerically solve the advection equation with f(x,0) = 0 using Forward-Time Central-Space (FTCS); the result is unstable. 

- Numerically solves the advection equation with f(x,0) = 0 using the Lax-Friedrichs method and for a choice of time interval, grid spacing and "u" such that the stability condition is satisfied. 

The two attempts are plotted (as they evolve) side-by-side. 

2. Advection-Diffusion.py:

Numerically solves the advection-diffusion equation with f(x,0) = 0 by splitting the operators and:

- updating the diffusion term using the implicit method (matrix inversion)
- calculating the advection term using the Lax-Friedrich method.

This is done for two choices of diffusion coefficients D, and as before, for a choice of time interval, grid spacing and "u" such that the stability condition is satisfied. The two solutions are plotted (as they evolve) side-by-side. We can observe that for the larger D, the stationary state is reached much sooner.

* Note: I unfortunately misnamed this repository; it was meant to be PHYS432-PS4. I have not changed it at the risk of the link become invalid. 
