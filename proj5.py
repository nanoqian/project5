# Project 05

# Electric field visualization

import sympy as sp
import math

# Symbols

t = sp.symbols('t')

# Operation

f = sp.sin(t)
g = sp.tan(t)


# Plot this
p = sp.plot_parametric(f,g, (t,0, 2*sp.pi))