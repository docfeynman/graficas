import matplotlib.pyplot as plt
import numpy as np

teta=np.linspace(0 ,2*np.pi,1000)
r=2 - 2 * np.sin(teta) + np.sin(teta) * (np.sqrt(np.abs(np.cos(teta)))) / (np.sin(teta) + 1.4)
x = r*np.cos(teta)
y = r*np.sin(teta)
plt.plot(x,y)
#plt.plot(t , y,linewidth=3, color='b',markersize =9, label = 'y= r sen(t)')
#plt.legend()
plt.title('x=r cos(0), y=r sen(0)$')
#plt.xlabel('Eje x', fontsize = 10)
#plt.xlabel('Eje y', fontsize = 10)
a = plt.gca()
#plt.fill_between(x,y,color='r')
a.set_facecolor('k')
#plt.grid(True)
#plt.fill_between(t,x,y,color='r')
#plt.axis('equal')
#plt.axis('off')
plt.savefig('parte5.png')