import numpy as np


def rot_x(x: float, y: float, z: float, theta: float) -> np.ndarray:
    '''
    Rota un vector tridimensional alrededor del eje X por un ángulo especificado.

    Parametros:
        x (float): Coordenada x del punto a rotar
        y (float): Coordenada y del punto a rotar
        z (float): Coordenada z del punto a rotar
        theta (float): Ángulo de rotación en radianes

    Regresar:
        np.ndarray: Vector rotado como array de NumPy
    '''
    vector = np.array([x, y, z])
    rotation_matrix = np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ])
    return np.dot(rotation_matrix, vector)


def rot_y(x: float, y: float, z: float, theta: float) -> np.ndarray:
    '''
    Rota un vector tridimensional alrededor del eje Y por un ángulo especificado.

    Parametros:
        x (float): Coordenada x del punto a rotar
        y (float): Coordenada y del punto a rotar
        z (float): Coordenada z del punto a rotar
        theta (float): Ángulo de rotación en radianes

    Regresar:
        np.ndarray: Vector rotado como array de NumPy
    '''
    vector = np.array([x, y, z])
    rotation_matrix = np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    return np.dot(rotation_matrix, vector)


def rot_z(x: float, y: float, z: float, theta: float) -> np.ndarray:
    '''
    Rota un vector tridimensional alrededor del eje Z por un ángulo especificado.

    Parametros:
        x (float): Coordenada x del punto a rotar
        y (float): Coordenada y del punto a rotar
        z (float): Coordenada z del punto a rotar
        theta (float): Ángulo de rotación en radianes

    Regresar:
        np.ndarray: Vector rotado como array de NumPy
    '''
    vector = np.array([x, y, z])
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])
    return np.dot(rotation_matrix, vector)


def rotar(x: float, y: float, z: float, theta: float, axis: str) -> np.ndarray:
    '''
    Rota un punto tridimensional alrededor del eje especificado por un ángulo dado.

    Parametros:
        x (float): Coordenada x del punto a rotar
        y (float): Coordenada y del punto a rotar
        z (float): Coordenada z del punto a rotar
        theta (float): Ángulo de rotación en radianes
        axis (string): Eje de rotación; puede tomar valor 'x', 'y' o 'z'

    Regresar:
        np.ndarray: Vector rotado como array de NumPy
    '''
    if axis == 'x':
        return rot_x(x, y, z, theta)
    elif axis == 'y':
        return rot_y(x, y, z, theta)
    elif axis == 'z':
        return rot_z(x, y, z, theta)
    else:
        raise ValueError("El eje debe ser 'x', 'y' o 'z'")
