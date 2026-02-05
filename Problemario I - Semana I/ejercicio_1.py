"""
Calculo de ganancia: Como analista junior, debes calcular la ganancia neta de un
producto. Solicita el "Precio de Venta" y el "Costo de Fabricación". Resta el costo del
precio y muestra el resultado. Asegúrate de usar números con decimales (float) para que
el cálculo sea exacto para la contabilidad.
"""

while True:
    costo = float(input("Ingresa el costo de fabricacion del producto: "))
    precio = float(input("Ingresa el precio de venta del producto: "))
    ganancia = precio-costo 
    
    if costo < precio:  #Se agrega condicional para los casos en los que el precio de la venta sea menor al costo de fabricacion.

        print(f"La ganancia es de {ganancia}$")
    else:
        print(f"Se perdieron {abs(ganancia)}$")  #La funcion abs() nos arroja el valor absoluto