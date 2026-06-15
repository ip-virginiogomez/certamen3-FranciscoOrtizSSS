# Se crea una Lista en base a una matriz de 3x3, donde se puede ingresar datos
# De las ventas del dia para al final del dia hacer un calculo exacto de 
# Las ganacias totales.
# Calcula el total de ventas de cada vendedor (suma por fila solamente).
# Identifica qué vendedor tuvo el mayor total de ventas.
# Muestra una alerta si el total de algún vendedor es menor a $30.000.


matriz_ventas = []

for i in range(3):
    ventas_vendedor = []
    print(f"Registro de ventas para el Vendedor {i + 1}:")
    for j in range(3):
        venta = float(input(f"  Ingrese la venta del dia {j + 1}: $"))
        ventas_vendedor.append(venta)
    matriz_ventas.append(ventas_vendedor)

mejor_vendedor = 0
max_ventas = -1.0

print("\n--- Rendimiento por Vendedor ---")

for i in range(3):
    total_vendedor = sum(matriz_ventas[i])
    print(f"Vendedor {i + 1} - Total de ventas: ${total_vendedor:.2f}")
    
    if total_vendedor > max_ventas:
        max_ventas = total_vendedor
        mejor_vendedor = i + 1
        
    if total_vendedor < 30000:
        print(f"  ALERTA: El Vendedor {i + 1} tuvo bajo desempeno (ventas menores a $30.000).")

print(f"\nEl vendedor con el mayor rendimiento es el Vendedor {mejor_vendedor} con un total de ${max_ventas:.2f}")