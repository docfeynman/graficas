from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 10)
y = np.linspace(-5, 5, 10)

X, Y = np.meshgrid(x, y)
Z = np.abs(np.cos(X) + np.cos(Y))**1/2

ax = plt.axes(projection='3d')
ax.plot_wireframe(X, Y, Z, color='black')
ax.plot_surface(X, Y, Z, color = '#FAEBD7', linewidth = 0)#no veo un cambio claro con linewidth = 0
ax.set_title('z = |cos(x)+cos(y)|^1/2')
plt.savefig('superficie3.png')