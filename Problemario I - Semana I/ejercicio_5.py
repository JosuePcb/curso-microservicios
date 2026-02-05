"""
Bases de datos distribuida: Para optimizar una base de datos distribuida, los registros
deben enviarse a diferentes servidores según su ID único. Desarrolla un componente que
evalúe un número entero N ingresado por consola; si el ID es par, el sistema debe imprimir
"Servidor A", y si es impar, "Servidor B". Este ejercicio evalúa tu comprensión de
operadores aritméticos de residuo y bifurcación lógica simple.
"""

def main():
    while True:
        try:
            num = int(input("Ingrese un numero entero: "))
            if num%2 == 0:
                print("Servidor Par")
            else:
                print("Servidor Impar")
        except ValueError:
            print("ERROR. Debes ingresar un numero entero")
            
main()