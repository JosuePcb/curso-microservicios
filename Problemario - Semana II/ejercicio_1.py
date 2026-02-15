"""
API Health-Check Validator: En una arquitectura de microservicios, un "Health Check"
determina si un servicio está apto para recibir tráfico. Implementa una función que
reciba tres variables: latencia (ms), uso_cpu (%) y estado_db (booleano). El sistema debe
devolver un único valor booleano True solo si la latencia es menor a 200ms, el CPU está
por debajo del 80% y la base de datos está conectada; de lo contrario, devuelve False.
"""

def health_check():
    while True:
        try:
            latencia = int(input("Ingrese la latencia: "))
            cpu = float(input("Ingrese el porcentaje de uso del CPU: "))
            conexion = input("La base de datos esta funcionando? (y/n): ".lower())
            
            if conexion == "y":
                bd = True
            elif conexion == "n":
                bd = False
            else:
                print("Dato invalido. Ingrese y o n")
                continue
            
            if latencia < 200 and cpu < 80 and bd == True:
                return True
            else: 
                return False
        except ValueError:
            print("Dato invalido. Intenta nuevamente")
            
print(health_check())