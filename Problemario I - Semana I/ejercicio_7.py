"""
Transacción Validada: Un procesador de pagos requiere validar la integridad de las
transacciones antes de su registro. Implementa un flujo que solicite al usuario un método
de pago y su respectiva clave de validación: si es "Pago Móvil", debe poseer exactamente
8 dígitos; si es "Tarjeta", debe poseer 16. El programa debe utilizar estructuras de control
para rechazar entradas con longitudes incorrectas o caracteres no numéricos.
Pista: Necesitas dos validaciones: len(variable) para contar los caracteres y .isdigit() para
asegurar que no metieron letras. Usa un if anidado o operadores lógicos and para verificar
que ambas condiciones se cumplan al mismo tiempo.
"""
while True:
    metodo_pago = input("Elija un metodo de pago (Pago movil/Tarjeta): ").lower()
    if metodo_pago == "pago movil" or metodo_pago == "tarjeta":

        clave = input("Ingrese su clave: ")
        
        if metodo_pago == "pago movil" and len(clave) == 8 and clave.isdigit():
            print("Transaccion valida")
            
        elif metodo_pago == "tarjeta" and len(clave) == 16 and clave.isdigit():
            print("Transaccion valida")
        else:
            print("Transaccion invalida")
    else:
        print("ERROR. Ingrese un metodo de pago valido")