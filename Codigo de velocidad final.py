# Calcular la velocidad final utilizando la fórmula de movimiento rectilíneo uniformemente acelerado
def calcular_velocidad_final(inicial, aceleracion, tiempo):
    velocidad_final = inicial + (aceleracion * tiempo)
    return velocidad_final

inicial = float(input("ingrese la velocidad inicial en m/s: "))
aceleracion = float(input("ingrese la aceleración en m/s**2: "))
tiempo = float(input("ingrese el tiempo en s: "))

velocidad_final = calcular_velocidad_final(inicial, aceleracion, tiempo)
print("la velocidad final es de", velocidad_final, "m/s")