"""
NLP Pattern Identifier: Como parte de un motor de procesamiento de lenguaje natural
(NLP), se te pide identificar caracteres clave. Crea un script que reciba un solo carácter de
texto y determine si pertenece al conjunto de vocales. El programa debe ser robusto
frente a variaciones de caja, tratando 'A' y 'a' como equivalentes, y devolviendo un valor
booleano o un mensaje de confirmación de detección.
"""

def determinar_vocal(caracter):
    if caracter.lower() in "aeiou":
        return True
    else:
        return False
    
while True:
    caracter = input("Ingrese un caracter: ")
    if len(caracter) > 1:
        print ("Debes ingresar 1 solo caracter. Intenta nuevamente")
    elif determinar_vocal(caracter) == True:
            print("El caracter es una vocal")
    else:
        print("El caracter no es una vocal")