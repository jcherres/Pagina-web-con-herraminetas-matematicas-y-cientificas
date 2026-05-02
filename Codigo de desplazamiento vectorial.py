# Calcular el desplazamiento vectorial de un objeto.
import math

def calcular_desplazamiento(x1, y1, x2, y2):
    resultado = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return resultado

x1 = float(input("¿En donde empieza x?: "))
y1 = float(input("¿En donde empieza y?: "))
x2 = float(input("¿En donde termina x?: "))
y2 = float(input("¿En donde termina y?: "))
unidad = input("Unidad del desplazamiento: ")

resultado = calcular_desplazamiento(x1, y1, x2, y2)
print("El desplazamiento vectorial es de: ", resultado , " ", unidad, sep="")
