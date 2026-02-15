"""
Protocol Data Converter (Low-Level): Las APIs a menudo se comunican con hardware
que envía datos en sistemas numéricos distintos. Crea un script que reciba un número
decimal y lo transforme a su representación Binaria y Hexadecimal sin usar las funciones
directas de Python (haciendo las divisiones sucesivas manualmente).
"""

def conversor_protocolo_manual(numero_decimal):
    if numero_decimal == 0:
        return {"binario": "0", "hexadecimal": "0"}

    # --- Conversión a Binario ---
    temp_decimal = numero_decimal
    resultado_binario = ""
    while temp_decimal > 0:
        residuo = temp_decimal % 2
        resultado_binario = str(residuo) + resultado_binario
        temp_decimal //= 2

    # --- Conversión a Hexadecimal ---
    temp_decimal = numero_decimal
    resultado_hexadecimal = ""
    digitos_hex = "0123456789ABCDEF" # CADENA DE NUMEROS HEXADECIMAL
    
    while temp_decimal > 0:
        residuo = temp_decimal % 16
        resultado_hexadecimal = digitos_hex[residuo] + resultado_hexadecimal # SI EL RESIDUO ES 10, VA A DEVOLVER EL VALOR 10 DE LA CADENA Y ASI SUCESIVAMENTE
        temp_decimal //= 16

    return {
        "decimal": numero_decimal,
        "binario": resultado_binario,
        "hexadecimal": resultado_hexadecimal
    }
