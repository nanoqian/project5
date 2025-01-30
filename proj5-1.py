import numpy as np
import matplotlib.pyplot as plt
from functools import reduce, partial

class Charge:
    def __init__(self, x: float, y: float, charge: float) -> None:
        self.x = x
        self.y = y
        self.energy = charge

def field_from_charge(X, Y, charge: Charge):
    # Make each point a unit vector pointing away from the charge
    U = X - charge.x
    V = Y - charge.y
    magnitudes = np.sqrt(U**2 + V**2)
    U /= magnitudes
    V /= magnitudes
    
    # Scale the vectors by the energy from the charge
    energy = charge.energy / ((X - charge.x)**2 + (Y - charge.y)**2)
    U *= energy
    V *= energy
    
    return U, V

def add_tuple(A, B):
    Ax, Ay = A
    Bx, By = B
    return Ax + Bx, Ay + By

def field_from_charges(X, Y, charges: list[Charge]):
    # The field from multiple charges is the sum of the field from each charge
    return reduce(add_tuple, map(partial(field_from_charge, X, Y), charges))

X, Y = np.meshgrid(np.linspace(-10, 10, 20), np.linspace(-10, 10, 20))
U, V = field_from_charges(X, Y, [Charge(-5, 0, 1), Charge(5, 0, -1)])

plt.quiver(X, Y, U, V)
plt.show()
