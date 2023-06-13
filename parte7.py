import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 4*np.pi,400)
r = 105+100*np.sin(4.5*t)
l = t-(np.cos(10*t)/10)
x = 320 + r*np.cos(l)
y = -240-r*np.sin(l)

plt.title('x= 320+rcos(λ), y= -240-r sen(λ)$')
plt.fill_between(x,y,color='b')
plt.grid(True)
plt.axis('equal')
plt.axis('off')

plt.savefig('parte7.png')