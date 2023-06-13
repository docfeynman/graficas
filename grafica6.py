import matplotlib.pyplot as plt
import numpy as np

x =np.linspace(0 , 2, 100)
fx=x*np.exp(-3*x)
gx=np.exp(-3*x)*(1-3*x)
plt.plot(x , fx, '<',linewidth=3, color='c',markersize =10, label = 'f(x) = xe^-3x')
plt.plot(x , gx, '<',linewidth=3, color='m',markersize =10, label = 'g(x) = e^-3x(1-3x)')
plt.legend()
plt.title('f(x) = xe^-3x , v(x) = e^-3x(1-3x) $')
plt.xlabel('Eje x', fontsize = 10)
plt.xlabel('Eje y', fontsize = 10)
a = plt.gca()
a.set_facecolor('k')
plt.grid(True)
plt.savefig('graficala6.png')