import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from ripser import ripser
from persim import plot_diagrams

## Step 1: Setup curve
N = 60  # Number of points to sample
R = 1  # Big radius of torus
r = 1  # Little radius of torus
X = np.zeros((N, 3))
t = np.linspace(0, 2 * np.pi, N)
X[:, 0] = (R + r * np.cos(2 * t)) * np.cos(t)
X[:, 1] = (R + r * np.cos(2 * t)) * np.sin(t)
X[:, 2] = r * np.sin(2 * t)

## Step 2: Compute persistent homology
dgms2 = ripser(X, coeff=3)['dgms']
dgms3 = ripser(X, coeff=4)['dgms']

fig = plt.figure(figsize=(9, 3))
ax = fig.add_subplot(131, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2])
ax.set_aspect('auto')
plt.title("Generated Loop")
plt.subplot(132)
plot_diagrams(dgms2)
plt.title("$\mathbb{Z} / 2$")
plt.subplot(133)
plot_diagrams(dgms3)
plt.title("$\mathbb{Z} / 3$")

plt.tight_layout()
plt.show()
