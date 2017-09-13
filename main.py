import numpy as np 
import pylab as pl 
pl.title('crescenciano cuautle coyotl')
# crea un vector con los valores del eje x
x=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)
# titulo del eje
pl.xlabel('anios')
y=(1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017)
pl.ylabel('anio en que naci')
#grafica del vector x contra el vector y
pl.plot(x,y)
#guarda la imagen
pl.savefig('grafica1.png')
