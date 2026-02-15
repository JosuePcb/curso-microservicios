"""
Payload Integrity Checksum: Para asegurar que un mensaje de una API no fue alterado,
se calcula la suma de los valores ASCII de sus caracteres. Crea un script que reciba un
string, sume el valor numérico de cada carácter y determine si el resultado es un
número par (indicativo de "Paquete Íntegro" en este ejemplo ficticio).
"""

def verificar_integridad_mensaje(mensaje):
    suma_ascii = 0

    for caracter in mensaje:
        suma_ascii += ord(caracter)
    
    es_par = (suma_ascii % 2 == 0)
    
    return es_par

print(verificar_integridad_mensaje("Hola"))