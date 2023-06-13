import matplotlib.pyplot as plt
import numpy as np

x =np.linspace(-1 , 5, 100)
fx=2*x**2-8*x-11
plt.plot(x , fx, '<',linewidth=3, color='r',markersize =10)
plt.title('$2x^2-8x-11$')
plt.xlabel('Eje x', fontsize = 14)
a = plt.gca()
a.set_facecolor('k')
plt.grid(True)
plt.savefig('graficala2.png')