import matplotlib.pyplot as plt
import numpy as np

t =np.linspace(0 , 2*np.pi ,100)
x=np.sin(3*t)
y=np.sin(4*t)
plt.plot( x , y, linewidth=7, color='c',markersize =7)
plt.title('x= sin(3t), y=sin(4t)$')
a = plt.gca()
a.set_facecolor('w')
plt.grid(True)
plt.savefig('graficala11.png')