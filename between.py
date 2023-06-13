import matplotlib.pyplot as plt
import numpy as np  

x = np.arange(0.0,2,0.01)#crea y devulve a un array valores que se crea tomando en cuenta el inicio los saltos y el final
y1 = np.sin(2*np.pi*x)#defino fucion
y2 = 1.2*np.sin(4*np.pi*x)#defino fucion
#1 subplot
plt.subplot(3,1,1)#aqui creo el trazo de una grafica
plt.fill_between(x,0,y1)#definimos el rango que queremos rellear
plt.ylabel('between y1 and 0')#coloca nombre al eje y de la grafica
#2 subplot
plt.subplot(3,1,2)#aqui creo otra grafica
plt.fill_between(x , y1 , 1)#aqui relleno el espacio
plt.ylabel('between y1 and 1')#coloca nombre al eje de la grafica
#3 subplot
plt.subplot(3,1,3)#aqui creo otro espacio para la grafica
plt.fill_between(x,y1,y2)#aqui relleno el espacio 
plt.ylabel('between y1 and y2')#coloca nombre al eje de la grafica
plt.xlabel('x')#coloca el nombre al eje x de la grafica 3

plt.show()