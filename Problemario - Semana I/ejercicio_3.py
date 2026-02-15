"""
Formato de Reportes: Un reporte de ventas debe verse profesional. Tienes tres variables:
producto, cantidad y precio. Tu tarea es imprimir una sola línea que diga: "Venta de
[producto]: [cantidad] unidades a un precio de $[precio] cada una", usando f-strings para
que el código sea limpio y moderno.
"""


def factura():
    producto = input("Indica el nombre del producto: ")
    
    while True: # Validacion de datos para las unidades
        try: 
            unidades = int(input("Indique cuantas unidades se vendieron: "))
            if unidades < 1:
                print ("ERROR. La venta debe de ser de minimo 1 unidad. Intente nuevamente")
            else:
                break
        except ValueError:
            print ("Debes ingresar un numero entero valido. Intenta nuevamente")
        
    precio_unitario = float(input("Indique el precio unitario del producto: "))
    
    print(f"Venta de {producto}: {unidades} unidades a un precio de {precio_unitario}$ cada una")
    
factura()