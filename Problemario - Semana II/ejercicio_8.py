"""
Node Proximity Service: En una red de microservicios, necesitamos saber la distancia
entre dos nodos en un plano cartesiano. Dados los puntos (x1,y1) y (x2,y2), calcula la
distancia euclidiana y devuelve un booleano True si los nodos están a menos de 10
unidades de distancia (Rango de proximidad).
"""

import math

def verificar_proximidad_nodos(x1, y1, x2, y2):

    delta_x = x2 - x1
    delta_y = y2 - y1
    
    distancia = math.sqrt(delta_x**2 + delta_y**2)
    
    umbral = 10
    
    cerca = distancia < umbral
    
    return cerca