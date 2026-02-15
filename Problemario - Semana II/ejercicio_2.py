"""
Geometric Topology Microservice: Un servicio de mapas necesita clasificar zonas de
cobertura representadas por triángulos. Dados tres ángulos internos, desarrolla un
algoritmo que determine si el área de cobertura es un Triángulo Equilátero (3 ángulos
iguales), Isósceles (2 iguales), Escaleno (todos distintos) o si incluye un Ángulo Recto
(90°).
"""

def clasificar_triangulo(a, b, c):
    if not (round(a + b + c, 2) == 180):
        return "Triangulo invalido. Sus angulos no son iguales a 180"

    types = []
    
    if a == 90 or b == 90 or c == 90:
        types.append("Rectangulo")

    elif a == b == c:
        types.append("Equilatero")
    elif a == b or b == c or a == c:
        types.append("Isosceles")
    else:
        types.append("Escaleno")

    return "".join(types)

print(clasificar_triangulo(60, 60, 60))