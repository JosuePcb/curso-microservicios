"""

DataSet de Sensores: Estás trabajando con un dataset de sensores climáticos que envían
datos en grados Celsius, pero el motor analítico global requiere la escala Fahrenheit.
Implementa un algoritmo que reciba una lista de valores flotantes y devuelva una nueva
lista con la conversión aplicada mediante la fórmula: F = (C * 9/5) + 32. El reto consiste en
procesar la colección completa sin alterar los datos originales (inmutabilidad).

"""

def conversion_celcsius_fahrenheit(celsius = list[float]):
    fahrenheit = []
    for c in celsius:
        fahrenheit.append((c * 9/5) + 32)
    return fahrenheit

grados_celsius = [26.0, 38.0, 10.0, 40.0]

print(conversion_celcsius_fahrenheit(grados_celsius))