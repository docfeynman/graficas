import matplotlib.pyplot as plt
import numpy as np
import math
t=np.linspace(-1 , 5, 300)
ft=t*np.exp(-2*t)
plt.plot(t , ft, '<',linewidth=3, color='k',markersize =10)
plt.title('$t*exp^-2t$')
plt.xlabel('Eje x', fontsize = 10)
a = plt.gca()
a.set_facecolor('w')
plt.grid(True)
plt.savefig('graficala3.png')