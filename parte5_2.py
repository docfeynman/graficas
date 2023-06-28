import matplotlib.pyplot as plt
import numpy as np

teta = np.linspace(0, 2*np.pi, 1000)
r = 2 - 2 * np.sin(teta) + np.sin(teta) * (np.sqrt(np.abs(np.cos(teta))) / np.sin(teta) + 1.4)
x = r * np.cos(teta)
y = r * np.sin(teta)

plt.plot(x, y)
plt.fill_between(x, y, color='red') 
plt.title('x=r cos(0), y=r sen(0)')
plt.gca().set_facecolor('k')
plt.axis('equal')  
plt.axis('off')  
plt.savefig('parte5_2.png')
