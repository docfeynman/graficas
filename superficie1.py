from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)

X, Y = np.meshgrid(x, y)
Z = X**2 - Y**2

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, color = '#38B7A9', linewidth = 2)
ax.plot_wireframe(X, Y, Z, color='black')#Grafica alambrica ,muestra la grafica original como una malla trasparente y permite ver mejor la grafica
ax.set_title('z = x^2 - y^2')
plt.savefig('superficie1.png')