"""
Backoff Exponential Algorithm: Cuando un microservicio falla al llamar a otro, se usa
una "Serie Fibonacci" para determinar el tiempo de espera antes de reintentar (1s, 1s,
2s, 3s, 5s...). Crea una función que reciba el número de reintento actual N y devuelva
cuántos segundos debe esperar el sistema según la secuencia de Fibonacci.
"""

def tiempo_espera_fibonacci(reintento_n):
    
    # Casos base para la serie (1s, 1s, 2s...)
    if reintento_n <= 0:
        return 0
    if reintento_n == 1 or reintento_n == 2:
        return 1


    anterior = 1  
    actual = 1    

    for i in range(3, reintento_n + 1):
        siguiente = anterior + actual
        anterior = actual
        actual = siguiente
        
    return actual