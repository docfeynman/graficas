
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 4*np.pi, 200)
sx = np.cos(2*x) + np.sin(2*x)
vx = 2*np.sin(2*x) + 3*np.cos(3*x)
plt.plot(x, sx, 'o', linewidth=3, color='b', markersize=10, label = 's(x) = cos(2x) + sin(2x)')
plt.plot(x, vx, 'o', linewidth=3, color='g', markersize=10, label = 'v(x) = -2sin(2x) + 3cos(3x)')
plt.legend()
plt.xlabel('Eje X', fontsize = 14)
plt.ylabel('Eje Y', fontsize = 14)
plt.title('Gráfico de: s(x) = cos(2x) + sin(2x) y v(x) = -2sin(2x) + 3cos(3x) ')
a = plt.gca()
a.set_facecolor('k')
plt.grid(True)
plt.savefig('Grafica5.png')