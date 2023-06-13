import matplotlib.pyplot as plt
import numpy as np

t =np.linspace(0 , 2*np.pi ,100)
x=np.cos(t)**3
y=np.sin(t)**3
plt.plot(t , x,'<',linewidth=3, color='w',markersize =10, label = 'x= cos^3(t)')
plt.plot(t , y, '<',linewidth=3, color='b',markersize =10, label = 'y=sin^3(t)')
plt.legend()
plt.title('x= cos^3(t), y=sin^3(t)$')
plt.xlabel('Eje x', fontsize = 10)
plt.xlabel('Eje y', fontsize = 10)
a = plt.gca()
a.set_facecolor('k')
plt.grid(True)
plt.savefig('graficala9.png')