from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10 , 50)
y = np.linspace(-10, 10 , 50)

X, Y = np.meshgrid(x, y)
Z = np.sin(np.abs(X)-np.abs(Y))

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, color = '#BF00BF', linewidth = 10)
#ax.plot_wireframe(X, Y, Z, color='black')
               
ax.set_title('z = sin(|x|-|y|)')
plt.savefig('superficie4.png')
