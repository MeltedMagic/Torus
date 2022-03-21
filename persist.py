import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from ripser import ripser
from persim import plot_diagrams

## Objective: Import data from csv and calculate
## > persistent homology

T = np.genfromtxt('torus.csv', delimiter=',')  ## Import csv
d = 1.5

## vary threshold, it is the diameter
diagram = ripser(T, maxdim=1, thresh=d)['dgms']
plot_diagrams(diagram, show=True)