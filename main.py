
import matplotlib.pyplot as plt 
import numpy as np 

# definimos las variables y el rango en el que cambian 

x=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)
y=(1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017)

t1=np.arange(0.0,5,0.2)
#Tu definici'on del coseno no es apropiada. Te falt'o aniadir como cosntante el anio en el que entraste a la universidad.
t2=np.cos(2*np.pi*t1)*4
#creamos e lgrupo de graficas 
plt.figure(1)
#creamios el lienzo con dos renglones y una columna y entramos a la primera seccion
plt.subplot(211)
#graficamos la variable x contra la variable y 
plt.plot(x, y, 'k--' )
plt.xlabel('anion')
plt.ylabel('edad')
#entramos en la segunda seccion 
plt.subplot(212)
#graficamos solamente la variable t1 con la variable t2
plt.plot(t1, t2, 'k')
#guardamos la grafica 
plt.savefig('grafica3.png')
#muestra la grafica3
plt.show()
