import matplotlib.pyplot as plt
import numpy as np

n_points = 100

x = np.random.randint(0, 500, n_points)
y = x + 30 * np.random.randn(n_points)

size = np.random.randint(0, 500, n_points)
color = np.random.randint(0, 10, n_points)
plt.scatter(x, y, s=size, c=color)
plt.show()
