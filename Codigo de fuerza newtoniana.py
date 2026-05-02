# Calcular la fuerza de un objeto utilizando la segunda ley de Newton
def calcular_fuerza(masa, aceleracion):
    fuerza = masa * aceleracion
    return fuerza

masa = float(input("ingrese la masa del objeto en kg: "))
aceleracion = float(input("ingrese la aceleración en m/s**2: "))

fuerza = calcular_fuerza(masa, aceleracion)
print("la fuerza es de", fuerza, "N")


