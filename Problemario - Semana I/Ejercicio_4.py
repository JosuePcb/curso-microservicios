"""
Precisión Aritmética en Autoría: En el sector financiero, la precisión es crítica. Tu tarea es
escribir una expresión aritmética en Python que utilice exactamente una multiplicación,
una división, un exponente, una suma y una resta para procesar tres variables de entrada,
de modo que el valor de retorno sea estrictamente igual a $100.25$. Debes demostrar el
dominio de la precedencia de operadores y el manejo de tipos de datos float para evitar
errores de redondeo en auditorías.
"""


a: int = 20
b: int = 5
c: int = 4

retorno: float = (a*b) + (b-c)**2/c

print(f"Ejercicio 4: {retorno:.2f}")