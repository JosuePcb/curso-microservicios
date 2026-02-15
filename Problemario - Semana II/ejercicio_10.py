"""
Microservice Rate-Limiter Logic: Un sistema de Rate Limiting permite un máximo de
solicitudes por segundo. Crea un programa que transforme la siguiente lógica en código:
"Si el usuario es 'Premium', permite hasta 1000 peticiones; si es 'Standard', permite 100.
Si el servidor está en 'Mantenimiento' (Booleano), permite 0 para todos". El programa
debe recibir el tipo de usuario y el estado del servidor, devolviendo el límite permitido.
"""

def obtener_limite_peticiones(tipo_usuario, en_mantenimiento):
    if en_mantenimiento:
        return 0

    if tipo_usuario == "Premium":
        limite = 1000
    elif tipo_usuario == "Standard":
        limite = 100
    else:
        limite = 0
        
    return limite

print(obtener_limite_peticiones("Premium", False))  
print(obtener_limite_peticiones("Standard", True))