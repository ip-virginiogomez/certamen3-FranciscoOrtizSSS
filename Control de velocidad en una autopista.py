# Solicita al usuario que ingrese 5 velocidades (en km/h).
# Guarda las velocidades en una lista.
# Calcula el promedio y la velocidad máxima registrada.
# Verifica si todas las velocidades están dentro del límite permitido (entre 60 y 120 km/h).
# Si alguna velocidad supera los 140 km/h o es menor a 20 km/h, muestra una advertencia de peligro.


velocidades = []

for i in range(5):
    velocidad = float(input(f"Ingrese la velocidad del vehiculo {i + 1} (en km/h): "))
    velocidades.append(velocidad)

suma_velocidades = sum(velocidades)
promedio = suma_velocidades / len(velocidades)
velocidad_maxima = max(velocidades)

print("\n--- Resultados del Analisis ---")
print(f"Velocidades registradas: {velocidades}")
print(f"Promedio de velocidad: {promedio:.2f} km/h")
print(f"Velocidad maxima registrada: {velocidad_maxima} km/h")

dentro_de_limites = True
for v in velocidades:
    if v < 60 or v > 120:
        dentro_de_limites = False
        break


if dentro_de_limites:
    print("Todas las velocidades estan dentro del limite permitido (60-120 km/h).")
else:
    print("Al menos una velocidad esta fuera del limite permitido (60-120 km/h).")

for i in range(len(velocidades)):
    v = velocidades[i]
    if v > 140 or v < 20:
        print(f"ADVERTENCIA DE PELIGRO: El vehiculo {i + 1} registro una velocidad extrema de {v} km/h.")
