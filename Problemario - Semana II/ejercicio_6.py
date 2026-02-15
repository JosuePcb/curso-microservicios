"""
Microservice Auth-Token Guard: Las APIs de seguridad validan tokens según reglas
complejas. Desarrolla un validador que reciba un token (string) y devuelva True si: 1)
Tiene más de 12 caracteres, 2) Contiene al menos un número y 3) No empieza con la
palabra "TEST".
"""

def validador_token_auth(token):
    
    longitud_valida = len(token) > 12
    
    no_test = token[:4] != "TEST"
    
    tiene_numero = False
    for caracter in token:
        if caracter.isdigit():
            tiene_numero = True
            break 
        
    return longitud_valida and no_test and tiene_numero 



print(validador_token_auth("ABC123def45678"))  