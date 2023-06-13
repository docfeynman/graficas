import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 1500)
r = -250*np.sin(5*t)*np.cos(4*t)
l = t + np.sin(r/100)
x = 320+r*np.cos(l)
y = -240-r*np.sin(l)

plt.title('x= 320+r cos(λ), y=-240-r sen(λ)$')
plt.xlabel('Eje x', fontsize = 10)
plt.xlabel('Eje y', fontsize = 10)
plt.fill_between(x,0,y,color='b')
plt.grid(True)
plt.axis('equal')
plt.axis('off')
plt.savefig('parte6.png')