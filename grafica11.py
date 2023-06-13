import matplotlib.pyplot as plt
import numpy as np

t =np.linspace(0 , 2*np.pi ,100)
x=np.sin(3*t)
y=np.sin(4*t)
plt.plot(t , x,linewidth=7, color='c',markersize =7, label = 'x= sin(3t)')
plt.plot(t , y,linewidth=7, color='b',markersize =7, label = 'y=sin(4t)')
plt.legend()
plt.title('x= sin(3t), y=sin(4t)$')
plt.xlabel('Eje x', fontsize = 5)
plt.xlabel('Eje y', fontsize = 10)
a = plt.gca()
a.set_facecolor('w')
plt.grid(True)
plt.savefig('graficala11.png')