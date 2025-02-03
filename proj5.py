import numpy as np
import matplotlib.pyplot as plt
from functools import reduce, partial

class Charge:
    def __init__(self, x: float, y: float, charge: float) -> None:
        self.x = x
        self.y = y
        self.charge = charge

def field_from_charge(X, Y, charge: Charge, epsilon=1e-12, min_distance=0.5):
    U = X - charge.x
    V = Y - charge.y
    magnitudes = np.sqrt(U**2 + V**2)
    magnitudes = np.where(magnitudes < min_distance, min_distance, magnitudes)
    U /= magnitudes
    V /= magnitudes
    energy = charge.charge / (magnitudes**2)
    U *= energy
    V *= energy
    return U, V

def add_tuple(A, B):
    Ax, Ay = A
    Bx, By = B
    return Ax + Bx, Ay + By

def field_from_charges(X, Y, charges: list[Charge]):
    return reduce(add_tuple, map(partial(field_from_charge, X, Y), charges))

X, Y = np.meshgrid(np.linspace(-10, 10, 200), np.linspace(-10, 10, 200))

charges = [Charge(-5, 0, 1), Charge(5, 0, -1)]
U, V = field_from_charges(X, Y, charges)

plt.quiver(X, Y, U, V, scale=30)
plt.show()