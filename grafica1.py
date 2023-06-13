#f(x)=5-4x-x^2
#-6 a 2, 200 puntos, en el eje x sale eje x y es color verde
#f(x)=2x^2-8x-11
#-1 a 5 y son 100 puntos,color rojo tamaño del marcador 10,dice eje x y eje y
#f(t)=t*exp^-2t
#-1 a 5 y son 300 puntos y el color es k y el tamaño es 10,tiene que escribir la exprecion en la grafica 
#h(t)=sin(2t)*e^-0.1t
#0 a 24 y son 250 puntos
#s(x)=cos(2x)+sen(2x) , v(x)=-2sen(2x)+3cos(3x)
#primeraa expñercion color azul la segunda color rojo, 0 a 4pi con 200 puntos
#f(x)=xe^-3x ,g(x)=1-3xe^-3x, f(x es color cian y g(color magenta)),lleva eje x y y titulo y leyenda 0 a 2 y son 100puntos
#f(t)=sen(st)*cos(2t),g(t)=1/2cos(t)+5/2cos(st)  de 0 a 4pi y son 100 puntos color igual a la pasada 
#x(t)=(1+sin(t)*cos(t)) , y(t)=(1+2sen(t))(sin(t))   de 0 a 2pi y son 100 puntos 

import matplotlib.pyplot as plt
import numpy as np

x =np.linspace(-6 , 2, 200)
fx=5-4*x - x**2
plt.plot(x , fx, '<',linewidth=3, color='g',markersize =10)
plt.title('$F(x) = 5 -4x -x^2$')
plt.xlabel('Eje x', fontsize = 14)
a = plt.gca()
a.set_facecolor('k')
plt.grid(True)
plt.savefig('graficala1.png')
