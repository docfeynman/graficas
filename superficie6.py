from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1 , 10)
y = np.linspace(-1, 1 , 10)

X, Y = np.meshgrid(x, y)
Z = np.cos(np.abs(X)+np.abs(Y))*(np.abs(X)+np.abs(Y))

ax = plt.axes(projection='3d')
ax.plot_wireframe(X, Y, Z, color='black')        
ax.plot_surface(X, Y, Z, color = '#DEB887', linewidth = 10)   
ax.set_title('z = cos(|x|+|y|)*(|x|+|y|)')
plt.savefig('superficie6.png')