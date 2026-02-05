"""
Criptografia (Loops): En criptografía, los "números perfectos" son aquellos cuya suma de
divisores (excluyendo el número mismo) es igual al número original. Escribe una función
que reciba un número entero positivo y determine si cumple con esta propiedad. Este reto
exige un uso eficiente de bucles for y acumuladores lógicos para procesar todos los
posibles divisores.
"""

def es_perfecto(numero = int): 
    cont = 0
    for i in range(1, numero):
        if numero%i == 0:
            cont += i
    if cont == numero:
        return True
    else: 
        return False

while True:
    try:
        num = int(input("Ingrese un numero entero: "))
        if es_perfecto(num) == True:
            print("El numero es perfecto")
        else: 
            print("El numero no es perfecto")
    except ValueError:
        print("ERROR. Debes ingresar un numero entero")