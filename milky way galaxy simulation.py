import numpy as np
import matplotlib.pyplot as plt
angle = np.linspace(0, 4*np.pi, 1000)
a = 0.6 
b = 0.4
h=5
plt.figure()
for i in range(h):
    offset = i * (2*np.pi/h)
    r = a * np.exp(b * angle)
    x = r * np.cos(angle + offset)
    y = r * np.sin(angle + offset)
    plt.scatter(x, y, s=1)
plt.title("Milky Way Galaxy Simulation")
plt.axis("equal")
plt.show()