"""
The Swiss-Army API Calculator: Diseña un endpoint de cálculo integral que reciba una
operación y dos números. El sistema debe soportar suma, resta, multiplicación, división,
y además, dos operaciones avanzadas: Serie Fibonacci (generar los primeros N números)
y Conversión de Bases (convertir el resultado a Binario y Hexadecimal).

Operaciones:

suma
resta
multiplicacion
division
fibonacci
conversion_bases
"""

def calculadora_endpoint(operacion, num1, num2=None): 
    try:
        resultado = None
        
        # Operaciones Básicas
        if operacion == "suma":
            resultado = num1 + num2
        elif operacion == "resta":
            resultado = num1 - num2
        elif operacion == "multiplicacion":
            resultado = num1 * num2
        elif operacion == "division":
            if num2 == 0: return {"error": "División por cero"}
            resultado = num1 / num2
            
        # Operaciones Avanzadas
        elif operacion == "fibonacci": # RETORNA UNA LISTA CON LOS VALORES DE LA SERIE
            n = int(num1) 
            serie = [0, 1]
            if n <= 0: return {"operacion": "fibonacci", "serie": []}   # RETORNAR LISTA VACIA 
            if n == 1: return {"operacion": "fibonacci", "serie": [0]} # SE RETORNA EL PRIMER VALOR DE LA LISTA, 0
            
            while len(serie) < n: # SE REPITE HASTA QUE LA CANTIDAD DE VALORES DE LA LISTA SEA IGUAL AL NUMERO INGRESADO
                serie.append(serie[-1] + serie[-2]) # SE SUMAN LOS ULTIMOS 2 VALORES DE LA LISTA
            return {"operacion": "fibonacci", "serie": serie[:n]}
            
        elif operacion == "conversion_bases":
            valor = int(num1)
            return {
                "decimal": valor,
                "binario": bin(valor),
                "hexadecimal": hex(valor).upper()
            }
        
        else:
            return {"ERROR. Operación no soportada"}

        return {"operacion": operacion, "resultado": resultado}
    except Exception as e:
        return {"error": str(e)}