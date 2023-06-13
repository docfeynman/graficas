import matplotlib.pyplot as plt
import numpy as np

t =np.linspace(0 , 24, 250)
ht=np.exp(-0.1*t)*np.sin(2*t)
plt.plot(t , ht, '<',linewidth=3, color='w',markersize =10)
plt.title('e^-0.1*sen(2t)$')
plt.xlabel('Eje x', fontsize = 10)
a = plt.gca()
a.set_facecolor('k')
plt.grid(True)
plt.savefig('graficala4.png')