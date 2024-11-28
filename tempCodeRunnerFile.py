import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters for the modified hyperboloid
a = 2  # Scaling along x-axis
b = 2  # Scaling along y-axis
c = 2  # Scaling along z-axis
thickness_factor = 30  # Controls the middle thickness effect

# Create a grid of points for the u (angle) and v (height) parameters
u = np.linspace(0, 2 * np.pi, 96)
v = np.linspace(-5, 5, 96)
u, v = np.meshgrid(u, v)

# Gaussian-like term for thickness modification
gaussian_thickness = 1 + thickness_factor * np.exp(-0.2 * v**2)

# Modified parametric equations for the hyperboloid of one sheet with thicker middle
x = a * gaussian_thickness * np.cosh(v) * np.cos(u)
y = b * gaussian_thickness * np.cosh(v) * np.sin(u)
z = c * np.sinh(v)