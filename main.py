import numpy as np 
import matplotlib.pyplot as plt 
# definimos las variable en el rango en el rango en que cambian 
t1=np.arange(0.0, 5, 0.2 )
t2=np.cos(2*np.pi*t1)*4
#graficamos la variable t1 contra la variable t2 con linea punteada de color negro
plt.plot(t1,t2,'k--')
#guardamos la figura que creamos 
plt.savefig('grafica2.png')
#muestra la grafica
plt.show()

