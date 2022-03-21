import numpy as np
import dionysus as d

points = np.genfromtxt('torus.csv', delimiter=',')
f = d.fill_rips(points, 2, 3.)
p = d.homology_persistence(f)
dgms = d.init_diagrams(p, f)

## Plot
d.plot.plot_bars(dgms[1], show=True)
