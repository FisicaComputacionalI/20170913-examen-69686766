import matplotlib.pyplot as plt 
import numpy as np 
#definimos las variables y el rango en que corren
x=np.arange(0.0, 21, 1)
y=np.arange(1096, 2017, 1)

t1=np.arange(0.0, 5, 0.2 )
t2=np.cos(2*np.pi*t1)*4
#crea el grupo de graficas
plt.figure(1)
#crea en el lienzo con dos renglones, una columna y entra en la primera seccion 
plt.subplot(211)
#grafica la variable x contra 