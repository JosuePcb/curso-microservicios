"""
Edge Case Latency Auditor: Un analista de datos debe identificar picos de latencia
sospechosos. Escribe un programa que reciba una lista de tiempos de respuesta y
determine si el promedio excede un "Umbral Crítico" (Input del usuario). El resultado
debe ser un booleano que dispare una alerta si el promedio es mayor al umbral o si al
menos un valor individual triplica el promedio.
"""

def auditor_latencia_critica(tiempos_respuesta, umbral_critico):

    if not tiempos_respuesta:
        return False

    suma_tiempos = sum(tiempos_respuesta)
    total_elementos = len(tiempos_respuesta)
    promedio = suma_tiempos / total_elementos

    excede_umbral = promedio > umbral_critico
    
    pico_sospechoso = False
    limite_pico = promedio * 3

    for tiempo in tiempos_respuesta:
        if tiempo > limite_pico:
            pico_sospechoso = True
            break  

    disparar_alerta = excede_umbral or pico_sospechoso

    return disparar_alerta

datos = [10, 12, 15, 100, 11] 
umbral = 50
print(auditor_latencia_critica(datos, umbral))