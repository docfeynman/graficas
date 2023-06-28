import matplotlib.pyplot as plt
import numpy as np

t =np.linspace(0 , 4*np.pi ,100)
ft=np.sin(3*t)*np.cos(2*t)
gt=1/2 *np.cos(t)+5/2*np.cos(5*t)
plt.plot(t , ft, '<',linewidth=3, color='c',markersize =10, label = 'f(t) = sin(3t)cos(2t)')
plt.plot(t , gt, '<',linewidth=3, color='m',markersize =10, label = 'g(t) = 1/2 cos(t)+5/2 cos(5t)')
plt.legend()
plt.title('f(t) = sin(3t)cos(2t) , g(t) = 1/2 cos(t)+5/2 cos(5t)$')
plt.xlabel('Eje x', fontsize = 10)
plt.xlabel('Eje y', fontsize = 10)
a = plt.gca()
a.set_facecolor('k')
plt.grid(True)
plt.savefig('graficala7.png')