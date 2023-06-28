import matplotlib.pyplot as plt
import numpy as np

t =np.linspace(0 , 2*np.pi ,100)
xt=(1+2*np.sin(t))*np.cos(t)
yt=(1+2*np.sin(t))*np.sin(t)
plt.plot(t , xt, '',linewidth=3, color='y',markersize =10, label = 'x(t)=(1+2sen(t))cos(t)')
plt.plot(t , yt, '',linewidth=3, color='b',markersize =10, label = 'y(t)=(1+2sen(t)sin(t))')
plt.legend()
plt.title('x(t) = (1+2sen(t))cos(t), y(t)=(1+2sen(t)sin(t)) $')
plt.xlabel('Eje x', fontsize = 10)
plt.ylabel('Eje y', fontsize = 10)
a = plt.gca()
a.set_facecolor('k')
plt.grid(True)
plt.savefig('graficala8.png')