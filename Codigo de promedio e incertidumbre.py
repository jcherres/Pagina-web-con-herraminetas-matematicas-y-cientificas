# Calcular el promedio y la incertidumbre de un conjunto de datos
def calcular_estadistica(datos):
    n = len(datos)
    if n == 0:
        return None, None
    
    promedio = sum(datos) / n
    variaza = sum((x - promedio) ** 2 for x in datos) / n
    incertidumbre = (variaza) ** 0.5
    return (promedio, incertidumbre)

mis_datos = []
print("Ingrese los datos estadisticos:")

while True:
    entrada = input("Ingrese un dato (o 0 para terminar): ")
    if entrada == "0":
        break
    try:
        dato = float(entrada)
        mis_datos.append(dato)
    except ValueError:
        print("Entrada no valida. Por favor, ingrese un numero.")

promedio, incertidumbre = calcular_estadistica(mis_datos)

if promedio is not None:
    print(f"El promedio es: {promedio}")
    print(f"La incertidumbre es: +-{incertidumbre}")
else:
    print("No hay datos suficientes para calcular la estadistica.")