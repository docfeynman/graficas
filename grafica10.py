import matplotlib.pyplot as plt
import numpy as np

t =np.linspace(-2*np.pi , 2*np.pi ,100)
x=t+2*np.sin(2*t)
y=t+2*np.cos(5*t)
plt.plot(t , x,'<',linewidth=3, color='w',markersize =9, label = 'x= t+2sin(2t)')
plt.plot(t , y, '<',linewidth=3, color='b',markersize =9, label = 'y=t+2cos(5*t)')
plt.legend()
plt.title('x= t+2sin(2t), y=t+2cos(5*t)$')
plt.xlabel('Eje x', fontsize = 10)
plt.ylabel('Eje y', fontsize = 10)
a = plt.gca()
a.set_facecolor('k')
plt.grid(True)
plt.savefig('graficala10.png')