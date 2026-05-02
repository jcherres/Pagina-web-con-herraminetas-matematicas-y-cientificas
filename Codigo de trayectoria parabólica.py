#Calcular la trayectoria parabólica de un proyectil.
import math

def calcular_trayectoria(velocidad_inicial, angulo, tiempo, gravedad):
     rad = math.radians(angulo)
     resultado = (velocidad_inicial * math.sin(rad) * tiempo) - (0.5 * gravedad * tiempo**2)
     return resultado

vi = float(input("Velocidad inicial: "))
ang = float(input("Angulo: "))
t = float(input("Tiempo: "))
g = float(input("Gravedad del lugar: ")) # En la Tierra, g = 9.81 m/s**2
unidad = input("Unidad: ")

resultado = calcular_trayectoria(vi, ang, t, g)  
print("La trayectoria parabólica es de: ", resultado , " ", unidad, sep="")