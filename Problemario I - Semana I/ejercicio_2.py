"""

Interfaz de Usuario: Todo sistema de análisis comienza con una interfaz de usuario. Tu
tarea es crear un programa que solicite al usuario su nombre y su cargo (ej. "Analista"), y
luego imprima un mensaje de bienvenida personalizado que diga: "Acceso concedido:
Bienvenido, [Nombre], al sistema de [Cargo]". Este ejercicio evalúa tu capacidad para
capturar entradas (input) y concatenar cadenas de texto.

"""

def bienvenida():
    while True:
        nombre = input("Cual es su nombre: ")
        cargo = input("Cual es su cargo. (Analista, Desarrollador): ")
        if nombre.isdigit() or cargo.isdigit():
            print("Datos no validos, no puede ingresar solo datos numericos")
        else:
            print(f"Acceso concedido. Bienvenido {nombre} al sistema de {cargo}")
            break
    
bienvenida()