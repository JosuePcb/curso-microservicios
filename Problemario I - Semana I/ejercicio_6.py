"""
Backend Logistico Dinamico: Diseña el backend de una aplicación de transporte que
calcule costos en tiempo real. El usuario selecciona un tipo de vehículo (Pickup: $6.00,
Gandola: $7.00, Mudanza: $10.00$) y define una distancia en kilómetros. El sistema debe
aplicar un recargo de $1.50 por cada kilómetro recorrido y generar un reporte final que
deslose el precio base, el costo por distancia y el monto total facturado.
"""
# FUNCION PARA DESPLEGAR MENUS UTILIZANDO LISTAS COMO PARAMETRO
def menu(opciones,mensaje):
    while True:
        i = 1
        print(mensaje)
        for op in opciones:
            print(f"[{i}] {op}")
            i += 1
        
        
        try: #VALIDACION DE DATOS
            op = int(input(">>> "))
            if op <= i-1 and op > 0:
                return op-1 # Retorna la opcion elegida
            else:
                print("El numero ingresado esta fuera del rango de las opciones. Intenta nuevamente.") # ERROR SI SE ELIGE NUMERO FUERA DE RANGO DE OPCIONES
        except ValueError:
            print("Error: Ese no es un numero entero. Intenta nuevamente.") # ERROR SI SE INGRESA OTRO DATO QUE NO SEA UN ENTERO

# FUNCION QUE GENERARA EL REPORTE, USANDO COMO PARAMETRO LA LISTA CON PRECIOS
def reporte(vehiculo):
    precio_kilometro = 1.50
    try:
        distancia = float(input("Ingrese la distancia en kilometros: "))
        costo_total = distancia*precio_kilometro
        
        return f"Precio base: {vehiculo}$\nCosto por distancia de {distancia}km: {costo_total}\nMonto total: {vehiculo+costo_total}"
        
    except ValueError:
        print("ERROR. Debes ingresar una distancia expresada en kilometros")
    
    return


# SE DEFINEN LAS LISTAS CON LOS VEHICULOS Y SUS PRECIOS.
vehiculos = ["Pickup $6.00","Gandola $7.00","Mudanza $10.00"]
precios_vehiculo = [6.00, 7.00, 10.00]

tipo_vehiculo = menu(vehiculos, "Escriba el numero de la opcion que desea: ")

print(reporte(precios_vehiculo[tipo_vehiculo]))

# NOTA: Trate de hacer un codigo minimamente reutilizable para otros ejercicios.