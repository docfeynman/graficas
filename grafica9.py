import matplotlib.pyplot as plt
import numpy as np

t =np.linspace(0.0, 2*np.pi ,100)
xt=np.cos(t)**3
yt=np.sin(t)**3
plt.plot(xt,yt,'',linewidth=3, color='w',markersize =4)

#plt.legend()
plt.title('x contra y $')
a = plt.gca()
a.set_facecolor('k')
plt.grid(True)
plt.savefig('graficala9.png')