
    # En otro archivo o en la consola de Python
from rotacion import rotar
import numpy as np

# Rotar el punto (1, 0, 0) 90 grados (π/2 radianes) alrededor del eje Z
resultado = rotar(0, 1, 0, np.pi/2, 'z')
print(f"Punto rotado: {resultado}")