import numpy as np
from matplotlib import pyplot as plt
from numpy import sin, cos, pi

n = num_segments = 5

rat = 1
cx = 0
cy = 0

angle = np.linspace(0, 2*np.pi, n + 1)
x = rat * np.cos(angle) + cx
y = rat * np.sin(angle) + cy

plt.plot(x, y, color="red", markersize=1)
plt.plot(x, y, 'bo')


plt.title("Inscribed Polygon")
plt.xlabel("X")
plt.ylabel("Y")
plt.gca().set_aspect('equal')
plt.grid()
plt.show()


print("El poligono regular es de",n, "lados.","\n Su angulo interno central es de", 360/n, "grados.")
print("Los angulos tangenciales a la circunferencia miden", 180*(n-2)/n,"grados")
print("Cada arista tiene una medida de",np.sin(2*pi/n)/np.sin(pi/2*(n-2)/n))
print("las coordenadas de los vertices de los poligonos son:")
for i in range(n):
    print( (np.cos(i*2*pi/n) , np.sin(i*2*pi/n)))

print("El area de este poligono regular es de",(n/2)*np.sin(2*pi/n) )
    
