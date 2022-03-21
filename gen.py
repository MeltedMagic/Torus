import numpy as np
import matplotlib.pyplot as plt

## Generate circles with varying angles
## output is csv file

N = 15  # number of samples
r = 1  # radius
u = 2 * np.pi  # upper bound
T = np.zeros((N, 4))  #Torus numpy array
## angles t(theta), p(phi)
t = np.random.uniform(0, u, N)
s = np.random.uniform(0, u, N)
T[:, 0] = r * np.cos(t)
T[:, 1] = r * np.sin(t)
T[:, 2] = r * np.cos(p)
T[:, 3] = r * np.sin(p)

np.savetxt("torus.csv", T, delimiter=",")

plt.scatter(T[:, 0], T[:, 1], color='purple')
plt.scatter(T[:, 2], T[:, 3], color='r')
plt.show()
